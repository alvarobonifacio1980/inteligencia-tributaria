# Inventário de fontes — 27/11/2026

| Fonte | Resultado efetivo | Uso / fallback |
|---|---|---|
| Empresa Ferroviária DFP 2025 | PDF baixado, texto inspecionado, hash e âncoras; tabelas extraídas e conciliadas | Notas 10/25/29/33; comparativo 2024 |
| Empresa Ferroviária ITR 3T26 | PDF baixado, texto inspecionado, hash e âncoras; tabelas extraídas e conciliadas | DRE p.24, notas 9/27/31; dados de setembro e 9 meses |
| Excel RI Empresa Ferroviária | XLSX válido, seis abas inspecionadas: Índice, Demonstração de Resultados, Endividamento, Resultados Financeiros, Resultados Operacionais e Outros Resultados; valores gerenciais em R$ mi | Fonte complementar; não misturar linhas gerenciais com DRE estatutária sem conciliar |
| CVM DFP 2025 | ZIP obtido; Pandas; CNPJ, escopo, última versão, moeda/unidade e 4 contas conciliadas | CSV apenas Empresa Ferroviária e relatório de conciliação |
| Receita Federal reforma | Página oficial aberta e cronograma conferido | Timeline 2026–2033; condições de teste explícitas |
| LC 214 compilada | Texto oficial aberto por pesquisa; coleta direta não concluída | Art.11 VII, créditos, regimes e transição; regulamentação relevante revisada, sem auditoria integral |
| LC 227/2026 | Texto oficial aberto; arts.136–140 conferidos | Não universalizar 240 parcelas |
| REIDI Portaria 779/2023 | Download direto retornou HTML; texto oficial recuperado por pesquisa/abertura | Estimativas históricas oficiais; simulador de aquisição hipotética, sem afirmar benefício real atual |
| REIDI histórico MT | Tabela oficial e portal conferidos | Estimativas corroboradas; portal lista Portaria 841/2024; revisar atos e aquisição antes de aplicar |
| ANTT SIADE 2026 | CSV candidato e JSON alternativo oficial retornaram HTML de rejeição | Sem números na aplicação; escopo de corredores adiado |
| DIRBI 2024 | Arquivo completo válido (20.137.041 bytes); aba Base_Dirbi filtrada pelo CNPJ e ano | 12 registros únicos, total R$ 140,19918494 mi; declaração, não caixa |

Documentos oficiais possuem atribuição e links; não se republicam PDFs integrais. Coletas válidas em `data/coletas.json`; dados não disponíveis não são completados com valores fictícios.

## Ampliação conciliada — estado atual

Ampliação conciliada e limites atuais:

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

## Evolução V2.1

- DIR 2025 e DIP 2027–2029: PDFs completos válidos, página única renderizada; totais por classe/ano em reais conciliados, traço distinto de zero. Hashes em conciliacao_v2.json.
- CVM DVA consolidada (DFP 2025 / ITR 2026): anual 2024/25 e 9M25/26; códigos 7.08.02.01–03, soma ao total. DFP p.46 e ITR p.33.
- CVM DFC_MI consolidada e ITR p.30: conta 6.01.02.12, pagamentos acumulados −194.592 e −19.087 R$ mil; sinal original preservado e magnitude positiva explícita.
- DFP nota 10(a): compensações de mesma tese 2024/2025; não equivalem ao total de compensações ou nova economia.
- DFP nota 25(c) e ITR nota 23.1(c): riscos possíveis/prováveis, contagens e temas; provável integra total.
- Apresentação 3T26: PDF válido, benchmark visual próprio sem copiar marca; CAPEX gerencial 9M com categorias e arredondamento identificados.
- Tarifas e simulador XLSX: dois arquivos válidos; abas, cabeçalhos, unidades, fórmulas/cache, proteção, nomes e vínculos inspecionados por openpyxl; sem macro/execução ou vínculo externo. Referência sem ICMS, não preço ou contrato real.
- Artigo institucional de 24/11/2026 e programação pública Tax Summit consultados: motivação gerencial, sem inferência de maturidade/processos implantados. Estatísticas externas não usadas como indicadores da empresa.
- Relatório de sustentabilidade indicado: HTTP 403. DVA estatutária/CVM escolhida; comparação numérica não foi fabricada.

Novos dados em base_revisada.json / v2; relatórios em conciliacao_v2.json. Coleta online com snapshot opcional explicitamente marcado quando fonte complementar estiver indisponível; divergência de conteúdo interrompe. Não se republicam PDFs ou planilhas integrais.

## Leituras complementares — 27/11/2026

Acrescentadas ao final de Fontes e metodologia, separadas dos dados dos indicadores: artigo institucional de gestão de24/11/2026; case anunciado na programação oficial do Tax Summit2026 (31/03–01/04); cobertura institucional de19/11/2026 confirmando participação no Brasil nos Trilhos2026; portais oficiais de marcos da Receita Federal e REIDI/Ministério dos Transportes. URLs exatas, contexto, evidência e limites em src/referencias.mjs.

Programação de evento não foi tratada como prova de resultados ou maturidade. O fórum ferroviário é contexto setorial, não evidência de benefício tributário. Referências técnicas gerais não foram apresentadas como eventos com participação da empresa. Autoria e identificação preservadas nos sites originais; textos do painel genéricos.

## Conferência pontual V2.1.1 — 27/11/2026

Consulta documental por ferramenta de pesquisa; não confundir com sucesso de coleta automatizada.

- LC 227/2026, arts. 136–140: conferidos no Planalto. Compensação com IBS distingue ativo permanente (prazo remanescente) e demais créditos (240 parcelas). Ressarcimento alternativo depende da impossibilidade de compensação; art. 139 prevê 240 parcelas ou prazo remanescente, pagamento até 90 dias após encerramento do mês de referência; art. 140 condiciona transferência e parcelas de ressarcimento à regularidade. Texto do painel explicitado, sem mudar simulador hipotético. https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm
- LC 214/2025 compilada: art. 11 VII (destino de carga), arts. 47–49 (crédito, documento, extinção e exceções), arts. 105–106 (REPORTO/REIDI), arts. 343–348 (fase inicial): conferidos. REPORTO art. 105 §7 mantém aquisições até 31/12/2028; REIDI depende de utilização/incorporação e condições específicas. https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
- Decreto 12.955/2026: texto atualizado da Câmara confirma regulamento da CBS; implantação gradual de split payment depende de ato conjunto (art. 33). https://www2.camara.leg.br/legin/fed/decret/2026/decreto-12955-29-abril-2026-799019-normaatualizada-pe.html
- SVRS: aviso de 12/11/2026 confirmado na página abaixo, incluindo CT-e NT 2026.004 v1.01 e adiamento de produção para 14/12/2026. Link específico incorporado; data anunciada não equivale a implantação já realizada. https://dfe-portal.svrs.rs.gov.br/Cte/Avisos/3021
- Split payment: comunicado SVRS de 02/03/2026 confirma caráter preparatório dos campos em 2026 e obrigatoriedade dependente de instrumento regulatório. Fonte separada do aviso CT-e. https://dfe-portal.svrs.rs.gov.br/Nfe/Busca?palavraschave=split+payment

Revisão pontual das afirmações existentes; não constitui auditoria jurídica integral nem comprova elegibilidade de operações reais. Sem divergência numérica identificada nesta revisão; cálculos preservados.
