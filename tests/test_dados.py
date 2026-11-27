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
 def test_aliquota_9m_conciliada(self):
  f=next(x for x in self.d['financeiro'] if x['periodo']=='9M2026')
  self.assertAlmostEqual(f['lair'],1295.227);self.assertAlmostEqual(f['ir'],428.676)
  self.assertAlmostEqual(f['ir']/f['lair']*100,33.0965923348)
 def test_historico_segregado(self):
  self.assertTrue(all(x['escopo']=='Controladora' for x in self.d['complementos']['historico_controladora']))
 def test_dirbi(self):
  b=self.d['complementos']['dirbi'];self.assertEqual(b['linhas'],12);self.assertAlmostEqual(b['total'],140.19918494)
  self.assertEqual(len(b['registros']),12)
if __name__=='__main__':unittest.main()
