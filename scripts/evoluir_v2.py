"""Extrai e concilia as diferenças V2.1; publicação só após validação completa."""
from pathlib import Path
import json,re,zipfile,hashlib,datetime,argparse,urllib.request,subprocess
import pandas as pd
R=Path(__file__).resolve().parents[1];C=R/'data/cache';CNPJ='01.417.222/0001-77'
URLS={'dip2027.pdf':'https://www.mrs.com.br/wp-content/uploads/2026/11/DIP-2027-2029.pdf','dir2025.pdf':'https://www.mrs.com.br/wp-content/uploads/2026/11/DIR-2025.pdf','apresentacao3t26.pdf':'https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/b562dfd9-524d-47fc-91a2-ef7558f6dbda','tarifas2026.xlsx':'https://www.mrs.com.br/wp-content/uploads/2026/07/TARIFAS-DE-REFERENCIA-2026-29.07.2026-1.xlsx','simulador2026.xlsx':'https://www.mrs.com.br/wp-content/uploads/2026/07/Simulador-Tarifario-2026-2027.xlsx'}
def numero(s):return int(s.replace('.',''))
def quadro(zname,tipo):
 z=zipfile.ZipFile(C/zname);name=next(n for n in z.namelist() if f'{tipo}_con' in n)
 df=pd.read_csv(z.open(name),sep=';',encoding='latin1',dtype={'CD_CONTA':str});df=df[(df.CNPJ_CIA==CNPJ)];df=df[df.DT_REFER==df.DT_REFER.max()];df=df[df.VERSAO==df.VERSAO.max()]
 assert set(df.MOEDA)=={'REAL'} and set(df.ESCALA_MOEDA)=={'MIL'}
 return df

def valor(df,year,conta):
 x=df[(df.CD_CONTA==conta)&(df.DT_INI_EXERC==f'{year}-01-01')&df.DT_FIM_EXERC.str.startswith(str(year))]
 assert len(x)==1,(year,conta,len(x));return float(x.iloc[0].VL_CONTA)
def executar(offline=True,permitir_snapshot=False):
 if not offline:
  tentativas=[]
  for n,u in URLS.items():
   try:
    with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as r:b=r.read()
    assert b.startswith(b'%PDF') if n.endswith('.pdf') else zipfile.is_zipfile(__import__('io').BytesIO(b))
    tmp=(C/n).with_suffix('.tmp');tmp.write_bytes(b);tmp.replace(C/n)
    if n.endswith('.pdf'):subprocess.run(['pdftotext','-layout',str(C/n),str(C/n.replace('.pdf','.txt'))],check=True)
    tentativas.append(dict(arquivo=n,status='obtido',sha256=hashlib.sha256(b).hexdigest()))
   except OSError as exc:tentativas.append(dict(arquivo=n,status='indisponivel',motivo=str(exc)))
  falhas=[x for x in tentativas if x['status']=='indisponivel']
  if falhas:
   if not permitir_snapshot:raise RuntimeError(falhas)
   from coletar import validar
   snapshot=json.loads((R/'data/base_revisada.json').read_text());validar(snapshot)
   (R/'data/coleta_v2_status.json').write_text(json.dumps(dict(reutilizada=True,tentativas=tentativas,motivo='Fonte complementar indisponível; snapshot V2 revisado preservado. Sem afirmar coleta nova.',revisao_original=snapshot['v2']['revisao']),ensure_ascii=False,indent=2))
   print('::warning::Fonte V2 complementar indisponível; snapshot revisado preservado. Ver coleta_v2_status.json.')
   return
 d=json.loads((R/'data/base_revisada.json').read_text());dip=[];dire=[]
 for line in (C/'dip2027.txt').read_text().splitlines():
  m=re.match(r'\s*([1-5])\s+(.+?)\s+R\$\s+([\d.]+|-)\s+R\$\s+([\d.]+|-)\s+R\$\s+([\d.]+|-)',line)
  if m:
   for year,n in zip([2027,2028,2029],m.groups()[2:]):dip.append(dict(codigo=int(m[1]),classe=m[2].strip(),ano=year,valor_reais=numero(n) if n!='-' else None,original=n,natureza='Real — previsão oficial',fonte='dip',localizador='DIP p.1',escopo='Regulatório'))
 assert len(dip)==15
 totals={str(y):sum(r['valor_reais'] or 0 for r in dip if r['ano']==y) for y in [2027,2028,2029]}
 assert list(totals.values())==[2299407714,2849161485,2560955015]
 for line in (C/'dir2025.txt').read_text().splitlines():
  m=re.match(r'\s*(\d+)\s+(.+?)\s+([\d.]+)\s*$',line)
  if m and 1<=int(m[1])<=11:dire.append(dict(codigo=int(m[1]),classe=m[2].strip(),ano=2025,valor_reais=numero(m[3]),original=m[3],natureza='Real',fonte='dir',localizador='DIR p.1',escopo='Regulatório'))
 assert len(dire)==11 and sum(x['valor_reais'] for x in dire)==3349592317
 dva=[];dfc=[]
 for zname,anos,prefix,fonte,pagina in [('cvm2025.zip',[2024,2025],'','dfp2025','DVA p.46'),('itr2026.zip',[2025,2026],'9M','itr2026','DVA p.33')]:
  v=quadro(zname,'DVA')
  for y in anos:
   row=dict(periodo=f'{prefix}{y}',federal=valor(v,y,'7.08.02.01')/1000,estadual=valor(v,y,'7.08.02.02')/1000,municipal=valor(v,y,'7.08.02.03')/1000,total=valor(v,y,'7.08.02')/1000,fonte=fonte,localizador=pagina,escopo='Consolidado',unidade='R$ mi',natureza='Real')
   assert abs(row['total']-sum(row[k] for k in ['federal','estadual','municipal']))<1e-6;dva.append(row)
 v=quadro('itr2026.zip','DFC_MI')
 rows=v[v.DS_CONTA.str.contains('Pagamento de Tributos Sobre o Lucro',case=False)]
 assert rows.CD_CONTA.nunique()==1
 conta=rows.CD_CONTA.iloc[0]
 for y,e in [(2025,-194592),(2026,-19087)]:
  n=valor(v,y,conta);assert n==e
  dfc.append(dict(periodo=f'9M{y}',original_mil=n,valor=-n/1000,unidade='R$ mi; saída em magnitude positiva',fonte='itr2026',localizador='DFC consolidada p.30; CVM '+conta,natureza='Adaptado',escopo='Consolidado'))
 for filename,tokens in [('dfp2025.txt',['1.000.469','970.129','974.874','72.468','93.616','935.621','151.214','643.211','142.762']),('itr2026.txt',['(19.087)','(194.592)','685.475','(17.798)','1.045.049','150.039'])]:
  text=(C/filename).read_text()
  assert all(t in text for t in tokens)
 riscos=[dict(data='31/12/2024',possivel=643.211,provavel=142.762,total=785.973,fonte='dfp2025',localizador='Nota 25(c), p.109'),dict(data='31/12/2025',possivel=935.621,provavel=151.214,total=1086.835,processos=194,recuperacao=26,risco=168,provaveis=9,fonte='dfp2025',localizador='Nota 25(c), p.109'),dict(data='30/09/2026',possivel=(1045049-150039)/1000,provavel=150.039,total=1045.049,processos=171,recuperacao=22,risco=149,provaveis=16,fonte='itr2026',localizador='Nota 23.1(c), p.80')]
 assert all(abs(x['possivel']+x['provavel']-x['total'])<1e-6 for x in riscos)
 temas=[dict(tema='Créditos ICMS RJ/SP',valor=239.015),dict(tema='PIS/Cofins: arrendamento, tráfego e passagem',valor=209.257),dict(tema='IPTU sobre imóveis operacionais',valor=142.419),dict(tema='ICMS: escrituração CIAP',valor=43.680),dict(tema='PIS/Cofins: subvenção',valor=22.917),dict(tema='PIS/Cofins: tráfego mútuo',valor=20.086)]
 # São temas das perdas possíveis de 2025, não categorias exaustivas nem soma ao provisionado.
 import openpyxl
 w=openpyxl.load_workbook(C/'simulador2026.xlsx',data_only=False);v=openpyxl.load_workbook(C/'simulador2026.xlsx',data_only=True)
 sh=w.worksheets[0];cache=v.worksheets[0]
 assert sh['E16'].value=='=ROUND(E14+(E13*D15),2)' and abs(round(cache['E14'].value+cache['E13'].value*cache['D15'].value,2)-cache['E16'].value)<1e-7
 tarifas=dict(fixa=cache['E14'].value,variavel=cache['E13'].value,distancia_exemplo=cache['D15'].value,teto_exemplo=cache['E16'].value,produto='Demais Produtos',unidade='R$/t',icms_incluido=False,vigencia_cache=cache['B7'].value.isoformat()[:10],ato=cache['E7'].value,fonte='tarifario',localizador='Primeira aba, E13:E16; PRODUTOS linha 31',formula='Arredondar(fixa + variável × distância, 2)',limite='Valor máximo homologado; não é preço efetivo. Data da célula é mantida como metadado, sem presumir início/fim além do documento.')
 inspection=[]
 for n in ['tarifas2026.xlsx','simulador2026.xlsx']:
  wb=openpyxl.load_workbook(C/n,data_only=False);inspection.append(dict(arquivo=n,abas=[dict(nome_generico=f'Aba {i+1}',linhas=s.max_row,colunas=s.max_column,protegida=s.protection.sheet,formulas=sum(c.data_type=='f' for row in s for c in row)) for i,s in enumerate(wb)],vinculos_externos=len(wb._external_links),nomes=list(wb.defined_names),macros=False))
 fontes=[dict(id='dip',nome='Dados públicos da empresa — DIP 2027–2029',url=URLS['dip2027.pdf'],localizador='p.1, classes e nota Outros',periodo='2027–2029',unidade='R$ originais',escopo='Regulatório',natureza='Real — previsão oficial'),dict(id='dir',nome='Dados públicos da empresa — DIR 2025',url=URLS['dir2025.pdf'],localizador='p.1, classes e notas',periodo='2025',unidade='R$ originais',escopo='Regulatório',natureza='Real'),dict(id='apresentacao',nome='Dados públicos da empresa — apresentação 3T2026',url=URLS['apresentacao3t26.pdf'],localizador='p.6,11,13,17',periodo='3T2026/9M2026',escopo='Gerencial',natureza='Real'),dict(id='tarifario',nome='Dados públicos da empresa — referência tarifária',url=URLS['simulador2026.xlsx'],localizador='Primeira aba e PRODUTOS',periodo='Arquivo 2026–2027',unidade='R$/t e R$/t.km',escopo='Teto regulatório',natureza='Real')]
 extra=dict(dva=dva,dfc=dfc,dip=dip,dir=dire,totais_dip=totals,total_dir=3349592317,riscos=riscos,temas_risco_2025=temas,compensacoes=[dict(ano=2024,valor=93.616),dict(ano=2025,valor=72.468)],compensacao_fonte='dfp2025',compensacao_localizador='Nota 10(a), p.63; exclusão ICMS de PIS/Cofins',tarifas=tarifas,inspecao_planilhas=inspection,capex_gerencial=[dict(periodo='9M2025',crescimento=1228,recorrente=1355,total=2583),dict(periodo='9M2026',crescimento=1248,recorrente=795,total=2043)],revisao='2026-11-27')
 extra['custos_referencia']={'periodo':'9M2026','total':3523.729,'grupos':[{'nome':'Depreciação e amortização','valor':955.593,'avaliacao':'Sem crédito presumido neste modelo'},{'nome':'Mão de obra e encargos','valor':856.768,'avaliacao':'Sem crédito presumido neste modelo'},{'nome':'Combustíveis/lubrificantes','valor':765.419,'avaliacao':'Regime e documento a validar'},{'nome':'Serviços de terceiros','valor':411.064,'avaliacao':'Elegibilidade a validar'},{'nome':'Insumos/outros materiais','valor':227.367,'avaliacao':'Elegibilidade a validar'},{'nome':'Partilhas de fretes e acessórios','valor':211.359,'avaliacao':'Operação a validar'},{'nome':'Concessão, aluguel e outros','valor':96.159,'avaliacao':'Indeterminado; não presumir crédito'}],'fonte':'itr2026','localizador':'Nota 28, p.86, consolidado'}
 assert abs(sum(x['valor'] for x in extra['custos_referencia']['grupos'])-3523.729)<1e-6
 extra['reconciliacao_9m']=[{'periodo':'9M2025','nominal':574.627,'ajustes':{'Incentivos fiscais':-20.569,'Exclusão ICMS base IR/CS':-86.501,'PIS/Cofins base ICMS':-.814,'Estoque':.723,'Doações':2.345,'Outros':-5.358},'efetivo':464.453},{'periodo':'9M2026','nominal':440.377,'ajustes':{'Exercícios anteriores':-6.367,'Incentivos fiscais':-15.158,'Estoque':.055,'Doações':1.765,'Outros':8.004},'efetivo':428.676}]
 for row in extra['reconciliacao_9m']:assert abs(row['nominal']+sum(row['ajustes'].values())-row['efetivo'])<1e-6
 extra['reidi_historico']={'ano':2023,'investimento':8732.17792182,'suspensao':807.72645777,'ato':'Portaria MT 779/2023 — Fase II','fonte':'reidi'}
 d['v2']=extra;d['versao']='2.1.1';d['revisao']='2026-11-27';d['fontes']=[s for s in d['fontes'] if s['id'] not in [f['id'] for f in fontes]]+fontes
 manifest=[dict(arquivo=n,url=u,bytes=(C/n).stat().st_size,sha256=hashlib.sha256((C/n).read_bytes()).hexdigest()) for n,u in URLS.items()]
 from coletar import validar
 validar(d)
 for dest,obj in [('data/base_revisada.json',d),('public/data/painel.json',d),('data/conciliacao_v2.json',dict(versao='2.1.1',fontes=manifest,dva=dva,dfc=dfc,totais_dip=totals,total_dir=extra['total_dir'],planilhas=inspection,revisao=extra['revisao']))]:
  p=R/dest;tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2));tmp.replace(p)
 (R/'data/coleta_v2_status.json').write_text(json.dumps(dict(reutilizada=False,modo='cache validado' if offline else 'online',revisao=extra['revisao']),ensure_ascii=False,indent=2))
 print('V2 conciliada: DVA, DFC, DIR/DIP, compensações, riscos e planilhas tarifárias.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');p.add_argument('--permitir-snapshot',action='store_true');args=p.parse_args();executar(not args.online,args.permitir_snapshot)
