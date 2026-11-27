# Inventário de fontes — 27/11/2026

| Fonte | Resultado efetivo | Uso / fallback |
|---|---|---|
| Empresa Ferroviária DFP 2025 | PDF baixado, texto inspecionado, hash e âncoras; tabelas extraídas e conciliadas | Notas 10/25/29/33; comparativo 2024 |
| Empresa Ferroviária ITR 3T26 | PDF baixado, texto inspecionado, hash e âncoras; tabelas extraídas e conciliadas | Nota 9/27; dados de setembro e 9 meses |
| Excel RI Empresa Ferroviária | XLSX válido, seis abas inspecionadas: Índice, Demonstração de Resultados, Endividamento, Resultados Financeiros, Resultados Operacionais e Outros Resultados; valores gerenciais em R$ mi | Fonte complementar; não misturar linhas gerenciais com DRE estatutária sem conciliar |
| CVM DFP 2025 | ZIP obtido; Pandas; CNPJ, escopo, última versão, moeda/unidade e 4 contas conciliadas | CSV apenas Empresa Ferroviária e relatório de conciliação |
| Receita Federal reforma | Página oficial aberta e cronograma conferido | Timeline 2026–2033; condições de teste explícitas |
| LC 214 compilada | Texto oficial aberto por pesquisa; coleta direta não concluída | Art.11 VII e regras gerais de créditos; regulamentação operacional não auditada integralmente |
| LC 227/2026 | Texto oficial aberto; arts.136–140 conferidos | Não universalizar 240 parcelas |
| REIDI Portaria 779/2023 | Download direto retornou HTML; texto oficial recuperado por pesquisa/abertura | Estimativas históricas oficiais identificadas; nenhuma simulação de benefício atual |
| REIDI histórico MT | Tabela oficial e portal conferidos | Estimativas corroboradas; portal lista Portaria 841/2024; revisar atos e aquisição antes de aplicar |
| ANTT SIADE 2026 | CSV candidato e JSON alternativo oficial retornaram HTML de rejeição | Sem números na aplicação; escopo de corredores adiado |
| DIRBI 2024 | Página oficial localizada; arquivo baixado parcial (2.621.440 bytes), inválido como ZIP; origem indica 19.665 KB | Sem filtro CNPJ ou benefício atribuído; fonte não integrada |

Documentos oficiais possuem atribuição e links; não se republicam PDFs integrais. Coletas válidas em `data/coletas.json`; dados não disponíveis não são completados com valores fictícios.

## Ampliação conciliada — estado atual

As situações históricas acima de DIRBI parcial, ausência de IR/CS 9M e ausência de simulação foram superadas:

| Fonte | Resultado atual | Uso |
|---|---|---|
| CVM DFP 2023 | ZIP válido; DRE individual 2022/2023 conciliada | Histórico controladora segregado |
| CVM ITR 2026 | ZIP válido; DRE consolidada acumulada 9M2025/2026 conciliada ao PDF | LAIR, IR/CS, lucro e alíquota efetiva |
| DIRBI 2024 | XLSB completo válido, 20.137.041 bytes; 12 registros únicos pelo CNPJ | Filtro por tributo; total declarado R$ 140,19918494 mi |
| Relatórios públicos da empresa | Volume e investimento por período, destaques p.4 | Contexto operacional com unidade e conceito gerencial |
| ANTT alternativas | API rejeitada; XLSX oficial HTTP 403 | Sem dados por rota; fallback identificado |
| LC 214 compilada / LC 227 | Artigos 105–108 e 343–348; 136–140 revistos | CAPEX condicional, transição explícita e ICMS |
| RFB / CT-e / DOU | Marcos regulatórios, atos técnicos e habilitação histórica consultados | Agenda com status e data; Fases II/III separadas |

Hashes das três bases adicionais em `data/conciliacao_expandida.json`. Dados selecionados em `data/complementos_revisados.json`. Não se publicam bases nacionais ou PDFs integrais no cliente.
