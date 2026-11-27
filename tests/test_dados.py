import sys,json,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from coletar import validar
class Dados(unittest.TestCase):
 def setUp(self):self.d=json.loads((Path(__file__).resolve().parents[1]/'data/base_revisada.json').read_text())
 def test_conciliacoes(self):validar(self.d)
 def test_escopo_e_despesa(self):
  f=self.d['financeiro'][1];self.assertAlmostEqual(f['ir']/f['lair']*100,27.7644896,places=4)
 def test_provisao_nao_somada(self):
  c=self.d['contingencias'];self.assertLess(c['provisao'],c['exposicao']);self.assertEqual(c['processos_total']-c['acoes_recuperacao'],c['processos_risco'])
 def test_detecta_base_invalida(self):
  self.d['financeiro'][0]['liquida']+=1
  with self.assertRaises(AssertionError):validar(self.d)
if __name__=='__main__':unittest.main()
