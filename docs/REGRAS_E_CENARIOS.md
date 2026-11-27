# Revisão de regras e cenários — 27/11/2026

## Fontes consultadas e consequências

- LC 214 compilada: art.11 VII (destino de carga), arts.47–56 (créditos e condições), arts.105–106 (REPORTO e REIDI), art.108 (bens de capital), arts.343–348 (transição).
- LC 227: arts.136–140, segregação, homologação, compensação/transferência/ressarcimento de saldos ICMS. A referência de 240 parcelas não se aplica indistintamente a qualquer estoque.
- Decreto 12.955/2026: texto atualizado aberto na Câmara dos Deputados; RFB lista também Resolução CGIBS 6/2026 e Portaria Conjunta 7/2026. Não se afirma auditoria de toda regulamentação de cada operação.
- CT-e: Ato Técnico Conjunto 10/2026, II, aprova NT 2026.004 v1.01 e 2026.005. Notícia SVRS de 12/11/2026 posterga produção das alterações citadas para 14/12/2026; usar comunicado mais recente, não data inicial de 16/11. Reconfirmar versão na implantação real.
- Split payment: notícia SVRS de 02/03/2026 informa campos preparatórios em 2026 e necessidade de instrumento regulatório para obrigatoriedade. Não se presume implantação universal.
- DOU 12/11/2024 p.55: ADE 1.662/2024 e Portaria 841/2024 correspondem à Fase III. Não são atualização numérica automática da estimativa de Fase II da Portaria 779/2023.

Links exatos sem identificação nominal da empresa: `src/regras.mjs`. Todos os textos públicos usam designação genérica. Documentos oficiais de origem preservam sua identificação própria.

## Reforma: fórmula V2

Bases econômicas por fora. Taxas atual federal e estadual/municipal são líquidas e hipotéticas; não derivadas da dedução bruta da DRE. Crescimento escolhido multiplica receita e custos igualmente. CAPEX elegível é hipótese de aquisição sem regime especial simultâneo.

2026 conserva carga atual hipotética, assumindo cumprimento de obrigações para dispensa do teste. 2027–28: federal atual substituída, CBS plena hipotética menos 0,1 p.p. e IBS 0,1%; estadual/municipal atual permanece. 2029–32: fator IBS 0,1/0,2/0,3/0,4; ICMS/ISS 0,9/0,8/0,7/0,6. Em 2033: integralidade do IBS e legado zero.

Débito = receita × taxa do exercício. Crédito = (custos × elegibilidade + CAPEX × elegibilidade CAPEX) × taxa. Legado = receita × taxa estadual/municipal atual × fator remanescente. Tributo a recolher no modelo = legado + max(débito − crédito, 0). Excedente é exibido separado e não convertido em caixa. O prazo incide sobre créditos utilizados no modelo. Sem apuração por operação, monofasia, regimes diferenciados, imposto seletivo específico, restrições documentais detalhadas ou cálculo de margem/EBITDA. Modelo de sensibilidade, não cálculo para recolhimento.

## CAPEX: fórmula V2

Modelo IBS/CBS de aquisição hipotética a partir de 2027. Seleção de um regime por vez. Resultado numérico condicionado à declaração explícita de uma hipótese de habilitação/eligibilidade, sem confirmar a situação real da empresa. REPORTO além de 2028 bloqueia o cenário conforme art.105 §7. REIDI depende do período de habilitação do projeto, não apenas do ano escolhido.

Suspensão = investimento × parcela elegível × alíquota hipotética. Crédito alternativo = suspensão × fração de crédito sem regime. VP crédito = crédito/(1+taxa anual)^(meses/12). Benefício incremental VP = suspensão − VP crédito − custo. Principal permanente = suspensão − crédito alternativo. A parcela nominal de suspensão não é somada ao benefício VP. Se crédito alternativo integral e imediato, ganho incremental antes dos custos é zero. Não simula multa, cancelamento ou todos os tributos de importação.

## ICMS parcelado

Parcelas iguais, primeira no mês carência+1, taxa efetiva anual e sem correção. VP é soma dos fluxos descontados. O modelo não projeta estoque em 2033 nem incorpora toda atualização monetária legal. Prazos alternativos editáveis são hipóteses econômicas; não representam permissões legais asseguradas.

## Business cases

Três fichas ampliadas: evidência, hipótese, custo/prazo sintéticos ou não estimados, dependências, responsáveis genéricos, confiança, risco, etapas e critério de sucesso. Priorização qualitativa transparente: urgência regulatória e continuidade, depois materialidade e viabilidade. Nenhuma oportunidade é considerada comprovada sem validação dos requisitos.

## V2.1 — decisão metodológica vigente da interface

A interface passa a usar apenas comparação atual hipotética × pleno 2033. O cronograma 2026–2033 permanece legal e qualitativo. A função legada de transição é preservada e testada, mas não oferecida como apuração anual. CAPEX sai do agregado, mantendo simulador próprio. Custos públicos da nota 28 são escala contábil, com fração elegível hipotética e grupos potencialmente indeterminados, sem apropriação automática.

Defaults de demonstração centralizados em modelo.mjs. Créditos: 50 mi, 24 meses, 12% a.a., custo 0,5; alternativas 18/12/6 meses. Mesma base em cada comparação, sem probabilidades. Natureza e vínculo da fonte mudam com edição/reset.

CAPEX prazo: B=I×fração base, T=B×taxa hipotética, R=T×recuperação. VP=R/(1+r)^(m/12); custo do prazo=R−VP; não recuperável=T−R. Ganho incremental líquido=VP no prazo alternativo−VP no prazo atual−custo incremental. DIP vinculado tem investimento bloqueado; selecionar ano/classe muda o valor real de referência. Edição manual desfaz vínculo. Não adicionar T ao total oficial do investimento; não equivale a imposto devido ou incentivo assegurado.

Fixture 100 mi, base 50%, taxa 10%, recuperação 80%, prazo 12m, capital 10%: B50, T5, R4, VP3,636364, custo prazo0,363636, não recuperável1. Custos negativos não permitidos; resultado pode ser negativo, zero ou positivo.

Contratos: base comparável de receita, encargo atual e pleno hipotéticos, volume constante. Δ=novo−referência; comercial=Δ×repasse; residual=Δ×(1−repasse). Δ positivo é encargo maior; Δ negativo é redução potencial, cujo compartilhamento diminui retenção. Referência8/pleno12 e repasse0/50/100% → residual4/2/0 por100. Referência12/pleno8, 50% → −2. Não é preço final, margem, demanda, cláusula de reajuste válida ou previsão. Vigência e marcos são qualitativos.

Tarifa arquivada: E16 arredonda fixa + variável×distância; cache e fórmulas conferidos, base sem ICMS. Exemplo de teto não alimenta receita, tributação de rota ou contrato. Campo de vigência é conservado sem interpretar início/fim não demonstrado; demais serviços têm regras próprias.
