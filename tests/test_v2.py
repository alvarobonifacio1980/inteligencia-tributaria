import unittest,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class V2(unittest.TestCase):
 def setUp(self):self.d=json.loads((R/'data/base_revisada.json').read_text())['v2']
 def test_dir_dip_inteiros_e_tracos(self):
  d=self.d;self.assertEqual(sum(x['valor_reais'] for x in d['dir']),3349592317)
  self.assertEqual(sum(d['totais_dip'].values()),7709524214)
  for y,n in d['totais_dip'].items():self.assertEqual(sum(x['valor_reais'] or 0 for x in d['dip'] if x['ano']==int(y)),n)
  self.assertEqual([x['valor_reais'] for x in d['dip'] if x['classe']=='Meio Ambiente'],[None,None,None]);self.assertEqual(next(x for x in d['dir'] if x['classe']=='Meio ambiente')['valor_reais'],0)
 def test_dva_somas_e_sinal(self):
  for x in self.d['dva']:self.assertAlmostEqual(sum(x[k] for k in ['federal','estadual','municipal']),x['total'])
  self.assertLess(next(x for x in self.d['dva'] if x['periodo']=='9M2026')['estadual'],0)
 def test_dfc_nao_confunde_sinal_despesa(self):
  a,b=self.d['dfc'];self.assertEqual([a['original_mil'],b['original_mil']],[-194592,-19087]);self.assertAlmostEqual(a['valor']-b['valor'],175.505)
  for x in [a,b]:self.assertEqual(x['valor'],-x['original_mil']/1000)
 def test_riscos_sem_dupla_contagem(self):
  for x in self.d['riscos']:self.assertAlmostEqual(x['total'],x['possivel']+x['provavel'])
  self.assertEqual(self.d['riscos'][-1]['risco']+self.d['riscos'][-1]['recuperacao'],self.d['riscos'][-1]['processos'])
 def test_reconciliacoes_acumuladas(self):
  for x in self.d['reconciliacao_9m']:self.assertAlmostEqual(x['nominal']+sum(x['ajustes'].values()),x['efetivo'])
 def test_fixtures_independentes(self):
  f=json.loads((R/'tests/fixtures_v2.json').read_text());p=f['capex']['entrada'];b=p['investimento']*p['fracaoBase']/100;t=b*p['aliquota']/100;r=t*p['recuperacao']/100;vp=r/(1+p['taxa']/100)**(p['prazo']/12)
  self.assertAlmostEqual(vp,f['capex']['vp'])
  for c in f['contratos']:p=c['entrada'];self.assertAlmostEqual((p['novo']-p['referencia'])*(1-p['repasse']/100),c['residual'])
 def test_tarifa_cache_e_escopo(self):
  x=self.d['tarifas'];self.assertFalse(x['icms_incluido']);self.assertEqual(round(x['fixa']+x['variavel']*x['distancia_exemplo'],2),x['teto_exemplo'])
  self.assertTrue(all(x['vinculos_externos']==0 and not x['macros'] for x in self.d['inspecao_planilhas']))
