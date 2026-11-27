"""Extrator restrito aos layouts verificados; falha fechada diante de mudança."""
from pathlib import Path
import re,json,csv
R=Path(__file__).resolve().parents[1]
def numeros(linha):
 return [int(x.strip('()').replace('.','')) for x in linha.split() if re.fullmatch(r'\(?\d{1,3}(?:\.\d{3})*\)?',x)]
def linha(texto,rotulo,n):
 linhas=[l for l in texto.splitlines() if rotulo in l and len(numeros(l))==n]
 if len(linhas)!=1:raise ValueError(f'Layout ambíguo/alterado: {rotulo} ({len(linhas)})')
 return numeros(linhas[0])
def executar():
 d=json.loads((R/'data/base_revisada.json').read_text());a=(R/'data/cache/dfp2025.txt').read_text();b=(R/'data/cache/itr2026.txt').read_text()
 financeiro=[]
 for texto,cols,periodos,idx in [(a,2,['2024','2025'],[1,0]),(b,4,['9M2025','9M2026'],[3,1])]:
  bruta=linha(texto,'Receita bruta de serviços',cols);imp=linha(texto,'Impostos sobre serviços',cols)
  for p,i in zip(periodos,idx):
   atual=next(x for x in d['financeiro'] if x['periodo']==p)
   extraido=dict(periodo=p,bruta=bruta[i]/1000,impostos=imp[i]/1000,liquida=(bruta[i]-imp[i])/1000)
   for k in ['bruta','impostos','liquida']:assert abs(atual[k]-extraido[k])<1e-7,f'Divergência {p} {k}'
   financeiro.append(extraido)
 creditos=[]
 for texto,nota,periodos,indices in [(a,'10.   Tributos a recuperar',['31/12/2024','31/12/2025'],[3,2]),(b,'9.   Tributos a recuperar',['30/09/2026'],[2])]:
  t=texto.split(nota,1)[1].split('Composição dos créditos de ICMS',1)[0]
  pis=linha(t,'a recuperar',4);irrf=linha(t,'Imposto de renda retido',4);outros=linha(t,'Outros',4)
  # Linha de ICMS é quebrada no PDF; localizar marcador de nota (b).
  icms=linha(t,'(b)',4)
  for p,i in zip(periodos,indices):
   extraido=dict(data=p,pis=pis[i]/1000,irrf=irrf[i]/1000,outros=outros[i]/1000,icms=icms[i]/1000)
   atual=next(x for x in d['creditos'] if x['data']==p)
   for k in ['pis','irrf','outros','icms']:assert abs(atual[k]-extraido[k])<1e-7,f'Divergência {p} {k}'
   creditos.append(extraido)
 (R/'data/extracao_validada.json').write_text(json.dumps(dict(financeiro=financeiro,creditos=creditos),ensure_ascii=False,indent=2))
 print('Extração estrutural: 4 períodos de receita e 3 datas de créditos conciliados.')
if __name__=='__main__':executar()
