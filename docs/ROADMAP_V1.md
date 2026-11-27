# Inteligência Tributária — Roadmap V1.0

**Subtítulo:** Planejamento estratégico e eficiência fiscal  
**Estudo de caso:** MRS Logística — setor ferroviário brasileiro  
**Data-base do planejamento:** 27/11/2026  
**Status:** planejamento consolidado; implementação, validação de arquivos e publicação ainda pendentes.  
**Pilares:** Diagnosticar · Otimizar · Antecipar

## 1. Finalidade e contexto

Iniciativa profissional independente para complementar a candidatura à vaga de Especialista Tributário da MRS Logística, Juiz de Fora/MG. Não é encomenda, auditoria, parecer tributário, produto oficial, diagnóstico interno nem promessa de economia. O objetivo é apresentar à recrutadora e aos gestores, inclusive após a entrevista, uma aplicação que demonstre capacidade de integrar dados, finanças, tecnologia, planejamento tributário e gestão de projetos. O acesso deve ser imediato, anônimo e gratuito. Não enviar mensagem à recrutadora automaticamente.

A missão da vaga é converter oportunidades, riscos e mudanças tributárias em análises econômico-financeiras, business cases, recomendações executivas e projetos implementáveis, integrando Planejamento Tributário, Finanças, Operações, Tecnologia, Suprimentos, Comercial, Jurídico e demais áreas. A gerência apoia decisões da alta administração, sustentabilidade financeira e conformidade; a vaga exige análise de dados, dashboards gerenciais, comunicação objetiva, gestão de projetos e visão estratégica, além de Excel/Power BI e conhecimentos desejáveis de Python, HTML e legislação tributária.

Público primário: gerência, especialistas de planejamento e alta liderança; público inicial: recrutadora, que deve compreender o propósito sem conhecimento técnico. Público operacional secundário. Valorizar a trajetória real do candidato em gestão de TI, processos, integração e análise de dados, sem atribuir experiência fiscal interna ou certificações não confirmadas.

### Decisões consolidadas e precedência

- Power BI Desktop permanece opção futura. Conta pessoal não funcionou no Service; UFJF permitiu acesso mas bloqueou Publish to Web por administração; domínio CDMF não autenticou; não há caminho permanente, anônimo e gratuito comprovado no contexto atual. Não insistir em licenças, trials, novos tenants, conversores ou duas interfaces.
- MVP web em React + ECharts, ETL em Python/Pandas, arquivos CSV/JSON e GitHub Pages. Sem servidor de aplicação, banco remoto ou API própria.
- Preservar a possibilidade de reconstrução futura em Power BI e de apresentação estática em PowerPoint. Não construir nenhum dos dois agora. A interatividade web não precisa ser reproduzível em PPT; o conteúdo executivo, sim.
- Roadmap V1 prevalece sobre planejamento antigo do Power BI; histórico complementa motivações. Consultar o chat de origem, o chat anterior “Desenvolver Dashboard Fiscal” / “Desenvolver dashboard fiscal” e “Avaliações diversas de oportunidades” do projeto Carreira se acessíveis; a grafia dos títulos pode variar. Eventual pacote antigo `tax-intelligence-poc.zip` não é dependência, não foi inspecionado nesta consolidação; reaproveitar somente após validação, se encontrado e útil.

## 2. Requisitos estruturantes (PE)

| ID | Requisito |
|---|---|
| PE01 | Orçamento de implantação, fontes e infraestrutura R$ 0; não contratar, ativar trials, inserir cartão ou assumir despesas. |
| PE02 | Máxima automação e interações mínimas com o patrocinador. |
| PE03 | Conteúdo, interface, documentação de negócio e mensagens em português do Brasil. |
| PE04 | Priorizar dados públicos reais; adaptar/simular apenas lacunas necessárias. |
| PE05 | Arquitetura KISS, modular e extensível. |
| PE06 | GitHub pessoal, versionamento e publicação automatizada. |
| PE07 | Independência de licenças comerciais. |
| PE08 | Separar dados, regras analíticas, interface e tema. |
| PE09 | Fundamentação tributária em legislação e documentos oficiais vigentes. |
| PE10 | Reaproveitamento futuro de base/modelo/indicadores no Power BI; síntese em PowerPoint. |
| PE11 | Nenhum dado interno, pessoal ou sigiloso; não sugerir vínculo institucional. |
| PE12 | KISS em toda decisão: valor para negócio antes de quantidade de recursos. |
| PE13 | Orientação tática, estratégica e executiva. |
| PE14 | Classificação da natureza dos dados por indicador, gráfico, tabela e cenário. |
| PE15 | Rastreabilidade a fonte, documento, página/aba/conta, período e versão quando disponíveis. |
| PE16 | Separar fatos observados, cálculos, estimativas, simulações e hipóteses. |
| PE17 | Fundamentação legislativa com data de verificação e distinção entre regra vigente, transição e hipótese. |
| PE18 | Avaliação econômico-financeira das oportunidades. |
| PE19 | Identificar áreas envolvidas e plano de ação de cada business case. |
| PE20 | Detalhamento progressivo; primeira página compreensível rapidamente. |
| PE21 | Insights calculáveis, explicáveis e reproduzíveis, sem API de IA paga. |
| PE22 | Recomendações condicionadas a validação interna fiscal, jurídica, contábil e financeira. |
| PE23 | Evitar dupla contagem de créditos, benefícios e impactos. |
| PE24 | Distinguir economia fiscal, efeito de caixa, valor presente, redução de riscos e produtividade. |
| PE25 | Identidade visual inspirada nos materiais institucionais da MRS. |
| PE26 | Tema centralizado de cores, tipografia e componentes. |
| PE27 | Legibilidade, hierarquia executiva e acessibilidade visual. |
| PE28 | Não usar logomarca oficial, fotos sem licença ou elementos de falsa afiliação. |
| PE29 | Priorizar gráficos nativos/convencionais, indicadores, tabelas e layouts replicáveis no Power BI; cada página deve poder ser sintetizada em 1–2 slides executivos. |
| PE30 | Automação de ingestão, testes, build, publicação, documentação e recuperação de falhas; nenhuma ação pública externa fora do escopo (ex.: enviar e-mail). |

## 3. Arquitetura e identidade visual

Fluxo: fontes oficiais → download/extração → Python/Pandas (normalização, validação, agregação e conciliação) → CSV/JSON de publicação → React + Apache ECharts → build estático → GitHub Pages. Vite ou equivalente simples, versões fixadas por lockfile, Python com dependências registradas. Usar apenas dependências gratuitas/licenças compatíveis. Não introduzir frameworks, APIs, banco ou infraestrutura adicional sem necessidade demonstrada. Filtros e simuladores no navegador; arquivos analíticos pré-processados, não baixar bases nacionais inteiras no cliente. Cálculos compartilhados por especificações e fixtures de teste, evitando divergência Python/JS. GitHub Actions para testes e deploy com permissões mínimas; preferir execução manual por workflow_dispatch e build/deploy no push, evitando agendamentos frequentes sem necessidade. Verificar planos/limites e regras atuais antes de ativar. Se a conta não permitir Pages gratuito ou exigir autorização, não contratar; reportar bloqueio e fornecer build local.

Identidade: **Inteligência Tributária** / **Planejamento estratégico e eficiência fiscal** / **Estudo de caso — MRS Logística**. Inspiração nos relatórios de resultados, sustentabilidade e site institucional da MRS, sem imitar produto oficial. Paleta inicial aproximada (não manual oficial): #002B49 azul escuro, #005BAA azul principal, #FFD200 amarelo de destaque, #007EBA azul complementar, #F3F5F7 fundo, #FFFFFF superfície. Montserrat/Inter ou fontes de sistema compatíveis, preferir assets locais/licenciados. Verde/vermelho discretos apenas com texto/ícone complementar. Menu lateral azul, seleção amarela, área analítica clara, desktop prioritário e layout móvel responsivo. Usar amarelo com texto escuro e contrastes verificáveis. Rodapé/identificação visível: “Estudo independente, baseado em dados públicos e simulações. Sem vínculo institucional com a MRS.”

**Impacto visual sem excesso:** cards de KPI, linhas, colunas, barras, cascata, composição simples, tabelas/matrizes, segmentadores e timeline. Mapas apenas se agregarem valor e forem sustentados por dados e licenças. Evitar 3D, efeitos CSS elaborados, animações gratuitas, visualizações exóticas, dependência de visuais personalizados, dashboards com dezenas de gráficos. Usar grid consistente e gráficos com rótulos legíveis. Proposta por página: 4–6 KPIs quando pertinentes, 2–3 gráficos centrais, até 3 insights em destaque, tabelas/detalhes sob demanda; não preencher cotas artificialmente. Primeira tela deve mostrar propósito, data-base, métricas e ação relevante sem tutorial.

## 4. Inventário de fontes candidatas e estratégia de dados

Links abaixo foram identificados no planejamento anterior. São pontos de partida, não comprovação de disponibilidade atual ou de que o arquivo foi processado. Verificar acesso, conteúdo, competência, licença, escopo individual/consolidado e revisões antes de usar. Não fabricar dados se um link falhar: procurar endereço oficial alternativo, registrar evidências e reduzir escopo se necessário.

| Fonte | Link inicial | Uso |
|---|---|---|
| RI MRS | https://ri.mrs.com.br/informacoes-financeiras/central-de-resultados/ | DFP, ITR, releases, apresentações e resultados interativos |
| Relatórios anuais MRS | https://ri.mrs.com.br/informacoes-financeiras/relatorios-anuais/ | Contexto histórico |
| Sustentabilidade MRS | https://www.mrs.com.br/sustentabilidade/ | Contexto operacional/visual |
| DFP 2025 MRS (PDF candidato) | https://api.mziq.com/mzfilemanager/v2/d/e14f1680-635b-4328-8a06-b799b1574b43/acbef322-8f85-850f-ae21-8d531a3467b4?origin=2 | Notas tributárias, receita, IRPJ/CSLL, contingências |
| ITR 3T26 (PDF candidato) | https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/ed0c4c1c-5cc3-4a74-ac98-e657a4cd7bbf | Créditos, passivos, notas |
| Release 3T26 | https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/a21948c4-c51e-4c70-ba17-cc332fe9741f | Indicadores gerenciais |
| Excel de resultados MRS | https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/da20407a-9590-4cd5-865c-a65c0ee52fbc | Inspecionar abas; confirmar utilidade |
| CVM DFP | https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp | CSV anuais por companhia/conta |
| CVM ITR | https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr | CSV trimestrais por companhia/conta |
| ANTT SIADE | https://dados.antt.gov.br/dataset/sistema-de-acompanhamento-do-desempenho-operacional-das-concessionarias-siade | Produção por competência, ferrovia, mercadoria, origem/destino, TU/TKU |
| ANTT produção histórica | https://www.gov.br/antt/pt-br/assuntos/ferrovias/dados-de-producao-do-transporte-de-carga-origem-destino | Excel/CSV histórico |
| ANTT CSV 2025 | https://dados.antt.gov.br/dataset/438a5184-09db-49a3-88c8-0bad418b4409/resource/d7263808-bd77-4153-9910-49e041d73b21/download/producao_origem_destino_2025.csv | Referência operacional |
| ANTT CSV 2026 | https://dados.antt.gov.br/dataset/438a5184-09db-49a3-88c8-0bad418b4409/resource/c2854ec9-1cc5-4554-a1ae-96c5f37b5df6/download/producao_origem_destino_2026.csv | Exercício em andamento |
| ANTT tarifas e preços | https://www.gov.br/antt/pt-br/assuntos/ferrovias/relatorio-de-tarifas-e-precos/relatorio-de-tarifas-e-precos | Referências agregadas, não preço de contrato |
| ANTT declaração de rede | https://www.gov.br/antt/pt-br/assuntos/ferrovias/declaracao-de-rede/declaracao-de-rede-2025 | Malha e estações |
| ANTT concessão | https://www.gov.br/antt/pt-br/assuntos/ferrovias/concessoes-ferroviarias/mrs-logistica-s-a/contrato-de-concessao-e-aditivos | Obrigações/investimentos |
| Ministério dos Transportes REIDI | https://www.gov.br/transportes/pt-br/assuntos/incentivos/reidi | Projetos/regimes |
| Portaria 779/2023 | https://www.gov.br/transportes/pt-br/assuntos/incentivos/incentivos-fiscais/reidi-requerimento-e-consulta/Portarian779de03ago2023MRSLogsticaREIDIDOU04ago2023.pdf | Projeto Malha Sudeste Fase 2; estimativas de aprovação |
| Receita Federal benefícios | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/beneficios | DIRBI e benefícios |
| DIRBI 2024 | https://www.gov.br/fazenda/pt-br/assuntos/politica-fiscal/atuacao-spe/plataforma-de-desoneracoes-tributarias/arquivos/desoneracoes-dirbi-2024.xlsb/view | Filtrar pelo CNPJ oficial confirmado; verificar cobertura |
| Receita Federal arrecadação CNAE | https://www.gov.br/receitafederal/dados/arrecadacao-cnae.csv/view | Contexto setorial, não arrecadação individual |
| ANTF | https://www.antf.org.br/dados/ | Contexto setorial, secundário |
| Dados geográficos | https://dados.transportes.gov.br/dataset/dados-georreferenciados-no-ministerio-dos-transportes-ferroviario | Opcional |
| Receita Federal reforma | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/reforma-tributaria-do-consumo/entenda/entenda-a-reforma-tributaria-do-consumo/ | Cronograma e guias oficiais |
| LC 214/2025 compilada | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm | Regras do consumo, créditos, regimes especiais |
| LC 227/2026 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm | IBS, transição e saldos de ICMS |
| EC 132/2023 | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm | Base constitucional da reforma |

Também consultar regulamentos vigentes, atos oficiais e documentação técnica CT-e se necessários; conferir artigos e redação compilada no momento da implementação. Fontes de custo zero; observar direitos de reprodução e atribuição, sem republicar PDFs integrais ou arquivos grandes se não necessário.

### Período, granularidade e conciliação

Proposta inicial 2022 até último período oficial disponível; 2025 exercício anual de referência, 3T2026 referência recente a verificar. Não forçar cobertura uniforme; exibir períodos reais e lacunas. Priorizar consolidado e distinguir controladora. Identificar companhia por CNPJ/código CVM e concessionária por chave normalizada; evitar homônimos. Em ITR, distinguir acumulado e trimestre isolado, datas de referência, reapresentações, moeda e unidade; não somar estoques trimestrais. Conciliar valores CVM com RI/notas. ANTT: TU/TKU, competência, origem/destino, mercadoria; não inferir imposto, tarifa ou preço individual de rota. Não vincular valores financeiros agregados a rotas sem rateio explicitamente estimado. DIRBI: não somar duplicidades, não confundir renúncia declarada com caixa recebido ou economia incremental. Registrar fonte ausente e fallback.

### Classificação visível e metadados

- **Real:** fato ou valor publicado, preservando conceito, granularidade e escopo. Uma estimativa oficialmente divulgada deve ser rotulada como “Real — estimativa oficial”, não como valor realizado.
- **Adaptado:** transformação/cálculo sobre dados reais; distinguir derivação exata de estimativa por rateio/hipótese. Se hipóteses materiais forem combinadas, classificar preferencialmente como híbrido.
- **Híbrido:** fatos oficiais combinados com premissas hipotéticas (ex.: saldo público e prazo simulado).
- **Sintético:** dados fictícios para demonstrar processo interno, nunca apresentados como fatos sobre MRS.

Cada indicador/visual: natureza, fonte, URL, documento, competência/data de corte, entidade/escopo, unidade, fórmula, premissas, limitações, data da coleta/validação e página/aba/conta quando disponível. Tooltip ou painel de detalhes; página “Fontes e metodologia” com catálogo completo, versões e links. Texto e ícone junto à cor. Simulações sempre explicitamente hipotéticas; separar visualmente resultados observados e cenário. Nunca tratar saldo de crédito reconhecido como novo benefício descoberto.

### Valores candidatos previamente localizados (não carregar como verdade sem validar)

DFP 2025: receita bruta de serviços ~R$ 8,05 bi; impostos sobre serviços ~R$ 469,79 mi; receita líquida ~R$ 7,59 bi; IRPJ/CSLL ~R$ 597,71 mi; alíquota efetiva ~27,76% (2024 ~30,87%); nominal 34%; reconciliação da nota 33. ITR 3T26: tributos a recuperar ~R$ 553,76 mi (dez/25 ~R$ 387,95 mi), ICMS ~R$ 277,60 mi, PIS/Cofins ~R$ 129,01 mi, IR retido ~R$ 146,39 mi, outros ~R$ 0,77 mi. ICMS circulante RJ/SP ~R$ 103,99/99,68 mi (não confundir subtotal circulante com total ICMS). Contingências 2025: números candidatos ~194 processos tributários, 26 ações de recuperação, R$ 1,09 bi perdas possíveis/prováveis, R$ 151,21 mi provisões; verificar conceitos, classes e não somar provisão à exposição se já incluída. REIDI Portaria 779/2023: estimativas originais ~R$ 8,73 bi investimentos, R$ 807,73 mi suspensões, 93 locomotivas, 3.981 vagões; confirmar atualizações e não tratá-las como realização. Se divergirem das fontes, prevalecem dados conferidos; documentar correção.

## 5. Modelo analítico mínimo

Tabelas de fatos candidatas (criar apenas necessárias): `fato_financeiro` (competência, conta, entidade/escopo), `fato_transporte` (mês, concessionária, mercadoria, estação/UF origem/destino), `fato_creditos_tributarios` (data de saldo, tributo, localização quando disponível, classificação circulante/não circulante), `fato_obrigacoes_fiscais`, `fato_beneficios_fiscais` (benefício/período/projeto quando identificado), `fato_investimentos` (projeto/período), `fato_contingencias` (data, natureza, classificação), `fato_simulacoes` ou configuração de cenários. Dimensões compartilhadas quando pertinentes: tempo, tributo, localidade, mercadoria, projeto, fonte, escopo. Definir chaves, unidades, granularidade e regras de agregação. Não materializar tabelas vazias apenas por desenho. Preferir formatos portáveis; dicionário de dados e indicadores independente de React e reutilizável em BI.

## 6. Produto e requisitos funcionais

| Módulo | MVP e experiência |
|---|---|
| 01 Visão executiva | 4–6 KPIs validados: receita, tributos sobre serviços, alíquota efetiva IRPJ/CSLL, tributos a recuperar/ICMS, contingências ou CAPEX conforme disponibilidade. 2–3 gráficos e agenda de até 3 insights acionáveis. Períodos explícitos. |
| 02 Diagnóstico tributário | Evolução e composição de créditos, alíquota efetiva e reconciliação em cascata, tributos sobre serviços, contingências por classe e contexto operacional ANTT quando validado. Detalhes sob demanda. |
| 03 Eficiência tributária | Gestão de créditos, capital de giro, estratégia ICMS, REIDI/REPORTO e CAPEX, evidências e oportunidade de investigação. Acessos a simuladores sem duplicar tela. |
| 04 Reforma tributária | Timeline 2026–2033, impactos setoriais, regras e agenda de adequação, simulador comparativo. Evidenciar o que é vigente, transição ou incerto. |
| 05 Cenários e projetos | Simuladores e business cases priorizados, VPL/efeito caixa, riscos, dependências e áreas. |
| Fontes e metodologia | Acesso transversal; catálogo, fórmulas, premissas, classificação, data de atualização, limitações. |

| ID | Requisito | Prioridade |
|---|---|---|
| RF01 | Filtros por período, tributo, localização/operação quando granularidade suportar | Essencial |
| RF02 | Atualização coerente dos indicadores e gráficos; filtro não aplicável identificado | Essencial |
| RF03 | Gráficos/tabelas interativos, tooltip, navegação clara | Essencial |
| RF04 | Comparação de períodos equivalentes, sem comparar acumulado com trimestre | Essencial |
| RF05 | Detalhamento de indicadores e fonte | Essencial |
| RF06 | Simuladores de créditos e reforma, cenários editáveis e reset | Essencial |
| RF07 | Fórmulas, premissas, unidades e limites acessíveis | Essencial |
| RF08 | Exportação CSV de dados filtrados ou síntese, se simples | Desejável |
| RF09 | Resumo executivo imprimível ou exportável, sem exigir geração PPTX | Desejável |
| RF10 | Atualização legislativa automatizada integral | Evolução |
| RF11 | Análise preditiva/ML | Evolução |
| RF12 | Matriz de oportunidades e fichas de business case | Essencial |
| RF13 | Insights calculados sobre evidências e cenários, com ação e limitação | Essencial |
| RF14 | Classificação, rastreabilidade e data-base visíveis em todas as páginas | Essencial |
| RF15 | Simulação de investimentos com regimes especiais, se premissas legais validadas | MVP preferencial; se insuficiente, ficha qualitativa e cenário simplificado explícito |

## 7. Dicionário preliminar de métricas e regras

- Receita bruta e líquida de serviços: contas oficiais, escopo/período declarados; reconciliar com deduções e outros ajustes, não presumir apenas impostos.
- Tributos incidentes sobre serviços: deduções de receita divulgadas; indicador adaptado = valor absoluto / receita bruta de serviços × 100. Não chamar de carga tributária total.
- Alíquota efetiva de IRPJ/CSLL = despesa líquida sobre lucro / lucro antes de IRPJ/CSLL × 100, conforme nota; validar sinais, corrente/diferido, base negativa ou zero (não aplicável) e reconciliação com nominal. Não confundir com tributos sobre consumo.
- Tributos a recuperar: estoque em data de referência; composição por tributo, circulante/não circulante quando divulgado; variação absoluta e percentual com períodos comparáveis e denominador válido. Saldo não é necessariamente recuperável imediatamente.
- Contingências: valores por classe conforme CPC/nota divulgada; exposição possível/provável e provisão não devem ser agregadas se sobrepostas; não reclassificar processos.
- CAPEX/incentivos: distinguir investimento estimado/aprovado/realizado, suspensão, isenção definitiva, crédito e benefício de caixa. Benefícios não automaticamente somáveis.
- Operações: TU/TKU e distribuição por rota/mercadoria; calcular razões apenas sobre universo consistente. Não inferir tributação individual da rota.
- Indicadores de cenário: VPL incremental, fluxo de caixa, payback se aplicável e com fluxo adequado, sensibilidade, margem/EBITDA apenas se efeitos econômicos/contábeis forem explicitados. Nenhum cálculo sem unidade, fórmula, hipótese e limites.

## 8. Reforma tributária e oportunidades

Verificar legislação oficial atualizada antes de implementar, inclusive EC 132, LC 214 compilada, LC 227 e regulamentação pertinente. Linha do tempo candidata: 2026 testes e obrigações acessórias conforme regras/dispensa aplicáveis; 2027 entrada CBS e extinção PIS/Cofins, 2027–28 transição federal; 2029–32 substituição progressiva ICMS/ISS por IBS; 2033 novo regime. Conferir exceções, percentuais e obrigações específicas. Não aplicar reduções destinadas a transporte coletivo de passageiros ao transporte ferroviário de cargas. Não tratar alíquota de referência futura estimada como definitiva.

Temas prioritários: créditos IBS/CBS e condições de apropriação; saldos ICMS e homologação/transição (eventual realização em até 240 parcelas em hipóteses legais, conferir exceções e atualização); REIDI e REPORTO (elegibilidade, habilitação, bens, destinação e prazos); bens de capital; local da operação no transporte de cargas (destino indicado em documento fiscal, conferir art. 11); contratos e preços; repasse e margens; fluxo de caixa, split payment se pertinente; CT-e e adequação de sistemas. Candidatos na LC 214: arts. 11, 47–56, 105, 106, 108 — verificar texto compilado, não citar de memória. Distinguir efeito em cadeia, na empresa e no cliente; não prometer economia.

### Estudos de caso e simulações

1. **Realização de créditos** (essencial). Usar saldo real como referência e parcela elegível hipotética editável, prazo atual e proposto, custo de capital anual, custo inicial. Modelo simples: VP = C/(1+r)^(m/12); benefício líquido incremental = VP proposto − VP atual − custo inicial. Exemplo exclusivamente hipotético: C=R$50 mi; prazos 24/12 meses; taxa 12% a.a.; custo R$0,5 mi. Premissas: realização única, sem correção monetária; alternativa de fluxo mensal se simples. Validar limites e não apresentar antecipação como redução do principal. Áreas: Tributário, Tesouraria, Contabilidade, Jurídico e TI.
2. **Créditos ICMS até 2033** (essencial, pode compartilhar simulador 1). Conservador/intermediário/otimizado, com diferentes percentuais e prazos de realização legalmente possível; projetar caixa e VP. Não presumir todos os créditos sujeitos ao mesmo tratamento nem que saldo de hoje persista até 2033. Comparação qualitativa quando informação insuficiente.
3. **CAPEX/REIDI/REPORTO** (essencial como análise, simulador preferencial). Usar portaria de investimento como referência; com/sem regime quando elegível; comparar desembolso, suspensão, apropriação de créditos, prazo e efeito econômico. Não aplicar benefício automaticamente a todos os ativos nem sobrepor regimes. Áreas: Engenharia, Suprimentos, Tributário, Finanças, Jurídico.
4. **Reforma tributária** (essencial). Comparar regime atual/transição/novo em exercício selecionado; receitas e custos calibrados por fonte pública, proporção de custos elegíveis, alíquotas de IBS/CBS explicitamente hipotéticas quando não definidas, repasse ao cliente, crescimento, CAPEX e prazo de crédito. Calcular débito/crédito por bases coerentes, tributos líquidos, efeito caixa, margem e EBITDA somente sob hipóteses contabilmente válidas. Não comparar tributo por dentro com por fora sem harmonização. Cenário simplificado se faltar dado; mostrar fórmula e premissas. Não extrapolar previsão da MRS. Testar zero créditos, 100% elegibilidade, sem repasse, mudança de alíquota, etapas de transição e evitar dupla contagem. Não assumir incidência legal em operações específicas sem dados.
5. **Corredores logísticos e competitividade** (segunda etapa). ANTT real, distribuição estimada de receitas/custos, cenários de repasse e tributação. Não apresentar rateio como preço/faturamento oficial. 
6. **Automação/governança** (segunda etapa). Horas economizadas, qualidade, tempo de relatório, custo, benefício recorrente, payback/VPL em hipóteses sintéticas. Valoriza experiência real em TI e projetos; não inventar indicadores internos da MRS.

### Insights e business cases

Insights determinísticos, calculados dos dados: variação histórica, concentração, reconciliação, sensibilidade, VPL, marcos legais. Cada insight: evidência → impacto → ação a investigar → limitação. Sem texto afirmando causalidade ou oportunidade comprovada sem dados internos. Matriz de oportunidades: ICMS, CBS 2027, CAPEX, elegibilidade a créditos, contratos, automação e integração. Priorizar mediante critérios transparentes (impacto, urgência, esforço, risco, confiança), pesos explícitos se houver score; caso contrário ranking qualitativo fundamentado. Nenhuma prioridade é decisão oficial da MRS.

Ficha mínima: título, evidência/fonte, problema, hipótese, impacto financeiro ou qualitativo, fórmula/premissas, risco, requisitos legais, custo e prazo quando estimáveis, áreas envolvidas, dependências, próximas ações, critério de sucesso, grau de confiança. Usar linguagem “avaliar”, “investigar”, “validar”, não “economia assegurada”. Incluir proposta de integração interáreas (levantamento/conciliação → validação fiscal/jurídica → cenário financeiro → decisão gerencial → implementação/monitoramento).

## 9. Requisitos não funcionais (RNF)

| ID | Critério |
|---|---|
| RNF01 | Navegação intuitiva: primeira página comunica diagnóstico e objetivo em poucos minutos. |
| RNF02 | Meta de carregamento inicial até 3 s em condição convencional definida e medida quando possível; otimizar payload; relatar medição real, não prometer universalmente. |
| RNF03 | Desktop e mobile sem overflow horizontal indevido; testar resoluções típicas. |
| RNF04 | Acesso público sem login/instalação e controles acessíveis por teclado; contraste e alternativas textuais quando pertinentes. |
| RNF05 | Chrome/Edge atuais prioritários; Firefox/Safari quando ambiente permitir; declarar cobertura real de testes. |
| RNF06 | Indicadores e simuladores conciliados com fonte/fixtures; testes de denominador zero, ausências, sinais, unidades e filtros. |
| RNF07 | Rastreabilidade e atualização visíveis. |
| RNF08 | Código modular, versionado, README e instruções simples de reprodução. |
| RNF09 | Nenhuma credencial, documento privado, dado pessoal ou informação de candidato desnecessária no repo público; dependências e permissões mínimas. |
| RNF10 | Geração sintética reproduzível com parâmetros/semente quando aplicável; snapshots/metadados e dependências registrados. |
| RNF11 | Identidade MRS-inspirada, sem marca oficial; consistência, legibilidade e português BR. |
| RNF12 | Aplicação estática, sem hibernação de servidor; verificar disponibilidade do link após deploy. |
| RNF13 | Custo zero; sem contratação/trial ou custo implícito de infraestrutura. Work usa a franquia do usuário; reduzir interações e repetições, não prometer consumo zero. |
| RNF14 | Layout e indicadores portáveis para Power BI e síntese PowerPoint; sem conversor nem PPTX obrigatório. |
| RNF15 | Falha de coleta não sobrescreve última base válida; mostrar última atualização e limitações. |

## 10. Roadmap de execução autônoma

Cada etapa deve terminar com evidências, resultado, arquivos alterados, testes, pendências e próximo passo no arquivo `docs/STATUS.md` (ou equivalente). Atualizar roadmap/backlog no repo, sem apagar histórico. As decisões reversíveis são do Work; seguir automaticamente se o gate técnico for satisfeito. Não exigir aprovação intermediária por rotina. Se houver bloqueio externo, trabalhar nas etapas independentes e solicitar somente o mínimo indispensável quando não houver caminho alternativo.

| Etapa | Ações | Entrega / gate de aceitação |
|---|---|---|
| 00 — Retomada | Ler roadmap e prompt; consultar históricos se acessíveis; confirmar ferramenta/repo/ambiente e regras do GitHub Pages; verificar se já existe repo equivalente antes de criar. | Plano curto e status inicial; nenhuma dependência de Power BI. |
| 01 — Prova de fontes | Baixar e inspecionar DFP/ITR/CVM, notas MRS, Excel RI e ANTT; tentar DIRBI/REIDI; verificar período, chaves, campos, unidades, licenças, cobertura e atualidade. | Inventário auditável com resultado efetivo por fonte, amostras, páginas/abas/contas, gaps e fallback. Gate: base financeira/tributária primária confirmada ou escopo reduzido explicitamente. |
| 02 — Repositório e esqueleto | Criar/usar repo `inteligencia-tributaria` após verificar colisão, preservar repositórios existentes; estrutura simples, dependências, .gitignore, tema base, testes e build. | Repo e build local funcionais. Sem segredos ou dados pessoais. |
| 03 — ETL e dados | Implementar coleta reexecutável, cache/snapshots quando permitido, normalização, deduplicação e conciliação; manter dados por granularidade; gerar arquivos de publicação e metadados. | Comando reprodutível, logs, fixtures e relatórios de validação; dados conferidos. |
| 04 — Indicadores e legislação | Consolidar dicionário, fórmulas, fontes e regras; confirmar dispositivos da reforma, mudanças posteriores e elegibilidade dos regimes; revisar inconsistências. | Indicadores testados e notas legais rastreáveis; hipóteses não validadas marcadas como tal. |
| 05 — Interface base | Criar navegação, tema MRS-inspirado, layout responsivo e componentes compartilhados; construir visão executiva e fontes/metodologia primeiro. | Tela funcional com dados reais; usabilidade e contraste; disclaimer. |
| 06 — Diagnóstico e eficiência | Adicionar histórico, créditos, contingências, reconciliação, REIDI e contexto operacional validado; insights determinísticos. | Filtros e gráficos coerentes; sem falsa granularidade nem dupla contagem. |
| 07 — Reforma e cenários | Implementar timeline, temas legais, simuladores prioritários e matriz/business cases. Testar casos extremos, cálculos e restauração de cenário. | Cenários editáveis, premissas visíveis, resultados reproduzíveis; não há previsões apresentadas como fato. |
| 08 — QA integrado | Executar testes Python/JS, lint/build, conciliação de métricas, validação de links, navegação, filtros, simulações; testar desktop/mobile e capturar evidências visuais quando disponível. | Falhas críticas corrigidas, lista de limitações e testes realmente executados; revisão da impressão executiva e portabilidade visual. |
| 09 — Deploy | Configurar GitHub Actions/Pages para site estático, caminho base correto; commit/merge quando autorizado e seguro; verificar execução e URL pública em sessão anônima ou browser sem autenticação. | URL real acessível, assets/links carregando, sem login; verificar mobile, sem erros críticos. Se ferramenta não permitir teste anônimo, declarar e pedir apenas esse teste. |
| 10 — Handoff | README, fontes, dicionário, instruções, roadmap atualizado, evidências, URL, versão e resumo executivo do que foi entregue. Preparar texto sugerido à recrutadora apenas como rascunho, se útil; não enviar. | Entrega única para avaliação do patrocinador; informar o que foi feito, testado, não feito e por quê. |
| 11 — Evolução posterior | Corredores, automação/governança, benchmark de concessionárias, exportações avançadas, predição, conversão/reconstrução BI ou PPTX se solicitados. | Fora do MVP; incorporar só após validar entrega principal e decisão do patrocinador. |

### Estrutura mínima sugerida (adaptável)

```
inteligencia-tributaria/
  README.md
  docs/               # roadmap, status, fontes, dicionário, decisões, testes
  scripts/            # coleta, transformação, validação em Python
  data/               # metadados/snapshots permitidos; sem arquivos grandes ou privados
  public/data/        # CSV/JSON mínimos para o cliente
  src/                # páginas, componentes, cálculos, tema
  tests/              # fixtures/testes analíticos e de interface
  .github/workflows/  # testes, build e deploy; atualização manual se necessário
```

## 11. Política de autonomia e controle de custo

Modelo de colaboração inspirado na experiência do usuário com CDMF: patrocinador define objetivos e avalia resultado; Work pesquisa, constrói, testa, corrige, versiona e publica com ferramentas disponíveis. Não solicitar “pp” por etapa, não transferir tarefas técnicas factíveis (downloads, merges, execução de código, testes, configuração), não pedir cópia de saídas acessíveis, não parar por problema recuperável. Investigar causa, corrigir, reexecutar, registrar evidência. Evitar perguntas cosméticas; decidir conforme roadmap e documentar. Agrupar eventual autorização necessária em uma interação quando possível. O usuário autoriza a criação/publicação do novo projeto demonstrativo no GitHub pessoal dentro deste escopo, sujeito aos mecanismos de confirmação da plataforma; não tocar em CDMF ou outros repos. Não inferir permissões nem contornar controles de acesso. Se faltar autorização do conector ou recurso, pedir apenas o ato indispensável.

Interromper para decisão apenas em: possível custo/contratação; autenticação/consentimento pessoal obrigatório; ação destrutiva/irreversível ou alteração em recursos existentes não autorizada; necessidade de dado privado; mudança material de escopo/objetivo; bloqueio que impossibilite entrega segura e não tenha alternativa razoável. Não prometer execução em background; entregar resultados concretos no modo disponível e deixar ponto de retomada. Não criar automações externas recorrentes sem escopo claro; workflow de build/deploy do projeto e atualização manual são suficientes inicialmente. Não enviar e-mails, publicar em redes sociais nem contatar MRS.

## 12. Definição de pronto e limites

MVP pronto quando: URL pública verificada (ou bloqueio real explicitado); cinco módulos enxutos com funções essenciais; dados oficiais conferidos e fontes navegáveis; cenários interativos e classificados; reforma com regras verificadas; business cases sem falsa precisão; aparência profissional alinhada à MRS; testes relevantes executados; README/status/roadmap atualizados; ausência de custos, segredos ou falsa afiliação. Caso alguma fonte complementar falhe, reduzir dependência sem inventar dados. Se uma entrega essencial não for viável, indicar claramente a lacuna e não chamar o produto de completo.

Fora do escopo inicial: Power BI/PBIX/PBIP, conversor, PPTX, login, banco remoto, SAP/ERP, microsserviços, API de IA, chatbot, ML, dados em tempo real, benchmark amplo, scraping sem autorização, auditoria/parecer fiscal, contato com recrutadora. A qualidade da apresentação decorre das evidências e da decisão de negócio, não do número de tecnologias.


---
## Registro de execução — 27/11/2026

Planejamento original preservado acima. A versão demonstrativa foi implementada e publicada: https://alvarobonifacio1980.github.io/inteligencia-tributaria/ . Estado detalhado em STATUS.md, backlog em BACKLOG.md, inventário em FONTES_STATUS.md e testes em TESTES.md. Etapas 00–10 executadas no escopo validado, com ressalvas de ANTT/DIRBI, histórico inicial reduzido, REIDI/REPORTO sem quantificação atual e reforma como sensibilidade simplificada. Não declarar cobertura integral das fontes/regras pendentes.
