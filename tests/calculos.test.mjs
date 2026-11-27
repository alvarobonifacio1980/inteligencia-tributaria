import test from 'node:test';import assert from 'node:assert/strict';import {credito,reforma,percentual} from '../src/calculos.mjs';
const p={capital:50,atual:24,proposto:12,taxa:12,custo:.5};
test('Antecipação calcula VP sem reduzir o principal',()=>{const r=credito(p);assert.ok(Math.abs(r.beneficio-(50/1.12-50/1.12**2-.5))<1e-10);assert.equal(r.capital,50)});
test('Prazo igual, taxa zero e custo',()=>{assert.equal(credito({...p,proposto:24}).beneficio,-.5);assert.equal(credito({...p,taxa:0}).beneficio,-.5)});
test('Recusa valores negativos e NaN',()=>{assert.throws(()=>credito({...p,capital:-1}));assert.throws(()=>credito({...p,taxa:NaN}))});
const s={receita:100,custos:60,elegibilidade:100,atual:10,cbs:9,ibs:18,ano:2033,repasse:100,prazo:0,taxa:12};
test('Reforma: zero e integralidade de créditos',()=>{assert.equal(reforma({...s,elegibilidade:0}).creditos,0);assert.equal(reforma(s).creditos,16.2);assert.ok(Math.abs(reforma(s).novo-10.8)<1e-10)});
test('Repasse integral neutraliza diferencial sem prazo; sem repasse afeta caixa',()=>{assert.equal(reforma(s).efeitoCaixa,0);assert.ok(reforma({...s,repasse:0}).efeitoCaixa<0)});
test('Transição e extremos',()=>{assert.equal(reforma({...s,ano:2026}).transicao,10);assert.equal(reforma({...s,ano:2033}).transicao,reforma(s).novo);assert.equal(reforma({...s,receita:0,custos:0}).novo,0);assert.throws(()=>reforma({...s,elegibilidade:101}));assert.equal(percentual(1,0),null)});
