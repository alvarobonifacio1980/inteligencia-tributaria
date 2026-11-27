export function credito({capital,atual,proposto,taxa,custo}) {
 if (![capital,atual,proposto,taxa,custo].every(Number.isFinite)||![atual,proposto].every(Number.isInteger)||capital<0||atual<0||proposto<0||taxa<0||custo<0) throw Error('Premissas inválidas');
 const vpAtual=capital/(1+taxa/100)**(atual/12),vpProposto=capital/(1+taxa/100)**(proposto/12);
 return {vpAtual,vpProposto,beneficio:vpProposto-vpAtual-custo,capital};
}
// Bases econômicas por fora. Cenário geral, sem regimes especiais ou apuração de operação real.
export function reforma({receita,custos,elegibilidade,atual,federalAtual=atual*.375,cbs,ibs,ano,repasse,prazo,taxa,crescimento=0,capex=0,elegibilidadeCapex=0}){
 const ns=[receita,custos,elegibilidade,atual,federalAtual,cbs,ibs,ano,repasse,prazo,taxa,crescimento,capex,elegibilidadeCapex];
 if(!ns.every(Number.isFinite)||!Number.isInteger(ano)||ano<2026||ano>2033||receita<0||custos<0||capex<0||prazo<0||taxa<0||crescimento< -100||federalAtual<0||federalAtual>atual||[elegibilidade,repasse,elegibilidadeCapex,atual,cbs,ibs].some(v=>v<0||v>100))throw Error('Premissas inválidas');
 const baseReceita=receita*(1+crescimento/100),baseCustos=custos*(1+crescimento/100);
 const fracao=ano<2029?0:ano===2033?1:(ano-2028)/10;
 const aliquotaCBS=ano===2026?0:ano<=2028?Math.max(0,cbs-.1):cbs;
 const aliquotaIBS=ano===2026?0:ano<=2028?.1:ibs*fracao;
 const base=baseReceita*atual/100;
 const legado=ano===2026?base:baseReceita*(atual-federalAtual)/100*(1-fracao);
 const baseCredito=baseCustos*elegibilidade/100+capex*elegibilidadeCapex/100;
 const debito=baseReceita*(aliquotaCBS+aliquotaIBS)/100,creditos=baseCredito*(aliquotaCBS+aliquotaIBS)/100;
 const saldo=debito-creditos,creditosExcedentes=Math.max(-saldo,0),utilizados=Math.min(debito,creditos);
 const transicao=legado+Math.max(saldo,0);
 const novo=(baseReceita-baseCredito)*(cbs+ibs)/100;
 const diferenca=transicao-base,repasseValor=diferenca*repasse/100;
 const custoPrazo=utilizados*(1-1/(1+taxa/100)**(prazo/12));
 return {debito,creditos,novo,base,transicao,diferenca,repasseValor,efeitoCaixa:repasseValor-diferenca-custoPrazo,custoPrazo,fracao,legado,aliquotaCBS,aliquotaIBS,creditosExcedentes,saldo,baseReceita,baseCustos};
}
export function capexRegime({investimento,elegibilidade,aliquota,creditoSemRegime,prazoCredito,taxa,custo}){
 if(![investimento,elegibilidade,aliquota,creditoSemRegime,prazoCredito,taxa,custo].every(Number.isFinite)||[investimento,prazoCredito,taxa,custo].some(v=>v<0)||[elegibilidade,aliquota,creditoSemRegime].some(v=>v<0||v>100))throw Error('Premissas inválidas');
 const suspensao=investimento*elegibilidade/100*aliquota/100;
 const creditoAlternativo=suspensao*creditoSemRegime/100;
 const vpCredito=creditoAlternativo/(1+taxa/100)**(prazoCredito/12);
 return {suspensao,creditoAlternativo,vpCredito,caixaInicial:suspensao-custo,efeitoPermanente:suspensao-creditoAlternativo,beneficioVP:suspensao-vpCredito-custo};
}
export function fluxoParcelado({capital,parcelas,carencia,taxa}){
 if(![capital,parcelas,carencia,taxa].every(Number.isFinite)||capital<0||!Number.isInteger(parcelas)||parcelas<1||parcelas>360||carencia<0||taxa<0)throw Error('Premissas inválidas');
 const mensal=capital/parcelas,fluxos=Array.from({length:parcelas},(_,i)=>({mes:carencia+i+1,valor:mensal,vp:mensal/(1+taxa/100)**((carencia+i+1)/12)}));
 return {mensal,vp:fluxos.reduce((a,f)=>a+f.vp,0),fluxos};
}
export const percentual=(a,b)=>b>0?a/b*100:null;

// Modelos V2.1 independentes; CAPEX não alimenta automaticamente a reforma agregada.
export function capexPrazo({investimento,fracaoBase,aliquota,recuperacao,prazo,proposto,taxa,custo}){
 const ns=[investimento,fracaoBase,aliquota,recuperacao,prazo,proposto,taxa,custo];
 if(!ns.every(Number.isFinite)||[investimento,prazo,proposto,taxa,custo].some(v=>v<0)||![prazo,proposto].every(Number.isInteger)||[fracaoBase,aliquota,recuperacao].some(v=>v<0||v>100))throw Error('Premissas inválidas');
 const base=investimento*fracaoBase/100,tributo=base*aliquota/100,recuperavel=tributo*recuperacao/100,vp=recuperavel/(1+taxa/100)**(prazo/12),vpProposto=recuperavel/(1+taxa/100)**(proposto/12);
 return {base,tributo,recuperavel,vp,vpProposto,custoPrazo:recuperavel-vp,naoRecuperavel:tributo-recuperavel,bruto:vpProposto-vp,beneficio:vpProposto-vp-custo};
}
export function contrato({base,referencia,novo,repasse}){
 if(![base,referencia,novo,repasse].every(Number.isFinite)||base<=0||referencia<0||novo<0||repasse<0||repasse>100)throw Error('Premissas inválidas');
 const diferenca=novo-referencia,comercial=diferenca*repasse/100,residual=diferenca-comercial;
 return {diferenca,comercial,residual,percentual:residual/base*100};
}
export function sensibilidadeCBS(r){return [-2,0,2].map(delta=>{const cbs=Math.max(0,Math.min(100,r.cbs+delta));return {delta,cbs,...reforma({...r,cbs})}})}
