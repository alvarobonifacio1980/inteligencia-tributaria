# Confronto do estado estável com a V2.1

Baseline recuperável: `a961724182664b0baef92c0eebea2a1432c8bf4c`, árvore `1b1baf64bb058bd850604efe5d07b4fb10f0c51f`. Branch de execução `v2-melhorias`. A versão pública não foi alterada durante coleta, desenvolvimento e QA. Nenhum histórico foi reescrito.

| Requisito / critério | Estado no início | Diferença executada / evidência |
|---|---|---|
| 00: proteção, testes e linha de base | 19 testes e site estável | Branch a partir do HEAD verificado; 11 JS + 8 Python e build aprovados antes de alterar código |
| 01: financeiros 9M e créditos | Conciliados | Reutilizados; sem nova atribuição de ausência ou duplicação da coleta validada |
| 01/04: DVA consolidada | Ausente | DVA anual 2024/25 e 9M25/26 conciliada à CVM; soma esferas e sinal estadual negativo preservados |
| 01/04: DFC | Ausente | Saídas originais −194.592/−19.087 R$ mil, DFC consolidada p.30 e conta CVM; magnitude e comparação calculadas |
| 01/04: compensação específica | Ausente | Nota 10(a) DFP p.63: fluxos anuais; sem somar ao estoque ou atribuir causa à DFC |
| 01/04: contingências | 2025 | Série 2024/25/set26, provisão dentro do total; temas 2025 sem fingir atualização; contagens com universo |
| 01/05: DIR/DIP | Ausente | Extração de classes originais e inteiros, traços nulos e zero preservados; totais oficiais e horizonte conciliados |
| 01/09: apresentação 3T26 | Tema existente | PDF recuperado; inspeção visual p.6; gráficos e CAPEX p.17 inspecionados; rótulos, contraste e comparativos incrementais |
| 01/06: tarifas | Não inspecionadas | XLSX abertos sem macros; abas, fórmulas/cache, proteção, nomes e vínculos inspecionados; exemplo E16 reproduzido; sem usar teto como preço |
| 01: sustentabilidade | Complementar | PDF indicado retornou HTTP 403; DVA estatutária/CVM prevalece; sem equivalência numérica inventada |
| 02: números/datas e natureza | Duplicações/fixos | Derivações em modelo.mjs; dados e defaults separados do JSX; origem por campo; vazio conserva último válido com aviso |
| 02: rastreabilidade/modal | Adaptado presente | Preservado e estendido a Híbrido/Sintético; fórmulas, referências e limites; metadados por domínio |
| 02: validação de publicação | V1 | validar() ampliado a DVA, DIR/DIP, DFC e riscos; geração atômica após conciliação; snapshot preservado em falha de fonte |
| 03: executivo recente | Inicial anual | Inicia último período disponível (9M2026), variações equivalentes e p.p.; patrimônio com data própria |
| 03: gráficos e insights | Receita/tributos na mesma escala | Dois gráficos independentes; composição acessível; três mensagens ligadas às subabas |
| 04: ponte de créditos | Evolução por tributo | Cascata de datas/tributo com universo coerente, Outros e contribuição; positivo/negativo/zero testados |
| 04: IR/CS | Cascata anual | Preservada; resumo/detalhamento, 9M25/26 separados, ajustes e alíquotas calculados |
| 04: resultado/patrimônio/caixa | Sem painel conjunto | Bloco de conceitos distintos e fontes próprias; não soma DRE/DVA/DFC/créditos |
| 05: contexto ferroviário | Volume/investimentos | Preservado; não calcula intensidade por tonelada com universo que inclui carga sem receita |
| 05: DIRBI e regimes | Tabela integrada | Filtro e gráfico por programa, REIDI/REPORTO, total calculado; histórico distinto de benefício novo |
| 05: CAPEX futuro | Sem DIR/DIP | Colunas empilhadas e total, tabela original, realizado separado de previsão; seleção ano/classe abre cenário vinculado |
| 06.1: créditos | VP e opção 10% público | Presets comparáveis, gráfico, resultado bruto/líquido, origem dinâmica, reset e exportação |
| 06.2: reforma | Transição econômica aproximada | Interface prioriza pleno 2033, cronograma legal separado; CAPEX fora do agregado; componentes CBS/IBS, excedente separado, CBS limitada 0–100% |
| 06.3: CAPEX prazo | Suspensão condicional | Modelo de prazo com DIP bloqueado enquanto vinculado, fração de base hipotética, VP, recuperação e custo; fixture independente |
| 06.4: contratos | Ausente | Comparativo normalizado 0/50/100%, sinais de compartilhamento, marcos qualitativos, origem e agenda; não soma ao agregado |
| 07: reforma e funções | Agenda/matriz básica | Oito temas, regra/impacto/ação/marco/funções/fonte; ações 2027/29/33; sem afirmar prontidão interna |
| 08: três business cases | Fichas estáticas ampliadas | BC01/02/03 usam estado atual dos simuladores; critérios, dependências, riscos e custos/prazos não estimados; mapa conceitual ERP |
| 09: navegação | Estado local sem links diretos | Hash simples, subabas, Voltar/Avançar, título, foco, teclado e aria-current; seis módulos mantidos |
| 09: CSV/impressão | Exportação financeira e fluxos | Contexto de cada análise, premissas/resultados com unidades, Excel pt-BR e proteção de fórmulas; campos mantidos na impressão |
| 09/10: responsividade | Desktop/móvel V1 | Subabas verificadas em 390×844; inspeções adicionais e limites em TESTES_V2.md |
| 10: testes/gate | 19 testes | 23 JS + 16 Python aprovados; cenários compartilhados e invariantes independentes; build; regressão e visual em TESTES_V2.md |
| 11: publicação | URL pública V1 | Publicar somente após gate; mesma URL, rollback pelo commit anterior; registro final em STATUS.md |

Não foram repetidas etapas já aprovadas da V1. Limites de fonte são tratados como limites explícitos, não como números inventados ou novo escopo. O modelo é gerencial, sem apuração fiscal por documento, integração empresarial ou parecer de elegibilidade.
