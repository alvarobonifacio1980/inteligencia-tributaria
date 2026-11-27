"""Fixtures compartilhadas, verificadas por fórmula independente em Python."""
import unittest,json
from pathlib import Path
class Cenarios(unittest.TestCase):
 def test_transicao(self):
  for c in json.loads((Path(__file__).parent/'fixtures_cenarios.json').read_text()):
   p=c['entrada'];fracao=0 if p['ano']<2029 else 1 if p['ano']==2033 else (p['ano']-2028)/10
   cbs=p['cbs']-.1 if p['ano']<=2028 else p['cbs'];ibs=.1 if p['ano']<=2028 else p['ibs']*fracao
   legado=p['receita']*(p['atual']-p['federalAtual'])/100*(1-fracao)
   valor=legado+(p['receita']-p['custos']*p['elegibilidade']/100)*(cbs+ibs)/100
   self.assertAlmostEqual(valor,c['esperado']['transicao'])
