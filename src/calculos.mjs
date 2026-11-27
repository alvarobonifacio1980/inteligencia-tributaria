export function credito({capital,atual,proposto,taxa,custo}) {
 if (![capital,atual,proposto,taxa,custo].every(Number.isFinite)||capital<0||atual<0||proposto<0||taxa<0||custo<0) throw Error('Premissas inválidas');
 const vpAtual=capital/(1+taxa/100)**(atual/12),vpProposto=capital/(1+taxa/100)**(proposto/12);
 return {vpAtual,vpProposto,beneficio:vpProposto-vpAtual-custo,capital};
}
// Bases econômicas líquidas de tributos. Hipóteses de débitos/créditos integralmente realizáveis.
export function reforma({receita,custos,elegibilidade,atual,cbs,ibs,ano,repasse,prazo,taxa}){
 if (![receita,custos,elegibilidade,atual,cbs,ibs,ano,repasse,prazo,taxa].every(Number.isFinite)||receita<0||custos<0||elegibilidade<0||elegibilidade>100||repasse<0||repasse>100||prazo<0||taxa<0||[atual,cbs,ibs].some(v=>v<0||v>100)||ano<2026||ano>2033)throw Error('Premissas inválidas');
 const fracao=ano<2029?0:ano===2033?1:(ano-2028)/10;
 // Sensibilidade de regime pleno ponderada: o atual é taxa líquida hipotética, não a dedução bruta da DRE.
 const debito=receita*(cbs+ibs)/100,creditos=custos*elegibilidade/100*(cbs+ibs)/100;
 const novo=debito-creditos,base=receita*atual/100;
 const peso=ano===2033?1:ano<2027?0:((cbs+ibs*fracao)/(cbs+ibs||1));
 const transicao=base*(1-peso)+novo*peso;
 const diferenca=transicao-base,repasseValor=diferenca*repasse/100;
 const custoPrazo=creditos*peso*(1-1/(1+taxa/100)**(prazo/12));
 return {debito,creditos,novo,base,transicao,diferenca,repasseValor,efeitoCaixa:repasseValor-diferenca-custoPrazo,custoPrazo,peso};
}
export const percentual=(a,b)=>b>0?a/b*100:null;
