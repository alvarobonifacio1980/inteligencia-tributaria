"""Amplia dados revisados: CVM histórica/ITR e DIRBI, sem substituir base válida em falhas."""
from pathlib import Path
import argparse,json,zipfile,urllib.request,hashlib,datetime
import pandas as pd
R=Path(__file__).resolve().parents[1];CACHE=R/'data/cache';CNPJ='01.417.222/0001-77'
URLS={
'dfp2023.zip':'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2023.zip',
'itr2026.zip':'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_2026.zip',
'dirbi.xlsb':'https://www.gov.br/fazenda/pt-br/assuntos/politica-fiscal/atuacao-spe/plataforma-de-desoneracoes-tributarias/arquivos/desoneracoes-dirbi-2024.xlsb/@@download/file?download=1'}
def obter(nome,offline):
 p=CACHE/nome
 if not offline:
  import time,subprocess
  falhas=[];raw=None
  for tentativa in range(3):
   try:
    req=urllib.request.Request(URLS[nome],headers={'User-Agent':'Mozilla/5.0 (coleta de dados publicos)','Accept':'*/*'})
    with urllib.request.urlopen(req,timeout=90) as r:raw=r.read()
    if not zipfile.is_zipfile(__import__('io').BytesIO(raw)):raise ValueError('Arquivo incompleto ou resposta não ZIP')
    break
   except (OSError,ValueError) as exc:
    falhas.append(str(exc));raw=None
    if tentativa<2:time.sleep(2+tentativa)
  if raw is None:
   # Cliente TLS alternativo padrão, com validação de certificado mantida.
   tmp=p.with_suffix('.download')
   try:
    subprocess.run(['curl','--fail','--location','--retry','2','--retry-delay','2','--max-time','90','--user-agent','Mozilla/5.0','--output',str(tmp),URLS[nome]],check=True,capture_output=True)
    raw=tmp.read_bytes()
    if not zipfile.is_zipfile(__import__('io').BytesIO(raw)):raise ValueError('Download alternativo inválido')
   except (OSError,ValueError,subprocess.CalledProcessError) as exc:
    raise RuntimeError(f'Download oficial indisponível: {nome}; tentativas: {falhas}; curl: {exc}') from exc
   finally:tmp.unlink(missing_ok=True)
  tmp=p.with_suffix('.tmp');tmp.write_bytes(raw);tmp.replace(p)
 if not p.exists():raise FileNotFoundError(p)
 return p

def dre(nome,scope,offline):
 p=obter(nome,offline);year='2023' if '2023' in nome else '2026';prefix='dfp' if year=='2023' else 'itr'
 z=zipfile.ZipFile(p)
 with z.open(f'{prefix}_cia_aberta_DRE_{scope}_{year}.csv') as f:df=pd.read_csv(f,sep=';',encoding='latin1',dtype={'CD_CONTA':str,'CNPJ_CIA':str})
 df=df[(df.CNPJ_CIA==CNPJ)&(df.DT_REFER==f'{year}-'+('12-31' if year=='2023' else '09-30'))]
 assert not df.empty
 df=df[df.VERSAO==df.VERSAO.max()]
 assert set(df.ESCALA_MOEDA)=={'MIL'} and set(df.MOEDA)=={'REAL'}
 return df

def valor(df,ano,conta):
 fim=f'{ano}-'+('12-31' if ano in [2022,2023] else '09-30')
 x=df[(df.DT_INI_EXERC==f'{ano}-01-01')&(df.DT_FIM_EXERC==fim)&(df.CD_CONTA==conta)]
 assert len(x)==1,f'Conta ausente/ambígua: {ano} {conta}'
 return float(x.iloc[0].VL_CONTA)/1000

def executar(offline=False):
 CACHE.mkdir(exist_ok=True,parents=True);d=json.loads((R/'data/base_revisada.json').read_text())
 df=dre('itr2026.zip','con',offline);rows=[]
 for year,expected in [(2025,(5636.531,1690.078,464.453,1225.625)),(2026,(5613.532,1295.227,428.676,866.551))]:
  v=(valor(df,year,'3.01'),valor(df,year,'3.07'),-valor(df,year,'3.08'),valor(df,year,'3.09'))
  assert all(abs(a-b)<.00001 for a,b in zip(v,expected)),'Divergência entre ITR/CVM e DRE'
  assert abs(v[1]-v[2]-v[3])<.00001
  f=next(x for x in d['financeiro'] if x['periodo']==f'9M{year}');f.update(lair=v[1],ir=v[2],lucro=v[3],conciliacao='CVM ITR e DRE consolidada p.24; nota 31')
  rows.append(dict(periodo=f'9M{year}',escopo='Consolidado',receita=v[0],lair=v[1],ir=v[2],lucro=v[3],versao=int(df.VERSAO.max())))
 # A DRE da ITR é a prova primária adicional; exige linha exata de corrente/diferido no PDF.
 text=(CACHE/'itr2026.txt').read_text()
 for token in ['1.295.227','88.303','340.373','1.690.078','166.115','298.338']:assert token in text
 assert 88303+340373==428676 and 166115+298338==464453
 hist=dre('dfp2023.zip','ind',offline);historico=[]
 for y in [2022,2023]:
  a={c:valor(hist,y,c) for c in ['3.01','3.07','3.08','3.09']}
  assert abs(a['3.07']+a['3.08']-a['3.09'])<.00001
  historico.append(dict(ano=y,escopo='Controladora',receita=a['3.01'],lair=a['3.07'],ir=-a['3.08'],lucro=a['3.09'],aliquota=-a['3.08']/a['3.07']*100,fonte='cvm2023'))
 p=obter('dirbi.xlsb',offline)
 x=pd.read_excel(p,sheet_name='Base_Dirbi',engine='pyxlsb');x.columns=[c.strip() for c in x.columns]
 def chave(n):
  if isinstance(n,(int,float)) and pd.notna(n):return str(int(n)).zfill(14)
  t=str(n).strip()
  return t.zfill(14) if t.isdigit() else None  # Identificadores textuais truncados/científicos não são inferidos.
 key=x.cnpj.map(chave);target=CNPJ.translate(str.maketrans('','','./-'))
 x=x[(key==target)&(x.ano==2024)].copy();assert len(x)>0,'CNPJ sem registro na DIRBI: não presumir zero'
 x=x.drop_duplicates();keys=['cnpj','uf','id_municipio','cod_programa','nome_tributo','ano']
 assert not x.duplicated(keys).any(),'DIRBI com chave duplicada: revisão necessária'
 assert x.Valor_desoneracao.notna().all() and (x.Valor_desoneracao>=0).all()
 def fix(t):
  try:return str(t).encode('latin1').decode('utf-8')
  except (UnicodeError,ValueError):return str(t)
 registros=[dict(ano=int(row.ano),uf=row.uf,programa=fix(row.nome_programa),tributo=fix(row.nome_tributo).upper().replace('_','/'),valor=float(row.Valor_desoneracao)/1e6) for row in x.itertuples()]
 fontes=[dict(id='cvm2023',nome='CVM — DFP 2023 e comparativo 2022',url=URLS['dfp2023.zip'],localizador='DRE individual, contas 3.01/3.07/3.08/3.09; versão 1',natureza='Real',periodo='2022–2023',escopo='Controladora',unidade='R$ mil na origem; R$ mi no painel'),dict(id='cvmitr',nome='CVM — ITR 3T2026',url=URLS['itr2026.zip'],localizador='DRE consolidada, 01/01–30/09; contas 3.01/3.07/3.08/3.09',natureza='Real',periodo='9M2025–9M2026',escopo='Consolidado',unidade='R$ mil na origem; R$ mi no painel'),dict(id='dirbi',nome='Ministério da Fazenda — DIRBI 2024',url=URLS['dirbi.xlsb'],localizador='Aba Base_Dirbi, chave CNPJ/UF/município/programa/tributo/ano; Dicionário',natureza='Adaptado',periodo='2024',escopo='CNPJ da empresa',unidade='R$ na origem; R$ mi no painel')]
 extra=dict(historico_controladora=historico,dirbi=dict(ano=2024,registros=registros,total=sum(x['valor'] for x in registros),linhas=len(registros),fonte='dirbi'),conciliacao_9m=rows,verificacao='2026-11-27')
 extra['operacional']=[{'periodo': '2024', 'volume': 202525, 'investimentos': 2864.5, 'fonte': 'dfp2025'}, {'periodo': '2025', 'volume': 213001, 'investimentos': 3400.8, 'fonte': 'dfp2025'}, {'periodo': '9M2025', 'volume': 157230, 'investimentos': 2583, 'fonte': 'itr2026'}, {'periodo': '9M2026', 'volume': 157121, 'investimentos': 2043, 'fonte': 'itr2026'}]
 for token in ['202.525','213.001','3.400,8','2.864,5']:assert token in (CACHE/'dfp2025.txt').read_text()
 for token in ['157.230','157.121','2.043','2.583']:assert token in (CACHE/'itr2026.txt').read_text()
 d['complementos']=extra
 for f in fontes:
  d['fontes']=[s for s in d['fontes'] if s['id']!=f['id']]+[f]
 d['limitacoes']=[s for s in d['limitacoes'] if not any(t in s for t in ['Histórico financeiro inicial','ANTT/DIRBI','CVM DFP 2025:'])]
 d['limitacoes']=list(dict.fromkeys(d['limitacoes']+['Histórico 2022–2023 é controladora; não comparar automaticamente com consolidado 2024–2026.','ANTT: downloads CSV/JSON/API e alternativa XLSX sem arquivo válido; contexto por rota não foi presumido.','DIRBI 2024 informa desonerações declaradas; não é caixa recebido nem economia incremental.']))
 from coletar import validar
 validar(d)
 manifest=[dict(arquivo=n,url=u,sha256=hashlib.sha256((CACHE/n).read_bytes()).hexdigest(),coleta=datetime.datetime.now(datetime.timezone.utc).isoformat()) for n,u in URLS.items()]
 for path,obj in [('data/complementos_revisados.json',dict(complementos=extra,fontes=fontes,financeiro_9m=rows)),('data/conciliacao_expandida.json',dict(fontes=manifest,contas_9m=rows,historico=historico,dirbi_registros=len(registros))),('data/base_revisada.json',d),('public/data/painel.json',d)]:
  dest=R/path;tmp=dest.with_suffix('.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2));tmp.replace(dest)
 print(json.dumps(dict(aliquota_9m2026=428676/1295227*100,dirbi=extra['dirbi'],historico=historico),ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--offline',action='store_true');args=p.parse_args();executar(args.offline)
