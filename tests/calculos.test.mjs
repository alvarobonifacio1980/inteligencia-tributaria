import test from 'node:test';import assert from 'node:assert/strict';import {credito,reforma,percentual,capexRegime,fluxoParcelado} from '../src/calculos.mjs';
const p={capital:50,atual:24,proposto:12,taxa:12,custo:.5};
test('Antecipação calcula VP sem reduzir o principal',()=>{const r=credito(p);assert.ok(Math.abs(r.beneficio-(50/1.12-50/1.12**2-.5))<1e-10);assert.equal(r.capital,50)});
test('Prazo igual, taxa zero e custo',()=>{assert.equal(credito({...p,proposto:24}).beneficio,-.5);assert.equal(credito({...p,taxa:0}).beneficio,-.5)});
test('Recusa valores negativos e NaN',()=>{assert.throws(()=>credito({...p,capital:-1}));assert.throws(()=>credito({...p,taxa:NaN}))});
const s={receita:100,custos:60,elegibilidade:100,atual:10,cbs:9,ibs:18,ano:2033,repasse:100,prazo:0,taxa:12};
test('Reforma: zero e integralidade de créditos',()=>{assert.equal(reforma({...s,elegibilidade:0}).creditos,0);assert.equal(reforma(s).creditos,16.2);assert.ok(Math.abs(reforma(s).novo-10.8)<1e-10)});
test('Repasse integral neutraliza diferencial sem prazo; sem repasse afeta caixa',()=>{assert.equal(reforma(s).efeitoCaixa,0);assert.ok(reforma({...s,repasse:0}).efeitoCaixa<0)});
test('Transição e extremos',()=>{assert.equal(reforma({...s,ano:2026}).transicao,10);assert.equal(reforma({...s,ano:2033}).transicao,reforma(s).novo);assert.equal(reforma({...s,receita:0,custos:0}).novo,0);assert.throws(()=>reforma({...s,elegibilidade:101}));assert.equal(percentual(1,0),null)});

test('Transição separa carga federal e estadual em 2027–2033',()=>{const x=reforma({...s,ano:2027,federalAtual:3});assert.equal(x.aliquotaCBS,8.9);assert.equal(x.aliquotaIBS,.1);assert.equal(x.legado,7);assert.ok(Math.abs(x.transicao-(7+9-5.4))<1e-9);assert.equal(reforma({...s,ano:2033}).legado,0)});
test('Crédito excedente não vira recebimento de caixa automático',()=>{const x=reforma({...s,custos:200,repasse:0});assert.equal(x.transicao,0);assert.ok(x.creditosExcedentes>0);assert.equal(x.custoPrazo,0)});

test('CAPEX não duplica suspensão e crédito alternativo',()=>{const p={investimento:100,elegibilidade:100,aliquota:10,creditoSemRegime:100,prazoCredito:0,taxa:12,custo:0};assert.equal(capexRegime(p).beneficioVP,0);assert.equal(capexRegime(p).efeitoPermanente,0);assert.ok(capexRegime({...p,prazoCredito:12}).beneficioVP>0);assert.equal(capexRegime({...p,elegibilidade:0}).suspensao,0)});
test('Fluxo parcelado preserva principal e desconta cada mês',()=>{const x=fluxoParcelado({capital:240,parcelas:240,carencia:0,taxa:0});assert.equal(x.mensal,1);assert.equal(x.vp,240);assert.ok(fluxoParcelado({capital:240,parcelas:240,carencia:0,taxa:12}).vp<240);assert.throws(()=>fluxoParcelado({capital:1,parcelas:0,carencia:0,taxa:0}))});

test('Fixtures independentes de cenários são reproduzidas em JS',async()=>{const {readFile}=await import('node:fs/promises');const cases=JSON.parse(await readFile(new URL('./fixtures_cenarios.json',import.meta.url)));for(const c of cases){const r=reforma(c.entrada);for(const [k,v]of Object.entries(c.esperado))assert.ok(Math.abs(r[k]-v)<1e-9,`${c.nome}: ${k}`)}});
