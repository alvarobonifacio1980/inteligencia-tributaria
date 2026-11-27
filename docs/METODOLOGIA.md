# Metodologia e rastreabilidade

Revisão em 27/11/2026. A fonte revisada prevalece sobre valores candidatos do planejamento.

| Conjunto | Granularidade / unidade | Fonte / localizador | Validação |
|---|---|---|---|
| Receita bruta, impostos e líquida | Fluxo anual ou 9 meses, R$ mi | DFP nota 29 p.116; ITR nota 27 p.85 | Bruta − impostos = líquida |
| LAIR, IRPJ/CSLL | Fluxo anual ou 9 meses consolidado, R$ mi | DFP DRE p.37 e nota 33 p.121; ITR DRE p.24 e nota 31 | Corrente + diferido; CVM 3.07/3.08 |
| Créditos | Estoque por data e tributo, R$ mi | DFP nota 10 p.63; ITR nota 9 p.48–49 | Soma tributos = total = circulante + não circulante |
| ICMS por UF | Subtotal circulante RJ/SP | ITR nota 9 p.49 | Não equiparar ao total ICMS |
| Contingências | Posição em 31/12/2025 | DFP nota 25 p.109 | 194 − 26 = 168 ações de risco; provisão incluída na exposição |
| Reconciliação IR/CS | 2025 consolidado, R$ mil | DFP nota 33 p.121 | 731.941 − 134.236 = 597.705 |

CNPJ validado na CVM: 01.417.222/0001-77; código CVM 017949. Seleção: consolidado, último exercício, maior versão, moeda REAL, escala MIL. Contas conciliadas 3.01, 3.07, 3.08 e 1.01.06. CSV com as linhas da companhia, sem base nacional no cliente.

## Correções e escolhas

- DFP consolidado IR/CS R$ 597,705 mi, 27,76%; controladora R$ 594,868 mi, 27,67%. Não misturar.
- Receita líquida 2024 exata na DFP: R$ 7.024,973 mi. Relatório de sustentabilidade usa arredondamento gerencial.
- Estoques de crédito têm data própria; filtro financeiro não os altera. Comparação somente anual/anual ou 9M/9M.
- Tributos sobre serviços é valor real; percentual sobre receita bruta é adaptado. Não representa recolhimento líquido após créditos.
- Simulação de realização única, sem correção monetária. Usar 10% do saldo oficial cria cenário híbrido; percentual não é elegibilidade comprovada.
- Reforma: bases econômicas líquidas/por fora. Carga atual é taxa líquida hipotética; custos, elegibilidade, taxas e repasse são hipóteses. A CBS substitui a parcela federal hipotética em 2027; o legado estadual/municipal remanescente reduz conforme transição. Créditos excedentes não viram caixa automaticamente. Não projetar EBITDA/margem com este modelo.

## Legislação consultada

- LC 214 compilada, art.11 VII: local de transporte de carga pela entrega/disponibilização ao destinatário no documento fiscal.
- LC 214, arts.47–56: condições e regras de créditos; não presumir apropriação automática de todos os custos.
- LC 227, arts.136–140: saldos credores homologados, compensação, transferência e ressarcimento; art.137 II prevê 240 parcelas na hipótese ali definida; art.139 disciplina ressarcimento. Não converter todo saldo atual em 240 parcelas.
- Receita Federal, cronograma 2026–2033: testes condicionados; CBS em 2027 e PIS/Cofins extintos; IBS/ICMS/ISS transição 2029–32; integralidade 2033.
- LC 214 compilada sinaliza Decreto 12.955/2026. Regulamentação operacional e atos CT-e não foram integralmente auditados; nenhuma conclusão de conformidade é fornecida.

Textos oficiais consultados por pesquisa e abertura em 27/11/2026. Coleta direta dos textos do Planalto não foi concluída; consulta web disponível. A legislação requer revisão antes de qualquer decisão real.

## Fontes complementares

ANTT: CSV/JSON/API retornaram rejeição HTML; XLSX oficial alternativo retornou 403. Dados operacionais do relatório público da empresa são fallback explícito, não dados ANTT nem inferência fiscal por rota.

DIRBI 2024: arquivo completo de 20.137.041 bytes validado e processado. Aba Base_Dirbi, CNPJ completo, ano 2024, 12 registros únicos; R$ 140,19918494 mi declarados. UF é domicílio declarado, não cobertura operacional. Conversão reais/milhões; sem somar a créditos reconhecidos ou estimativas de portarias. Identificadores textuais truncados/científicos não são inferidos.

CVM DFP 2023: 2022–2023 individual/controladora em tabela própria. CVM ITR 2026: DRE consolidada acumulada janeiro–setembro, maior versão; não trimestre isolado. 9M2026: LAIR 1.295,227 e IR/CS 428,676 mi; corrente 88,303 + diferido 340,373. 9M2025: LAIR 1.690,078 e IR/CS 464,453; corrente 166,115 + diferido 298,338. Conferência ITR p.24 e CVM; alíquota = IR/CS ÷ LAIR.

REIDI: Portaria 779/2023 Fase II é estimativa histórica; Portaria 841/2024 e ADE 1.662/2024 referem-se à Fase III, não atualização numérica automática da Fase II. Nenhum ato histórico comprova elegibilidade de toda compra futura.

Regras verificadas e fórmulas completas dos quatro simuladores: [REGRAS_E_CENARIOS.md](REGRAS_E_CENARIOS.md). Agenda técnica: NT CT-e 2026.004 v1.01 com produção anunciada para 14/12/2026, conforme comunicado oficial de 12/11/2026; split payment preparatório não implica exigência universal imediata. Sem conclusão de conformidade integral.

## Preservação

Downloads em cache ignorado; hash SHA-256 registrado. Não republicar PDFs integrais. O snapshot revisado é versionado; substituição do JSON ocorre somente após conciliações. A coleta verifica valores de controle, mas não é um parser universal nem um robô de atualização legislativa.
