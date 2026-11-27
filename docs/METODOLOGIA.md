# Metodologia e rastreabilidade

Revisão em 27/11/2026. A fonte revisada prevalece sobre valores candidatos do planejamento.

| Conjunto | Granularidade / unidade | Fonte / localizador | Validação |
|---|---|---|---|
| Receita bruta, impostos e líquida | Fluxo anual ou 9 meses, R$ mi | DFP nota 29 p.116; ITR nota 27 p.85 | Bruta − impostos = líquida |
| LAIR, IRPJ/CSLL | Fluxo anual consolidado, R$ mi | DFP DRE p.37 e nota 33 p.121 | Corrente + diferido; CVM 3.07/3.08 |
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
- Reforma: bases econômicas líquidas/por fora. Carga atual é taxa líquida hipotética; custos, elegibilidade, taxas e repasse são hipóteses. A ponderação de transição não reproduz apuração legal mista. Não projetar EBITDA/margem com este modelo.

## Legislação consultada

- LC 214 compilada, art.11 VII: local de transporte de carga pela entrega/disponibilização ao destinatário no documento fiscal.
- LC 214, arts.47–56: condições e regras de créditos; não presumir apropriação automática de todos os custos.
- LC 227, arts.136–140: saldos credores homologados, compensação, transferência e ressarcimento; art.137 II prevê 240 parcelas na hipótese ali definida; art.139 disciplina ressarcimento. Não converter todo saldo atual em 240 parcelas.
- Receita Federal, cronograma 2026–2033: testes condicionados; CBS em 2027 e PIS/Cofins extintos; IBS/ICMS/ISS transição 2029–32; integralidade 2033.
- LC 214 compilada sinaliza Decreto 12.955/2026. Regulamentação operacional e atos CT-e não foram integralmente auditados; nenhuma conclusão de conformidade é fornecida.

Textos oficiais consultados por pesquisa e abertura em 27/11/2026. Coleta direta dos textos do Planalto não foi concluída; consulta web disponível. A legislação requer revisão antes de qualquer decisão real.

## Fontes complementares

ANTT CSV candidato retornou HTML “Request Rejected”, não CSV, em 27/11/2026. Download direto da Portaria REIDI retornou HTML; consulta web oficial permitiu conferir a Portaria 779/2023 e a tabela histórica de estimativas. Valores históricos de investimento R$ 8.732.177.921,82 e suspensões R$ 807.726.457,77, nunca realização. O portal lista Portaria 841/2024; vigência/alterações e elegibilidade por bem ainda exigem validação. Não processar resposta como dado válido. DIRBI: download resultou em arquivo de 2.621.440 bytes sem diretório ZIP válido; página oficial informa ~19.665 KB. Não utilizar arquivo parcial. Sem inferência de tributação individual por rota, regime ou CNPJ na ausência de base validada.

## Preservação

Downloads em cache ignorado; hash SHA-256 registrado. Não republicar PDFs integrais. O snapshot revisado é versionado; substituição do JSON ocorre somente após conciliações. A coleta verifica valores de controle, mas não é um parser universal nem um robô de atualização legislativa.
