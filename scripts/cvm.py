"""Conciliação CVM/Pandas por CNPJ, escopo, versão, período e conta."""
from pathlib import Path
import pandas as pd
import urllib.request,zipfile,json,hashlib
R=Path(__file__).resolve().parents[1]
def executar():
 url='https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip'
 with urllib.request.urlopen(url,timeout=90) as r:raw=r.read()
 (R/'data/cache').mkdir(exist_ok=True,parents=True)
 path=R/'data/cache/cvm2025.zip';path.write_bytes(raw)
 z=zipfile.ZipFile(path);frames=[]
 for n in z.namelist():
  if 'DRE_con' in n or 'BPA_con' in n:
   with z.open(n) as f:df=pd.read_csv(f,sep=';',encoding='latin1',dtype={'CD_CVM':str,'CD_CONTA':str})
   df=df[(df.CNPJ_CIA=='01.417.222/0001-77')&(df.ORDEM_EXERC=='ÚLTIMO')]
   if not df.empty:
    df=df[df.VERSAO==df.VERSAO.max()]
    assert (df.ESCALA_MOEDA=='MIL').all() and (df.MOEDA=='REAL').all()
    frames.append(df)
 df=pd.concat(frames);out=[]
 for account,expected in [('3.01',7585058),('3.07',2152768),('3.08',-597705),('1.01.06',266787)]:
  x=df[df.CD_CONTA==account];assert len(x)==1,f'Conta não única {account}'
  row=x.iloc[0];assert abs(row.VL_CONTA-expected)<.01,f'Divergência CVM: {account}'
  out.append(dict(conta=account,descricao=row.DS_CONTA,valor_mil=float(row.VL_CONTA),data=row.DT_REFER,versao=int(row.VERSAO),cnpj=row.CNPJ_CIA,resultado='Conciliado com DFP Empresa Ferroviária'))
 df['DENOM_CIA']='Empresa Ferroviária'  # Designação editorial; CNPJ/contas preservados.
 df.to_csv(R/'data/cvm_empresa_2025.csv',index=False,sep=';',encoding='utf-8')
 (R/'data/conciliacao_cvm.json').write_text(json.dumps(dict(url=url,sha256=hashlib.sha256(raw).hexdigest(),contas=out),ensure_ascii=False,indent=2))
 print('CVM: 4 contas conciliadas com RI, consolidado 2025.')
if __name__=='__main__':executar()
