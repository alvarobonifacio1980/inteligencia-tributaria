"""Coleta auditável: documentos oficiais, extração e validação antes de publicação."""
from pathlib import Path
import urllib.request, subprocess, hashlib, json, re, datetime, argparse
ROOT=Path(__file__).resolve().parents[1]
FONTES={
 'dfp2025':('https://api.mziq.com/mzfilemanager/v2/d/e14f1680-635b-4328-8a06-b799b1574b43/acbef322-8f85-850f-ae21-8d531a3467b4?origin=2','DFP 2025',{'receita_bruta':8054851,'tributos_servicos':469793,'receita_liquida':7585058,'lucro_antes_ir':2152768,'ir_csll':597705}),
 'itr2026':('https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/ed0c4c1c-5cc3-4a74-ac98-e657a4cd7bbf','ITR 3T2026',{'creditos':553764,'icms':277596,'pis_cofins':129005,'irrf':146391,'outros':772})}
def br(n):return f'{n:,}'.replace(',','.')
def coletar():
 cache=ROOT/'data/cache';cache.mkdir(parents=True,exist_ok=True);manifest=[]
 for key,(url,nome,checks) in FONTES.items():
  pdf=cache/f'{key}.pdf'; tmp=cache/f'{key}.tmp'
  try:
   with urllib.request.urlopen(url,timeout=90) as r: raw=r.read()
   if not raw.startswith(b'%PDF'):raise ValueError('Resposta não é PDF')
   tmp.write_bytes(raw);subprocess.run(['pdftotext','-layout',str(tmp),str(cache/f'{key}.txt')],check=True)
   texto=(cache/f'{key}.txt').read_text()
   for campo,v in checks.items():
    if br(v) not in texto:raise ValueError(f'Valor esperado ausente: {campo}; revisar fonte antes de atualizar')
   tmp.replace(pdf)
   manifest.append(dict(id=key,documento=nome,url=url,sha256=hashlib.sha256(raw).hexdigest(),coleta=datetime.datetime.now(datetime.timezone.utc).isoformat(),validacao='Âncoras numéricas presentes; extração revisada por nota e escopo',campos=checks))
  finally:
   tmp.unlink(missing_ok=True)
 out=ROOT/'data/coletas.json';out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
 return manifest
def validar(d):
 for f in d['financeiro']:
  assert abs(f['bruta']-f['impostos']-f['liquida'])<.002,'Receita não concilia'
 for c in d['creditos']:
  assert abs(sum(c[k] for k in ['icms','pis','irrf','outros'])-c['total'])<.002,'Composição não concilia'
  assert abs(c['circulante']+c['nao_circulante']-c['total'])<.002,'Classificação não concilia'
 for f in d['financeiro']:
  if 'lucro' in f:assert abs(f['lair']-f['ir']-f['lucro'])<.002,'DRE não concilia'
 if 'complementos' in d:
  b=d['complementos']['dirbi'];assert abs(sum(x['valor'] for x in b['registros'])-b['total'])<1e-8,'DIRBI não concilia'
 assert d['reconciliacao']['nominal']+sum(d['reconciliacao']['ajustes'].values())==597705
 if 'v2' in d:
  v=d['v2']
  for x in v['dva']:assert abs(x['federal']+x['estadual']+x['municipal']-x['total'])<1e-6,'DVA não concilia'
  for year,n in v['totais_dip'].items():assert sum(x['valor_reais'] for x in v['dip'] if x['ano']==int(year) and x['valor_reais'] is not None)==n,'DIP não concilia'
  assert sum(x['valor_reais'] for x in v['dir'])==v['total_dir'],'DIR não concilia'
  for x in v['dfc']:assert x['original_mil']<0 and abs(x['valor']+x['original_mil']/1000)<1e-9,'DFC sinal inválido'
  for x in v['riscos']:assert abs(x['possivel']+x['provavel']-x['total'])<1e-6,'Riscos não conciliam'
  for x in v['reconciliacao_9m']:assert abs(x['nominal']+sum(x['ajustes'].values())-x['efetivo'])<1e-6,'IR/CS 9M não concilia'

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--offline',action='store_true');a=p.parse_args()
 if not a.offline:
  coletar()
  from extrair import executar
  executar()
 d=json.loads((ROOT/'data/base_revisada.json').read_text());validar(d)
 # Apenas após validação integral, substitui a base de publicação.
 dest=ROOT/'public/data/painel.json';temp=dest.with_suffix('.tmp');temp.write_text(json.dumps(d,ensure_ascii=False,indent=2));temp.replace(dest)
 print('Base validada e publicada; valores em R$ milhões; consolidado.')
