# Inteligência Tributária — Roadmap de evolução V2.1 — consolidado

**Planejamento estratégico e eficiência fiscal**  
**Data:** 27/11/2026 · **Status:** evolução implementada; aceite e limitações em ACEITE_V2.md e TESTES_V2.md  
**Referência:** revisão integral da V2.0, incorporando benchmark institucional, prioridades públicas da área tributária e novas fontes regulatórias; substitui a V2.0 e complementa a V1 para requisitos não conflitantes  
**Pilares:** Diagnosticar · Otimizar · Antecipar

## 1. Objetivo e regras de precedência

Evoluir a aplicação de uma ferramenta de diagnóstico para uma demonstração de planejamento tributário orientada à decisão, adequada à gerência e à alta administração do setor ferroviário. A público avaliador é o primeiro público: deve perceber o propósito, a qualidade e a utilidade em poucos minutos. O gestor deve encontrar análises fundamentadas, cenários comparáveis e propostas de projetos implementáveis.

O estudo é uma iniciativa profissional independente relacionada à demonstração profissional à vaga de Especialista Tributário da Empresa Ferroviária. Não é entrega contratada, auditoria fiscal, previsão da companhia nem produto oficial. A aplicação deve evidenciar capacidade de transformar dados, riscos e mudanças legislativas em análises econômico-financeiras, recomendações e iniciativas multidisciplinares.

**Atenção à divulgação:** a identificação pública será somente “Empresa Ferroviária” ou “Setor ferroviário”. Não mencionar nominalmente a Empresa Ferroviária, a demonstração profissional, público avaliador ou estruturas internas reais nos textos abertos do painel, README, roadmap público, commits, issues e demais materiais de divulgação. Usar áreas funcionais genéricas (Tributário, Finanças, Tecnologia, Suprimentos, Operações, Comercial, Jurídico) apenas como participantes propostos, sem atribuir organograma real. Fontes oficiais devem continuar autênticas, diretas e clicáveis: seus documentos, códigos públicos e links podem identificar a companhia. Isso é generalização editorial, não anonimização dos dados. Não adulterar fontes para ocultar identidade. Este documento de trabalho pode citar a empresa para contextualizar a execução; **não republicá-lo integralmente sem sanitização editorial**. Não reescrever histórico Git para remover referências anteriores sem autorização.

Precedência: orientações mais recentes do patrocinador → este roadmap V2.1 → Roadmap V1 para requisitos não alterados → documentação e código da versão efetivamente publicada → histórico dos chats. Havendo discrepância numérica, prevalece a fonte oficial conciliada, nunca um número preliminar deste documento.

### 1.0. Alterações desta revisão consolidada

A V2.1 substitui integralmente a V2.0 como especificação de evolução, não constitui uma nova aplicação nem exige reiniciar a V2 já em andamento. Conserva as doze etapas, critérios, dados candidatos e correções da revisão anterior. Acrescenta: benchmark de comunicação gerencial 3T26; manifestação pública da gestão tributária de 24/11/2026; descrição pública do case Tax Summit; DIR 2025 e DIP 2027–2029; pagamentos tributários na DFC; tarifas oficiais e simulador tarifário como fontes a inspecionar; planejamento de CAPEX, preços e contratos de longo prazo. A evidência disponível não autoriza concluir quais sistemas, metas, gargalos, processos ou prioridades internas estão efetivamente implantados.

**Escopo e ordem:** correção metodológica primeiro; incorporar dados públicos de alta materialidade e baixo esforço (DIR/DIP, DFC) em seguida; aprofundar decisões comerciais e investimentos mediante cenários transparentes; não criar novas páginas principais. Complementar iniciativas existentes, nunca apresentar a empresa como despreparada. O caminho crítico não depende de obter planilhas tarifárias, dados privados ou integração com ERP. Se o Work já tiver executado parte da V2, verificar e reaproveitar cada entrega aprovada, implementando somente diferenças e correções. 

### 1.1. Restrições permanentes

- R$ 0,00 para infraestrutura, fontes e serviços. Sem trials, cartões ou contratação. Evitar processamento/execuções excessivos; não prometer custo zero de créditos do Work.
- Máxima autonomia e mínimo de interações. Executar etapas e testes sem comandos `pp`; não solicitar ações técnicas que o Work possa fazer.
- Manter Python/Pandas, React/Vite, Apache ECharts, CSV/JSON e GitHub Pages. Não introduzir servidor, banco remoto, API de IA, login, chatbot, ML ou conversor Power BI.
- Manter português BR, identidade azul-escuro/azul/amarelo, tema centralizado, aparência executiva e sem logomarca da empresa. Não redesenhar por completo a V1.
- Gráficos convencionais, cards e tabelas facilmente reconstruíveis no Power BI e sintetizáveis em PowerPoint. Não produzir PBIX/PPTX agora. Sem animações ou recursos visuais exóticos.
- Separar fatos, cálculos, estimativas oficiais, hipóteses, evidência e recomendação. Não prometer redução de tributos ou concluir irregularidade sem validação interna.
- Não enviar mensagens à público avaliador ou à companhia. Não alterar outros repositórios, particularmente CDMF. A publicação da V2 deste painel está no escopo; contato externo não está.

## 2. Referências e linha de base

- Aplicação: https://alvarobonifacio1980.github.io/inteligencia-tributaria/
- Repositório: https://github.com/alvarobonifacio1980/inteligencia-tributaria/
- Referência de planejamento: Roadmap V1 e histórico dos chats de planejamento e implementação no projeto Carreira.
- Arquivos observados na revisão V1: `src/main.jsx`, `src/calculos.mjs`, `src/style.css`, `public/data/painel.json`, `data/base_revisada.json`, `data/conciliacao_cvm.json`, `scripts/preparar_base.py`, `docs/METODOLOGIA.md`, `docs/STATUS.md`, `docs/TESTES.md`, `docs/FONTES_STATUS.md`, `docs/BACKLOG.md`, testes e workflows existentes.

A avaliação anterior atribuiu nota qualitativa de 7,7/10 à V1. Pontos fortes: consistência dos números conferidos, fontes, arquitetura e automação. Lacunas: indicadores de 9M, profundidade dos insights, simulador da reforma, business cases, contexto ferroviário e navegação. A avaliação não corresponde a auditoria fiscal formal. A inspeção visual independente da aplicação publicada e a conciliação integral do ITR de setembro de 2026 ficaram pendentes; os testes de navegador relatados são evidências do Work, a repetir na nova versão.

Estado observado (não presumir que o HEAD permaneceu igual): seis páginas, dois simuladores, dados financeiros anuais 2024/25 e acumulados 9M2025/26, créditos em três datas, reconciliação IR/CS, riscos, fontes clicáveis nos KPIs, modal de adaptação e cascata resumida. ANTT e DIRBI não integradas por falhas na obtenção de arquivos válidos. Portaria REIDI histórica consultada; elegibilidade atual não comprovada. Pipeline não é atualização universal: há números, datas e textos quantitativos fixos em código.

### 2.1. Benchmark institucional e alinhamento estratégico (referências privadas de trabalho)

| Referência pública | URL / localizador | Implicação para a aplicação |
|---|---|---|
| Artigo da gestão tributária, autoria institucional, 24/11/2026 | [Artigo institucional](https://www.mrs.com.br/noticia/reforma-tributaria-o-desafio-agora-e-transformar-a-legislacao-em-decisoes-de-negocio/) | Traduzir regras em decisões sobre preços, contratos, créditos, caixa, dados e ERP; integrar funções de negócio; não usar estatísticas das pesquisas citadas como indicadores da empresa |
| Case anunciado no Tax Summit 2026, apresentação anunciada | [Programação do evento](https://confeb.liveuniversity.com/taxsummit), sessão de preparação para o novo modelo tributário | A descrição do case menciona análise por operação, adequações ao SAP S/4HANA, simulação e rastreabilidade. Não prova estágio, resultados ou arquitetura efetivamente implantada. Propor camada analítica complementar, não substituição de ERP |
| Apresentação de resultados 3T26 | [PDF](https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/b562dfd9-524d-47fc-91a2-ef7558f6dbda), páginas 4, 6, 11, 13, 17 e demais páginas pertinentes | Benchmark visual: indicadores com comparação e leitura gerencial, colunas, linhas, cascatas, rótulos de valor e notas discretas. Reabrir e confirmar padrões antes de replicar |
| Documentos regulatórios | [Portal](https://www.mrs.com.br/sustentabilidade/governanca/documentos-regulatorios/) | DIR, DIP, tarifas e simulador; confirmar competência e versão |
| Estratégia corporativa | [Site institucional](https://www.mrs.com.br/sobre-a-mrs-logistica/estrategia/) | Simplicidade e agilidade decisória, sem reproduzir slogan/marca |
| Relatório de Sustentabilidade 2025 | [PDF](https://www.mrs.com.br/wp-content/uploads/2026/03/Relatorio-de-Sustentabilidade-MRS-2025.pdf) | Benchmark complementar e comparação de escopo dos indicadores |
| Resultados interativos | [RI](https://ri.mrs.com.br/en/information-to-investors/interactive-results/) | Séries e planilhas gerenciais; reconciliar conceitos |
| ANTT — referência externa | [Painéis interativos](https://www.gov.br/antt/pt-br/assuntos/informacoes-estrategicas/paineis_interativos), [investimentos obrigatórios](https://www.gov.br/antt/pt-br/assuntos/ferrovias/fiscalizacao-e-infraestrutura/acompanhamento-dos-investimentos-obrigatorios), [anuário](https://www.gov.br/antt/pt-br/assuntos/ferrovias/anuario-do-setor-ferroviario), [RAPS/RASF](https://www.gov.br/antt/pt-br/assuntos/ferrovias/indicadores-operacionais/indicadores-do-raps-e-do-rasf) | Comparar apresentação, metodologia e cobertura; incorporar apenas dados necessários e conciliados |

O artigo e a programação foram reabertos em 27/11/2026; DIR e DIP conferidos diretamente nos PDFs, inclusive visualmente. A apresentação 3T26 foi inspecionada na pesquisa anterior, mas o link não reabriu nesta revisão: o Work deve recuperá-la pelo RI e validar o benchmark. As planilhas tarifárias foram localizadas, mas o conteúdo e as fórmulas não puderam ser inspecionados nesta revisão. Não foram localizados dashboards internos ou slides completos da palestra. Os padrões de comunicação e oportunidades sugeridos são inferências/propostas, não padrões internos confirmados. Preservar a regra editorial da seção 1: nomes e demonstração profissional apenas nesta especificação privada; fontes oficiais autênticas devem permanecer acessíveis. 

## 3. Sequência e prioridades de execução

| Etapa | Prioridade | Entrega | Dependência |
|---|---|---|---|
| V2-00 | P0 | Linha de base, proteção V1 e testes iniciais | — |
| V2-01 | P0 | Dados e conciliação 9M/ITR, DVA/DFC, DIR/DIP e referências tarifárias | 00 |
| V2-02 | P0 | Modelo de dados, metadados e cálculos dinâmicos | 01 (parcial em paralelo) |
| V2-03 | P1 | Visão executiva e comparabilidade | 01–02 |
| V2-04 | P1 | Diagnóstico, cascatas, compensações e riscos | 01–02 |
| V2-05 | P1 | Eficiência fiscal, contexto ferroviário e planejamento de CAPEX 2027–2029 | 01–02 |
| V2-06 | P0/P1 | Simuladores revisados, CAPEX e sensibilidade comercial | 01–02, 05 |
| V2-07 | P1 | Reforma: matriz, cronograma e ações | 01, 06 |
| V2-08 | P1 | Business cases e carteira estratégica | 04–07 |
| V2-09 | P1 | Navegação, benchmark visual 3T26, fontes, exportação e impressão | 03–08 |
| V2-10 | P0 | Testes integrados, regressão e revisão executiva | 00–09 |
| V2-11 | P0 | Publicação, verificação anônima e entrega | 10 |

P0 = integridade, precisão, segurança e condições de publicação; P1 = valor estratégico ou qualidade de experiência. As etapas são controles internos, não pedidos de autorização. Implementar atividades independentes em paralelo quando conveniente. Uma fonte complementar indisponível não bloqueia o restante; valores correspondentes devem ficar indisponíveis ou fora do painel, com explicação. Não aprovar uma etapa crítica se houver erro material não resolvido.

## 4. V2-00 — Retomar e proteger a versão publicada

1. Ler este documento, o Roadmap V1, o README e os arquivos de status, metodologia e testes atuais. Consultar histórico do projeto Carreira se acessível, sem parar se indisponível.
2. Consultar o HEAD da branch principal, o deploy efetivo e seus workflows. Registrar SHA, URL, data-base, status e estrutura de dados. Identificar alterações posteriores à revisão e preservar decisões já implementadas.
3. Criar branch de trabalho `v2-melhorias` (ou nome equivalente) e referência recuperável da V1, preferencialmente tag/commit conhecido. Não realizar force push, apagar histórico ou derrubar o painel publicado.
4. Executar os testes Python/JS e o build existentes. Capturar, quando houver navegador, o estado das seis páginas em desktop e mobile, incluindo filtros, modal, gráficos, fontes e simuladores. Registrar falhas reais.
5. Consolidar tarefas deste roadmap no backlog do repositório em versão publicável, com estados pendente/em execução/concluída/bloqueada e evidências. Não duplicar requisitos já satisfeitos: confirmar por teste.

**Aceite:** versão anterior recuperável, baseline registrada, testes iniciais conhecidos e nenhuma alteração em produção antes dos gates finais. Se não for possível testar algo, registrar exatamente o que falta.

## 5. V2-01 — Conciliação e ampliação das fontes

### 5.1. Fontes prioritárias

| Documento | Localizador | Uso |
|---|---|---|
| DFP 2025 | DRE p. 37; DVA p. 46; notas 10 p. 63, 25 p. 109, 29 p. 116 e 33 p. 121 (paginação impressa, confirmar) | Resultados, tributos, créditos, compensações, contingências e alíquota |
| ITR 3T2026 | DRE consolidada; nota 9 p. 48–49; nota 27 p. 85; demais notas pertinentes | Números 9M, créditos, riscos e dados recentes |
| CVM DFP/ITR | DRE 3.01, 3.07, 3.08; BPA 1.01.06 e demais contas pertinentes; DVA quando aplicável | Conciliação estruturada independente da extração PDF |
| Release 3T2026 e resultados interativos | DRE gerencial, volumes, investimentos, despesas por natureza, quando disponíveis | Contextualização operacional e calibração, sem misturar conceitos gerenciais e estatutários |
| Legislação e fontes oficiais | EC 132, LC 214 compilada, LC 227, atos RFB/CGIBS, Ministério dos Transportes e CT-e | Reforma, regimes especiais e requisitos de implementação |

Endereços de partida (reutilizar os da V1 quando válidos; confirmar documento e competência):

- DFP: https://api.mziq.com/mzfilemanager/v2/d/e14f1680-635b-4328-8a06-b799b1574b43/acbef322-8f85-850f-ae21-8d531a3467b4?origin=2
- ITR: https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/ed0c4c1c-5cc3-4a74-ac98-e657a4cd7bbf
- Release: https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/a21948c4-c51e-4c70-ba17-cc332fe9741f
- Excel RI: https://filemanager-cdn.mziq.com/published/e14f1680-635b-4328-8a06-b799b1574b43/da20407a-9590-4cd5-865c-a65c0ee52fbc
- CVM DFP: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp
- CVM ITR: https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr
- LC 214: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
- LC 227: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm
- RFB: https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/reforma-tributaria-do-consumo
- REIDI: https://www.gov.br/transportes/pt-br/assuntos/incentivos/reidi
- ANTT: https://dados.antt.gov.br/ ; https://www.gov.br/antt/pt-br/assuntos/ferrovias/dados-de-producao-do-transporte-de-carga-origem-destino
- DIRBI: https://www.gov.br/fazenda/pt-br/assuntos/politica-fiscal/atuacao-spe/plataforma-de-desoneracoes-tributarias

### 5.1.1. Novas fontes de prioridade alta

- DIP 2027–2029: https://www.mrs.com.br/wp-content/uploads/2026/11/DIP-2027-2029.pdf — p. 1, classes, anos, totais e nota explicativa de Outros. Plano oficial publicado, não orçamento interno aprovado ou execução garantida.
- DIR 2025: https://www.mrs.com.br/wp-content/uploads/2026/11/DIR-2025.pdf — p. 1, classes realizadas e notas. Escopo regulatório; verificar equivalência antes de comparar com CAPEX da DFC/RI.
- DFC: release 3T26 p. 16, DFP e ITR — pagamentos de tributos sobre lucro; conciliar rubrica, sinal e valores exatos com CVM DFC e notas. Não confundir despesa, pagamento, compensação e economia.
- Tarifas máximas de referência: https://www.mrs.com.br/wp-content/uploads/2026/07/TARIFAS-DE-REFERENCIA-2026-29.07.2026-1.xlsx
- Simulador tarifário 2026–2027: https://www.mrs.com.br/wp-content/uploads/2026/07/Simulador-Tarifario-2026-2027.xlsx
- Portal regulatório da seção 2.1: conferir condições de uso, data de validade, serviços acessórios e atualizações. A tarifa de referência é limite regulatório, não preço praticado, custo de transporte ou receita individual comprovada. Não pressupor campos, fórmulas ou impostos incluídos antes da leitura das planilhas.

**Procedimento adicional:** baixar arquivos válidos; para XLSX usar Python/openpyxl (se necessário) para listar abas, cabeçalhos, unidades, fórmulas e valores em cache, intervalos nomeados, dependências, células protegidas e possíveis vínculos externos. Não executar macros, não enviar arquivos privados, não usar credenciais de terceiros. Validar exemplos reproduzíveis com fórmulas simples, sem clonar a ferramenta integralmente. Se arquivo inacessível, registrar evidência e fallback para análise comercial normalizada da seção 10.4. Para PDFs DIR/DIP preservar linhas originais, rótulos, versão e nota; não agrupar classes antes de conciliar totais. Para ANTT, pesquisar alternativa oficial e esforço proporcional, sem bloquear o MVP. 

### 5.2. Procedimento de obtenção e conciliação

1. Reaproveitar downloads válidos e scripts existentes. Verificar status HTTP, assinatura de arquivo, tamanho/integridade, período, revisão e licença. PDF exige texto/tabelas e inspeção visual das páginas pertinentes; validar números de página impressa versus índice PDF. CSV/ZIP/XLSX/XLSB devem abrir efetivamente, sem respostas HTML ou downloads truncados.
2. CVM: selecionar companhia por código 017949/CNPJ 01.417.222/0001-77, consolidado, período exato, versão mais recente válida, moeda REAL e escala informada; não agregar linhas de versões diferentes ou períodos trimestral e acumulado. Converter sinais e unidades de modo documentado.
3. Conciliar 9M2025 e 9M2026: lucro antes de IRPJ/CSLL, despesa corrente e diferida, receita bruta/líquida e tributos sobre serviços. Usar DRE e notas do ITR e dados CVM. Conferir equivalência do período acumulado janeiro–setembro; não usar 3T isolado.
4. Revalidar todos os saldos de setembro/2026 da nota 9, componentes, circulante/não circulante e subtotais por UF. Verificar se há outras datas oficiais úteis (por exemplo, setembro/2025); quando não houver, manter datas explícitas sem inventar séries mensais.
5. Extrair DVA, compensações específicas, contingências por classe/tema, volumes transportados e investimentos. Se o ITR trouxer informação mais recente comparável, incorporá-la com data distinta e fonte. Não exigir séries 2022–23 para concluir V2; estender apenas se trivial e conciliado.
6. Buscar ANTT/DIRBI por canal oficial alternativo somente com esforço proporcional. Usar releases para suprir contexto operacional da V2. Não bloquear entrega por ausência dessas bases, não ratear tributos por rotas sem premissas explícitas.
7. Gerar relatório de conciliação por campo com fonte, localizador, valor original, unidade, valor normalizado, diferença, status e justificativa. Divergência além da precisão publicada exige investigação. Preservar último snapshot válido; não publicar dado não conciliado como Real.

### 5.3. Valores de controle e candidatos

Valores abaixo em R$ milhões, exceto indicação contrária. São referências para investigação e testes, **não dados a copiar automaticamente para produção**. Os anuais foram conferidos na avaliação anterior; os demais vêm da base V1, dos releases ou de leituras preliminares e precisam ser confirmados nas fontes. Verificar arredondamentos e versão.

| Métrica | 2024 | 2025 | Observação |
|---|---:|---:|---|
| Receita bruta | 7.484,648 | 8.054,851 | DFP, nota 29 |
| Tributos sobre serviços | 459,675 | 469,793 | Dedução de receita, não carga total |
| Receita líquida | 7.024,973 | 7.585,058 | Bruta menos dedução, conforme nota |
| LAIR | 2.047,741 | 2.152,768 | DRE consolidada |
| IRPJ/CSLL despesa líquida | 632,231 | 597,705 | Corrente + diferida |
| Alíquota efetiva | 30,87% | 27,76% | Calcular a partir de valores exatos |
| Compensações de tese específica de PIS/Cofins | 93,616 | 72,468 | Candidato: nota 10; não recuperação total |
| Perdas possíveis | 643,211 | 935,621 | Candidato: nota 25 |
| Perdas prováveis provisionadas | 142,762 | 151,214 | Candidato: nota 25 |
| Impostos, taxas e contribuições — DVA | aprox. 974,87 | 1.000,469 | Confirmar total e classificação |

DVA 2025 candidata: federal 970,129; estadual 28,897; municipal 1,443. Soma 1.000,469. Volume de transporte 2025 candidato: 213 milhões de toneladas, fonte institucional; verificar unidade, universo, precisão e compatibilidade com receita antes de calcular razões.

| Métrica | 9M2025 | 9M2026 |
|---|---:|---:|
| Receita bruta (V1) | 5.988,509 | 5.964,721 |
| Tributos sobre serviços (V1) | 351,978 | 351,189 |
| Receita líquida (V1) | 5.636,531 | 5.613,532 |
| LAIR (release, arredondado) | ~1.690 | ~1.295 |
| IRPJ/CSLL (release, arredondado) | ~464 | ~429 |
| Alíquota efetiva aproximada | ~27,5% | ~33,1% |

A diferença de aproximadamente +5,7 p.p. é um sinal para investigação, não uma conclusão de ineficiência. Buscar a reconciliação da nota tributária do ITR; se ela não explicar a variação, indicar que as causas requerem investigação, sem inventar componentes.

| Créditos (estoques) | 31/12/2024 | 31/12/2025 | 30/09/2026 |
|---|---:|---:|---:|
| ICMS | 188,852 | 222,207 | 277,596 |
| PIS/Cofins | 161,825 | 96,173 | 129,005 |
| IR retido | 115,312 | 68,792 | 146,391 |
| Outros | 0,671 | 0,779 | 0,772 |
| Total | 466,660 | 387,951 | 553,764 |
| Circulante | 325,341 | 266,787 | 379,308 |
| Não circulante | 141,319 | 121,164 | 174,456 |

ICMS circulante RJ/SP (V1): RJ 84,367 → 103,994; SP 69,278 → 99,684. Subtotal atual 203,678. MG não detalhado: não atribuir a diferença do saldo total a MG, nem representar zero.

### 5.4. Valores de controle adicionais — DIR, DIP e DFC

DIR e DIP reabertos e conferidos na fonte oficial em 27/11/2026, página única de cada documento. Valores **em reais**, não em milhares. Totais reconciliados por soma aritmética nesta revisão. Work deve revalidar a versão e registrar a extração, preservando os inteiros originais.

| Classe DIP — investimentos previstos | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Via Permanente | 1.086.252.267 | 1.975.822.012 | 1.946.976.735 |
| Material Rodante | 251.522.294 | 256.512.139 | 254.628.870 |
| Infraestrutura Predial | 71.507.739 | 72.975.830 | 72.467.249 |
| Meio Ambiente | — | — | — |
| Outros | 890.125.414 | 543.851.504 | 286.882.161 |
| Total oficial | 2.299.407.714 | 2.849.161.485 | 2.560.955.015 |

Total do horizonte: R$ 7.709.524.214. Traços da fonte não são dados faltantes a imputar: conservar representação original e explicitar que as classes numéricas conciliam o total. Para gráfico, não gerar série fictícia para Meio Ambiente. A nota de Outros descreve investimentos heterogêneos, incluindo oficinas, energia, controle de circulação, edificações e intervenções na malha. Não inferir elegibilidade tributária pela classe agregada.

| Classe DIR — investimentos realizados 2025 | R$ |
|---|---:|
| Via Permanente Ampliação | 829.795.735 |
| Via Permanente Existente | 1.286.433.958 |
| Material Rodante Novo | 481.606.376 |
| Material Rodante Existente | 368.855.334 |
| Telecomunicações | 4.810.491 |
| Oficinas | 1.850.564 |
| Informatização | 89.309.602 |
| Sinalização | 240.426.567 |
| Edificações | 5.494.032 |
| Meio ambiente | 0 |
| Outros | 41.009.658 |
| Total oficial | 3.349.592.317 |

Se agrupar classes pequenas para leitura, manter o detalhe em tabela e modal Adaptado; não substituir “Outros” oficial por categoria agregada sem rótulo distinto. DIR 2025 não é a linha de base de execução do DIP 2027–29: períodos diferentes, classes com diferentes níveis de detalhamento. Não medir percentual de execução do plano comparando estes dois conjuntos. Eventual análise de perfil deve usar categorias compatíveis documentadas.

**DFC — candidato ainda a conciliar:** desembolsos na rubrica de tributos sobre lucro de aproximadamente R$ 195 mi em 9M2025 e R$ 19 mi em 9M2026, conforme leitura anterior do release 3T26 p. 16. Diferença aproximada de R$ 176 mi em magnitude positiva. Extrair valores exatos do ITR/DFC antes de promover a indicador Real, verificar sinais, rubrica e comparação equivalente. Não concluir causa, economia ou compensação sem evidência documental. DVA: verificar diferença em relação ao relatório de sustentabilidade (escopo, conceito, período e arredondamento); manter DVA estatutária quando essa for a fonte escolhida. Não misturar valores sem conciliar.

**Aceite:** indicadores críticos do ITR e alíquota 9M conciliados, ou indisponibilidade explicitamente demonstrada; dados novos apenas quando fonte validada; relatório de conciliação atualizado. Se a fonte 9M exata estiver inacessível, valor arredondado do release só poderá aparecer com precisão e natureza adequadas, sem substituir silenciosamente DRE estatutária. Dados da V1 não devem regredir.

## 6. V2-02 — Modelo analítico, metadados e automação

1. Preservar arquitetura estática e contratos atuais; estender JSON com conjuntos separados: financeiro, DVA, DFC/pagamentos, créditos, compensações, contingências, operações, CAPEX realizado (DIR), CAPEX previsto (DIP por ano/classe/versão), tarifas de referência (se validadas), legislação e premissas. Cada fato preserva granularidade, natureza e unidade; separar horizonte de planejamento de data de publicação. Evitar juntar granularidades incompatíveis. Pode manter estrutura simples de arrays/objetos, sem banco ou camada genérica desnecessária.
2. Centralizar IDs de métricas, unidade, natureza, fonte, localizador, período/data de saldo, escopo, fórmula, transformação, premissas, limites e versão/data de revisão. Manter valor bruto e unidade original quando necessário para rastreabilidade. Fonte oficial de estimativa: indicar que o documento é real, mas o valor é projetado, não realizado.
3. Eliminar números, datas e resultados quantitativos duplicados de `src/main.jsx`: datas de saldo, subtotais, reconciliação, insights, rótulos percentuais, títulos de período e rodapé de atualização devem derivar dos dados. Premissas default em configuração central, não espalhadas. Textos legislativos podem ser estáticos versionados, com fonte e revisão.
4. Reusar funções em `src/calculos.mjs` ou módulos pequenos por domínio; React apresenta dados. Formatação pt-BR sem arredondar antes dos cálculos. Python extrai, valida e gera snapshot; JS filtra, agrega e simula. Adicionar fixtures de referência comuns quando ambos calcularem a mesma métrica.
5. Tratar nulo/ausente como “Não disponível”, não zero. Denominador zero/negativo em indicador que não o admite → não aplicável. Exibir diferença absoluta, percentual ou p.p. de acordo com o tipo. Não somar saldos em datas diferentes nem tributos da DVA com despesa DRE.
6. Verificar scripts: `preparar_base.py`, `coletar.py`, `extrair.py`, `cvm.py` e publicação do JSON. Usar valores extraídos e revisados em vez de constantes para o que for suportado; documentar o que ainda requer mapeamento humano. Validação atômica e proteção do último snapshot. Workflow manual de coleta/revisão e deploy após aprovação dos testes; sem agendamento frequente ou nova infraestrutura.
7. Preservar modal de Adaptado; acrescentar explicação equivalente para Híbrido e Sintético. Classificar cada resultado de acordo com o que efetivamente alimenta o cálculo. Conversão de unidade sem mudança de significado não transforma um valor real em estimativa. Ex.: valor monetário de tributos Real; razão tributos/receita Adaptado, com link explicativo. Não esconder origem quando misturar naturezas.

**Aceite:** alteração controlada de um valor/data em fixture atualiza todos os elementos derivados sem editar JSX; fontes clicáveis e modais reproduzem cálculo; ausência não vira zero; snapshot inválido não substitui o válido. Build e testes existentes e novos aprovados.

## 7. V2-03 — Visão executiva: dados recentes e decisões

1. Após conciliação, iniciar em 9M2026, com opção anual 2025/2024 e comparação 9M2025/9M2026. Mostrar claramente duas referências: “Resultado financeiro — período selecionado” e “Posição patrimonial — data do saldo”. Não usar filtro financeiro para alterar estoque sem base correspondente. Se não houver comparação anterior equivalente, não inventar variação.
2. Organizar 4–6 KPIs principais: receita líquida, tributos sobre serviços (valor e razão sobre receita bruta), alíquota efetiva IRPJ/CSLL, tributos a recuperar e, conforme espaço, DVA ou contingências. Para DVA anual, deixar 2025 explícito mesmo na visão de 9M; preferir deslocar para diagnóstico se a mistura de períodos prejudicar clareza. Cada card de valor precisa de fonte clicável e data; indicadores derivados precisam de modal. Exibir variação absoluta/percentual e, em alíquotas, pontos percentuais. Sinal de aumento não deve automaticamente significar melhora/piora.
3. Substituir comparação receita/tributos na mesma escala por dois pequenos gráficos alinhados, ou gráfico de tributos sobre serviços e razão em painel separado com escalas explícitas. Não usar dois eixos se confundirem o visitante. Manter comparação anual/anual ou 9M/9M. Exibir unidades e rótulos.
4. Melhorar composição de créditos: total ao centro da rosca ou título, legenda por tributo com valor e participação, data do saldo, tooltip e tabela/descrição acessível. Evitar rótulo sobreposto na parcela “Outros”.
5. Exibir até três insights em destaque: variação da alíquota efetiva, maior componente da variação de créditos, marco de reforma/ação estratégica. Gerar evidência → relevância → próxima ação → limite. Se optar por outro insight, documentar motivo. Links levam diretamente à análise pertinente, não apenas ao topo de página genérica.
6. Reduzir espaço da faixa de abertura, cabeçalho e textos repetidos se impedirem leitura dos cards. Priorizar título, contexto, métricas e gráficos visíveis rapidamente em desktop 1366×768. Preservar boa leitura em celular.

7. Aplicar o padrão de apresentação gerencial 3T26 da seção 2.1: valor, comparação equivalente e comentário de uma linha. Usar evidência verificável para explicar a variação; na ausência de causa comprovada, escrever “principal contribuição observada” ou “investigar”, sem inferir causalidade. Incluir acesso contextual a resultado, patrimônio e caixa (seção 8.6), e a CAPEX futuro/contratos, sem acrescentar mais cards do que o limite definido. Mostrar o horizonte 2027–29 como planejamento, nunca misturar com a posição realizada de 2026.


**Aceite:** gerente identifica o período e três mensagens-chave sem tutorial; filtro e comparações corretos; card de alíquota 9M utiliza valor validado ou informa limitação; nenhuma leitura como carga total ou caixa disponível. Layout com hierarquia clara, sem poluição visual.

## 8. V2-04 — Diagnóstico tributário aprofundado

### 8.1. Cascata dos créditos

Implementar gráfico de ponte entre estoques inicial e final, com opções de pares disponíveis (default dez/2025–set/2026). Usar componentes: ICMS, PIS/Cofins, IR retido e Outros. Variação = saldo final − inicial. Participação na variação = variação do componente / variação total quando não nula; explicar que parcelas podem ser negativas ou superiores a 100% em movimentos compensatórios. Não confundir participação no saldo com contribuição ao crescimento.

Valores de controle da V1, sujeitos à conciliação: inicial 387,951; ICMS +55,389; PIS/Cofins +32,832; IR retido +77,599; Outros −0,007; final 553,764. Aumento +165,813 (42,74% aproximadamente). IR retido explica aproximadamente 46,8% do aumento; ICMS é maior saldo atual. Incluir Outros na conta e tooltip, mesmo se barra quase invisível. Barras intermediárias flutuantes com sinal, inicial/final ancorados em zero, conectores e valores em R$ mi. Não escrever variação fixa no JSX. Filtro de tributo: se a cascata for filtrável, ajustar saldos inicial/final ao mesmo universo; preferir total completo por padrão.

### 8.2. Reconciliação IRPJ/CSLL

Preservar cascata já implementada e permitir detalhamento da nota 33. Resumo: nominal 731,941; ajustes líquidos −134,236; efetivo 597,705. Detalhamento candidato em R$ mi: exclusão ICMS da base IR/CS −86,501; incentivos −51,687; demais ajustes líquidos +3,952 (validar descrição e soma das rubricas). Mostrar todos os componentes em tabela sob demanda. Nominal 34% e efetiva calculada ~27,76%. Diferença em p.p. calculada, não hardcoded. Se existir conciliação equivalente de 9M, apresentar separadamente, sem aplicar ajustes anuais ao período parcial.

**Teste visual e lógico:** quedas e aumentos com sinais corretos; ajuste negativo não aparece como imposto adicional; barras final/inicial partem de zero; total final igual ao nominal mais ajustes. Gerar a cascata de forma genérica para ambos os sinais e validar ordem das categorias.

### 8.3. DVA — impostos, taxas e contribuições

Adicionar comparação anual e composição federal/estadual/municipal, a partir da DVA consolidada. Preferir barras horizontais com valores e participações; mostrar categorias pequenas sem exagerar escala. Distinguir conceito de distribuição de valor adicionado de despesa de IR/CS, deduções da receita e recolhimentos de caixa. Nunca somar esses indicadores para criar uma “carga fiscal total”.

### 8.4. Compensações tributárias realizadas

Extrair valores por exercício e natureza específica divulgada. Para tese de exclusão de ICMS da base de PIS/Cofins, candidatos 93,616 (2024) e 72,468 (2025). Exibir dois períodos, variação e total somente quando fluxos forem não sobrepostos e de mesma natureza. Explicar queda sem atribuir causa não demonstrada. Não chamar compensação histórica de economia nova descoberta. Se houver dados 2026 comparáveis, adicionar com período equivalente.

### 8.5. Contingências e riscos

Apresentar possível e provável/provisionado em barras empilhadas ou agrupadas, com total e data. Dados candidatos: exposição 2024 = 643,211 + 142,762 = 785,973; 2025 = 935,621 + 151,214 = 1.086,835; variação ~38,3%. Verificar se rubricas são mutuamente exclusivas e se a provisão já está no total. Não somar depósitos judiciais à exposição nem deduzi-los automaticamente. Incluir número de processos somente com classe e universo explícitos (V1: 194 totais, 26 recuperação, 168 riscos; candidato: 9 prováveis em 2025, confirmar). Se notas permitirem, destacar temas de materialidade com valores; caso contrário, lista qualitativa sem ranking monetário inventado. Explorar temas ferroviários: créditos ICMS/PIS/Cofins, arrendamentos, tráfego mútuo, direito de passagem, IPTU e outros conforme documento.

Manter ICMS por UF como subtotal circulante divulgado RJ/SP, com variação e fonte; MG não detalhado. Não gerar mapa de cobertura incompleta que sugira distribuição integral.

### 8.6. Resultado, patrimônio e caixa — três perspectivas distintas

- Resultado: despesa IRPJ/CSLL corrente + diferida e alíquota efetiva (DRE).
- Patrimônio: estoques de tributos a recuperar e, quando divulgadas e conciliadas, obrigações tributárias, com datas e classificação circulante/não circulante.
- Caixa: pagamentos de tributos sobre lucro na DFC e compensações específicas reconhecidas na nota, sem somá-los automaticamente.

Criar bloco compacto com comparação de pagamentos 9M/9M e leitura gerencial. Apresentar saídas em magnitude positiva se explicitado; manter sinal original na base. Exibir diferença e variação percentual com base comparável, sem transformar redução de desembolso em redução de despesa ou economia fiscal. Se causa divulgada for encontrada, citar e explicar; se não, recomendar conciliação entre DRE, DFC, créditos e obrigações. Não exigir uma ponte completa de fluxo de caixa se faltarem componentes. DVA em bloco separado, com escopo declarado e divergência com sustentabilidade documentada. Cada visual com fonte própria e modal Adaptado para cálculo ou inversão de sinal. Não somar as três perspectivas. Critério específico: comparação de caixa conciliada e reproduzível, ou indisponibilidade explícita com alternativa válida.

**Aceite da etapa:** DVA, compensações, contingências e cascatas conciliados; diferenças, escopo e natureza acessíveis; diagnóstico contém no máximo 2–3 gráficos centrais por bloco visível, com detalhes recolhíveis ou subabas simples. Sem duplicação de gráficos na visão executiva por mera decoração.

## 9. V2-05 — Eficiência fiscal e contexto ferroviário

1. Incluir indicadores operacionais oficiais dos releases/Excel RI: volume transportado (TU ou equivalente divulgado), investimentos realizados e composição de carga quando disponível. Selecionar apenas 2–3 métricas de maior utilidade. Manter período e escopo compatíveis com os dados contábeis; não comparar 9M com ano inteiro.
2. Se dados permitirem, calcular receita líquida de serviços por tonelada (R$/t) = receita em R$ / toneladas; tributos sobre serviços por tonelada = dedução em R$ / toneladas. Identificar como intensidade média agregada, não tarifa de frete ou imposto por prestação. Para valores em milhões de reais e milhões de toneladas, a razão direta produz R$/t; verificar unidades. Não inferir causalidade entre volume e tributo. Se universos não forem compatíveis, mostrar métricas separadas.
3. Conectar gestão dos créditos às compensações divulgadas e ao perfil circulante/não circulante. Apresentar evidências, perguntas de investigação, alternativas e critérios de sucesso, sem afirmar problemas internos ou saldos imediatamente realizáveis.
4. CAPEX e regimes especiais: atualizar Portaria MT 779/2023 e conferir atos posteriores, inclusive Portaria 841/2024. Valores históricos candidatos: investimento estimado R$ 8.732,178 mi e suspensões estimadas R$ 807,726 mi. Informar data, condição e natureza de estimativa oficial, não realização. Se houver dados DIRBI válidos, verificar CNPJ/benefício/período e risco de sobreposição antes de utilizar.
5. Se não houver comprovação de elegibilidade, manter REIDI/REPORTO qualitativo e incluir roteiro de validação por projeto/bem, habilitação, prazo, destinação, documentos e efeitos de caixa. Não aplicar percentuais genéricos ao CAPEX inteiro, não somar regimes sobre mesma aquisição. Simulação quantitativa só se dados e regras suficientes; caso contrário, backlog.

### 9.1. Planejamento tributário dos investimentos previstos — entrega prioritária

1. Importar DIR 2025 e DIP 2027–29 com valores originais, fonte e notas (seção 5.4). Calcular totais, participação por classe e ano, concentração de material rodante/via permanente e distribuição do plano. Apresentar realizado separado de previsto. Se necessário, usar uma tabela detalhada e um gráfico empilhado anual, com totais acima das colunas; não adicionar módulo principal.
2. Mostrar R$ 7,71 bi previstos e R$ 3,35 bi realizados em 2025 com datas explícitas; não tratá-los como comparação de desempenho ou valores de benefício. Incluir contexto do 9M CAPEX de RI somente após conciliação do escopo (recorrente/outros e crescimento/competitividade; candidatos 9M25 1.228 + 1.355 mi, 9M26 1.248 + 795 mi, validar números/arredondamentos na apresentação). Não usar esses números para preencher lacunas do DIR/DIP.
3. Relacionar ano e classe a pontos de investigação de REIDI/REPORTO, bens de capital, créditos e fluxo de caixa. Para regimes, validar legislação vigente, habilitação, projeto, aquisição, destinação e atos posteriores. A classe de investimento não comprova enquadramento.
4. Ligar ao simulador 10.3, à matriz da reforma e ao BC03, permitindo partir de uma classe/ano real. Manter todas as escolhas e premissas claramente identificadas. Não prometer economia nem comparar ano cheio com 9M.
5. Registrar perguntas gerenciais: quais classes concentram investimentos? em que etapas da reforma ocorrem? quais aquisições merecem avaliação jurídica e fiscal antecipada? qual a sensibilidade ao prazo de recuperação? Indicar equipes funcionais genéricas e decisões necessárias.

**Aceite adicional:** DIR/DIP conciliados em reais com totais oficiais, gráfico e tabela coerentes, previsão oficial distinguida de realizado e cenário híbrido. O gestor consegue selecionar ano/classe e avaliar sensibilidade de caixa sem pressupor regime especial. Se documento atualizado divergir, prevalece fonte vigente e registrar versão. 

**Aceite:** vínculo explícito entre indicadores ferroviários, tributação e decisão; pelo menos uma análise operacional real validada ou declaração de indisponibilidade; oportunidade de CAPEX com fonte e limites; ANTT/DIRBI não travam a versão se houver alternativas.

## 10. V2-06 — Simuladores: precisão, cenários e comunicação

### 10.1. Realização de créditos

Preservar função `credito` e modelo de realização única. VP = C/(1+r)^(m/12); benefício líquido incremental = VP proposto − VP atual − custo inicial. Taxa anual em fração, meses inteiros, valores em R$ mi. Não confundir custo de capital com juros do crédito; sem atualização monetária, pagamentos parciais ou recorrentes no modelo básico. Custos não devem ser confundidos com principal.

- Criar presets conservador, intermediário e otimizado com mesma base comparável: principal R$ 50 mi, prazo atual 24 meses, taxa 12% a.a., custo inicial R$ 0,5 mi; prazos propostos 18/12/6 meses. Calcular na execução (benefícios líquidos aproximadamente R$ 1,82 / 4,28 / 6,89 mi). Esses nomes descrevem premissas, não probabilidades de sucesso.
- Mostrar gráfico comparativo de benefícios líquidos, incluindo negativos com eixo zero; exibir VP atual/proposto, diferença bruta, custo, benefício líquido, antecipação em meses. Incluir texto interpretativo e limitação. Se custo supera benefício, recomendar reavaliar premissas, não apagar resultado negativo.
- Preservar opção de usar 10% do saldo público de ICMS (aprox. R$ 27,760 mi se saldo confirmado). Permitir percentual editável simples se útil. Fração elegível sempre hipotética. Marcar Híbrido enquanto vinculada ao dado real, Sintético quando principal substituído por hipótese manual; explicar origem e transformação. Reset restaura valores e natureza.
- Evitar comparação enganosa se cenários tiverem bases diferentes. Prazos iguais ou taxa zero implicam benefício bruto zero e líquido negativo do custo. Não usar payback se não houver fluxo de caixa adequado.

### 10.2. Reforma tributária — corrigir interpretação e modelo

O simulador atual pondera regime pleno por fração de transição e compara carga líquida atual hipotética, receita pública e custos hipotéticos. A V1, com receita 7.585,058, custos 4.000, elegibilidade 60%, carga atual 8%, CBS 9%, IBS 18%, repasse 50%, prazo 3 meses e custo de capital 12% a.a., gera efeito negativo próximo de R$ 415 mi no regime pleno. Isso não é previsão da empresa; não publicar esse número como impacto esperado.

**Estratégia KISS prioritária:** comparar regime atual de referência versus regime pleno hipotético (2033), separando componentes e mantendo cronograma legal em seção própria. Retirar ou desabilitar seleção de anos intermediários no cálculo se não for possível representar cada tributo com bases e regras consistentes. Não manter interpolação simplificada com aparência de apuração legal. Só implementar transição quantitativa anual se houver metodologia explícita, componente federal/estadual separado e fontes suficientes, sem ampliar desnecessariamente o prazo.

Passos:

1. Buscar despesas por natureza na DFP/ITR, notas e Excel RI. Reconciliar com conceitos contábeis e separar grupos potencialmente creditáveis, não creditáveis e indeterminados. Não assumir que uma categoria inteira é legalmente elegível. Custos reais de referência + frações hipotéticas = Híbrido; se não houver base compatível, manter valores sintéticos e explicar. A receita líquida real pode servir como referência econômica de base por fora, não como base fiscal comprovada.
2. Premissas editáveis e agrupadas: escala econômica (receita, custos por grupo ou total); carga líquida atual hipotética (não usar automaticamente dedução DRE); taxas CBS/IBS plenas hipotéticas; fração de custos com crédito; tratamento comercial; prazo/custo de capital. Diferenciar regras legais vigentes de taxas hipotéticas. Informar data de revisão das fontes e restaurar defaults.
3. Modelo pleno simplificado: débito = base de receita × taxa; crédito potencial = custos elegíveis × taxa (se taxas uniformes forem hipótese explícita); saldo líquido = débito − crédito; base atual hipotética = receita × taxa líquida atual. Separar CBS/IBS no detalhamento, sem alegar apuração efetiva. Se crédito > débito, mostrar saldo credor potencial; não registrar automaticamente como caixa ou benefício realizado. Tratar custo de prazo sobre créditos efetivamente realizáveis no modelo, com hipótese de realização explícita, sem dupla contagem.
4. Definir convenção de sinal: diferencial tributário positivo = maior encargo do novo cenário; contribuição comercial positiva = compensação de parte desse encargo via preço, sob hipótese de volume constante; se diferencial negativo, eventual redução de preço/compartilhamento de ganho tem sinal oposto. Repasse como ajuste econômico simplificado, não recalcular incidência ou demanda sem modelo explícito. Efeito líquido ilustrativo = compensação comercial − diferencial − custo financeiro de prazo, quando as premissas forem compatíveis. Caso contrário, apresentar componentes separadamente, sem total agregado. Não chamar efeito a VP de fluxo de caixa anual, EBITDA ou lucro; declarar horizonte e diferença entre grandezas.
5. Criar comparativo visual: tributo líquido atual hipotético vs pleno; ponte de impacto tributário, comercial e financeiro, se agregáveis sob a mesma base; sensibilidade a crédito/repasse com 3 cenários fixos e comparáveis (não escolher premissas para produzir economia atraente). Explicar quais variáveis dominam a diferença. Mostrar resultados negativos, zero e positivos com cor + texto, não apenas cor.
6. Metadados por premissa: origem da receita/custos, classificação, unidade e fórmula. Se todos os valores de referência forem substituídos por hipóteses, classificação Sintético; se pelo menos um dado público permanecer vinculado, Híbrido. Não manter fonte do valor original como se justificasse valor manual. Incluir aviso curto junto ao resultado: “Sensibilidade econômica hipotética. Não é previsão nem apuração fiscal.” Detalhar limitações no modal/expansível.
7. Manter CAPEX e regimes especiais fora deste cálculo agregado para evitar dupla contagem; usar o simulador independente 10.3. Acrescentar sensibilidade comercial normalizada da seção 10.4, reaproveitando funções/premissas. Não introduzir ML, previsão de demanda ou apuração fiscal por rota.

**Aceite:** fórmulas documentadas; comparação econômica coerente; nenhum valor hipotético apresentado como impacto real; cenários reproduzíveis, reset correto, resultados negativos interpretados, sem crédito excedente automaticamente convertido em caixa. Se modelagem plena ainda não sustentar um agregado econômico confiável, entregar comparação de componentes sem total líquido. Não omitir essa decisão do relatório.

### 10.3. Simulador de CAPEX previsto e efeito de caixa — escopo delimitado

Aproveitar DIP por ano/classe como escala real do investimento, não como base fiscal comprovada. Proposta KISS: avaliar isoladamente o valor presente do custo de antecipar um desembolso tributário recuperável. Não modelar incentivo definitivo sem validação de elegibilidade. Incluir na página de eficiência ou cenários, com link direto, sem novo módulo principal.

- Entradas: ano/classe do DIP (valor publicado, edição bloqueada enquanto ligado à fonte), fração hipotética do investimento que constitui base econômica sem tributos, taxa hipotética incidente, fração hipoteticamente recuperável, prazo de realização (meses), custo de capital anual e eventual custo de implementação. Opcional substituir base por valor manual com mudança de origem. Explicar que o valor do DIP pode incluir componentes não tributáveis e que a base sem tributos resulta de hipótese, não de extração fiscal. Não adicionar automaticamente tributo ao total oficial.
- Fórmula básica: B = investimento de referência × fração de base (0–1); T = B × taxa hipotética (0–1); R = T × fração recuperável; VP(R) = R/(1+r)^(m/12); custo financeiro do prazo = R − VP(R); parcela não recuperável = T − R, se essa premissa estiver explicitada. Valores em unidade única. Resultado não é cálculo de IBS/CBS devido. Não somar parcela não recuperável a um benefício de regime nem a crédito já reconhecido.
- Comparar cenário de referência com prazo alternativo ou suspensão hipotética **somente quando a parcela comparada tiver tratamento econômico equivalente**. Para antecipação do crédito, ganho incremental bruto = VP(R no prazo proposto) − VP(R no prazo atual), líquido após custo incremental. Não presumir suspensão/isenção automática, nem chamar T de economia. Se elegibilidade de REIDI/REPORTO não confirmada, mostrar apenas uma comparação financeira de prazo com indicação de que regimes são tema para investigação. Quantificação de regimes reais fica bloqueada até validação documental.
- Três presets com mesma base e taxa, variando prazo/percentual de recuperação de forma transparente; identificar mudança de premissas, não cenários probabilísticos. Resultado negativo ou nulo também deve aparecer. Gráfico simples de colunas e detalhe da fórmula. Fonte do DIP clicável e modal Híbrido explicando transformação. Se base manual, classificação Sintético se não restar referência pública efetivamente usada.
- Teste: base 100 mi, fração base 50%, taxa 10%, fração recuperável 80%, 12 meses, r=10% → B=50, T=5, R=4, VP≈3,636364, custo do prazo≈0,363636, não recuperável=1 (R$ mi). Prazo zero → custo zero; recuperação zero → custo financeiro zero; taxa zero → todos os valores tributários zero. Testar limites e sinais, classificação da origem, reset e seleção de ano/classe. Não confundir custo de prazo com total de imposto.

**Aceite:** análise híbrida reproduzível, hipótese de base visível, valores negativos preservados, ausência de promessa de incentivo ou economia. Caso não haja condição de validar um cenário específico de regime, entregar o modelo de prazo genérico acima e a agenda qualitativa, sem ampliar a aplicação.

### 10.4. Sensibilidade de contratos e preços — ponte com a reforma

O artigo institucional destaca contratos que atravessam diferentes fases da transição; a descrição do case menciona impactos por operação. Transformar essa motivação em análise comercial simples e explícita, sem simular contratos reais.

1. Implementar como subseção compacta do simulador da reforma, reaproveitando as premissas e funções existentes. Escolher contrato hipotético de preço/base anual e volume constante (ou normalizar para R$ 100 de receita comparável). Informar vigência inicial/final e cruzamento dos marcos 2027, 2029 e 2033 em timeline qualitativa, sem interpolar alíquotas legais. Não implementar motor de apuração anual sem fontes suficientes.
2. Comparar carga líquida atual hipotética e cenário pleno hipotético; diferencial Δ = novo − referência, com mesma base econômica. Testar repasse 0%, 50% e 100% e eventual compartilhamento de redução. Para Δ positivo, compensação comercial simplificada = Δ×p; pressão econômica residual = Δ×(1−p); para Δ negativo, sinal negativo representa redução potencial do encargo e compartilhamento diminui o benefício retido. Não tratar como reajuste contratual permitido, preço final tributado, margem/EBITDA real ou previsão de demanda. Se mostrar margem ilustrativa, usar receita e custos comparáveis, fórmula e base explícitas; caso contrário, limitar a diferença em R$ e % da receita de referência. Não somar ao resultado agregado do simulador de reforma: é sensibilidade alternativa.
3. Usar planilha tarifária oficial **somente se** sua unidade e fórmula forem verificadas. Inspecionar se tarifa é por tonelada, distância ou outra unidade e se inclui tributos/serviços acessórios. Escolher exemplo hipotético de operação compatível com a fonte e mostrar teto de referência, quantidade e demais parâmetros. Não estimar preço praticado, faturamento, tributo de rota ou contrato existente; se a fórmula não for reproduzível, manter o exemplo normalizado e o link para referência tarifária. Não condicionar a entrega à planilha.
4. Apresentar comparativo de três alternativas de repasse, tabela de implicações para contrato e ações sugeridas: mapear cláusulas tributárias, revisão de preço, responsabilidades, validade, negociação, efeito sobre crédito de cliente e documentação. Vincular Comercial, Jurídico, Suprimentos, Finanças, Tributário e Tecnologia como funções propostas. Indicar que contratos e decisões reais não estão disponíveis.
5. Testes: referência 8, novo 12 por R$ 100 comparável → Δ=4; repasse 0/50/100% → pressão residual 4/2/0. Referência 12, novo 8 → Δ=−4; compartilhamento 50% → residual −2. Verificar zero, valores inválidos, origem e não duplicação de resultados. Não usar gráfico que sugira uma previsão temporal.

**Aceite:** comparação comercial inteligível em uma tela, fonte/premissas e limitações próximas aos resultados, agenda contratual vinculada à reforma, nenhuma tarifa tratada como preço efetivo. Entregar exemplo normalizado mesmo se as planilhas falharem. 

## 11. V2-07 — Reforma tributária: matriz de impactos e agenda de preparação

Preservar timeline 2026–2033, verificar EC 132/2023, LC 214 compilada, LC 227/2026 e regulamentação atual. Conferir cronograma, testes de 2026 e condições de dispensa, CBS e fim de PIS/Cofins em 2027, transição 2029–32 e regime definitivo 2033. Não aplicar tratamento de passageiros ao transporte ferroviário de cargas.

Construir matriz com colunas Tema | mudança/regra | impacto a investigar | ação proposta | marco temporal | equipes funcionais | fonte/limite. Usar resumo compacto e detalhe sob demanda. Temas prioritários:

| Tema | Ação de planejamento proposta |
|---|---|
| CBS/IBS e créditos | Mapear aquisições, documentos, extinção de débitos e regras de apropriação |
| Créditos de ICMS | Conciliar origem, homologação e alternativas de realização durante transição |
| Tributação no destino | Verificar local de entrega indicado no documento fiscal e efeitos contratuais |
| CAPEX, REIDI e REPORTO | Cruzar calendário do DIP 2027–29 com marcos legais; validar projetos, bens elegíveis, habilitação, destinação e prazos; link ao cenário 10.3 |
| Contratos e preços | Mapear contratos de longa duração que cruzam marcos 2027/2029/2033, bases por dentro/por fora, responsabilidades, repasse e efeitos comerciais; link ao cenário 10.4 |
| Capital de giro | Investigar prazos de creditamento, ressarcimento e pagamento |
| CT-e, cadastros e tecnologia | Mapear interfaces de ERP, documentos, regras, cadastros, conciliação e homologação como arquitetura proposta; sem integração SAP real ou alegação sobre prontidão atual |
| Governança e conformidade | Definir responsáveis, evidências, homologação e monitoramento |

Artigos candidatos para verificação: LC 214 art. 11, VII; arts. 47–56; arts. 105, 106 e 108; LC 227 arts. 136–140. Validar redação vigente e condições. Não universalizar 240 parcelas para todos os créditos ICMS; distinguir saldo atual e eventual saldo homologado ao fim da transição. Identificar obrigações legais versus recomendações de gestão e atos pendentes de verificação. Não emitir parecer jurídico.

Criar agenda de preparação para marcos 2027, 2029 e 2033, com 2–3 ações prioritárias em cada marco, baseadas na matriz. Ligar cada item a fonte oficial ou business case. Se norma não acessível, apresentar tema como pendente de validação, sem afirmar obrigação específica.

Acrescentar agenda transversal inspirada nas referências da seção 2.1: a transição é uma questão de negócio, não apenas de cumprimento legal. Vincular Suprimentos à cadeia de crédito e aquisições; Comercial/Jurídico a preços e cláusulas; Tesouraria ao efeito de caixa; TI à confiabilidade dos dados; liderança à decisão. Usar marcos e próximos passos, não percentuais inventados de prontidão, status ou atrasos. Se houver necessidade de pesquisa legislativa adicional, registrar data e fonte, distinguindo proposta, norma publicada e vigência. Não replicar percentuais de pesquisas externas como indicadores da companhia.

**Aceite:** cronograma e matriz rastreáveis, específicos para cargas/infraestrutura, fontes e data visíveis; sem confusão entre legislação e parâmetros de simulação; página sintética e acionável, não enciclopédia fiscal.

## 12. V2-08 — Carteira estratégica de iniciativas e business cases

Estruturar três business cases prioritários; utilizar ficha comum e dados calculados, evitando duplicação manual. Não sugerir que são projetos oficiais ou aprovados. A decisão proposta é avançar para estudo/validação, não implementar automaticamente.

| Caso | Evidência / motivação | Indicadores / critério de decisão |
|---|---|---|
| BC01 — Gestão e realização de créditos ICMS | Saldo público e transição; histórico de créditos e compensações | Principal hipotético elegível, VP incremental, custo, prazo, restrições e cenários; estudo somente se elegibilidade e benefício documentados |
| BC02 — Preparação para CBS/IBS, contratos e CT-e | Marcos legislativos, desafios publicamente discutidos sobre contratos/preços e integração de dados | Comparativo de repasse 10.4, agenda de revisão contratual, inventário de interfaces/processos, riscos e homologação; sem afirmar lacuna real nem fabricar ROI |
| BC03 — Planejamento tributário de investimentos | DIR 2025, DIP 2027–29 e referências oficiais REIDI/REPORTO | Materialidade por ano/classe, sensibilidade de caixa 10.3, elegibilidade por aquisição; efeito de regime específico apenas quando fundamentado |

Cada ficha deve conter: título e status proposto; evidência e link; problema/pergunta; hipótese; benefício econômico/financeiro ou qualitativo (classificação da origem); premissas e fórmula; alternativas; riscos e dependências; esforço/custo/prazo se conhecidos ou “a levantar”; áreas funcionais genéricas; recomendação e decisão solicitada; etapas e critério de sucesso; grau de confiança/limitação. BC01 deve consumir os resultados do simulador ou cenário salvo na sessão, sem número fixo contraditório.

Fluxo de projeto padrão: diagnóstico e conciliação → validação fiscal/jurídica → business case → decisão gerencial → implementação/homologação → monitoramento dos benefícios. Indicar participantes propostos sem reproduzir áreas reais da empresa. Priorizar qualitativamente por materialidade, urgência, evidência e dependências; explicar critérios, não criar ranking numérico arbitrário. Separar economia fiscal, antecipação de caixa, VPL e redução de riscos, sem somar benefícios incomparáveis.

BC02 e BC03 devem consumir resultados calculados dos cenários 10.4 e 10.3, com origem e hipóteses, e decisões de validação (não de execução automática). Acrescentar no BC02 um pequeno mapa conceitual de fluxo futuro: dados de ERP/documentos/contratos → conciliação → modelo analítico → decisões. É uma proposta de integração, não descrição da arquitetura corporativa atual. Não implementar SAP, APIs empresariais, apuração de documentos reais ou nova infraestrutura. Cada ficha deve indicar responsável funcional proposto e dependências, não pessoas ou nomes de áreas internas. Não criar um quarto business case obrigatório; incorporar a análise comercial ao BC02 e o CAPEX ao BC03. 

**Aceite:** três fichas completas, ao menos uma com cálculo financeiro rastreável, critérios de aprovação e sucesso; recomendação executiva clara, sem estimativa inventada de custo/prazo quando indisponível.

## 13. V2-09 — Navegação, identidade visual, fontes e exportação

1. Implementar navegação por hash/rotas simples compatíveis com GitHub Pages (sem servidor ou configuração complexa), links diretos por módulo, atualização de título, funcionamento Voltar/Avançar, recarga e retorno ao início. Preservar filtros e cenários na sessão quando útil. Usar links/controles acessíveis, `aria-current`, foco visível e navegação por teclado. Não instalar roteador pesado sem necessidade.
2. Melhorar navegação contextual: links de insights devem abrir o gráfico, tema ou simulador correspondente; botão claro de retorno; filtro local identifica visual afetado. Manter cinco módulos + fontes. Simuladores com presets, reset, unidades, inputs válidos e feedback de erro; não converter campo vazio em zero inadvertidamente.
3. Revisar todos os cards monetários/percentuais, insights financeiros, gráficos e tabelas: fonte clicável no próprio elemento (não só na página de metodologia), título/localizador e período. Modal de dados adaptados deve explicar o que e como foi adaptado, com exemplo reproduzível. Para hipóteses, link para premissas/metodologia, não para uma fonte que não contém o valor. Links externos confiáveis, abertura em nova aba quando apropriado. Fonte oficial pode revelar a identidade; não remover rastreabilidade.
4. Layout: manter azul/azul-escuro/amarelo, fundo claro, hierarquia, tipografia legível, 4–6 KPIs e 2–3 gráficos principais quando pertinentes, até três insights em destaque. Evitar duplicar cards de data e disclaimers em excesso; data/natureza/limite material permanecem próximos ao valor. Gráficos com rótulos, eixos, unidades, contraste, legenda e tooltip; alternativa textual compacta. Preferir barras, cascata e tabelas legíveis a efeitos sofisticados. Sintetizar cada página em 1–2 slides conceitualmente, sem gerar PowerPoint.
5. Exportar CSV conforme módulo e filtros, incluindo período, métrica, valor numérico, unidade, natureza, fonte e localizador. Nos simuladores, exportar premissas e resultados separadamente ou em CSV claramente estruturado. Formato compatível com Excel pt-BR (UTF-8 BOM, separador ponto e vírgula, vírgula decimal ou convenção explicitada), sem fórmulas maliciosas em campos textuais. Não exportar uma linha de resultado financeiro quando usuário estiver em diagnóstico de créditos.
6. Impressão: CSS print preserva período, data-base, premissas dos simuladores, resultado, fonte e limites. Evitar esconder os inputs sem replicar os valores em resumo imprimível. Gráficos sem corte, margens e quebras legíveis. Não criar gerador PDF/PPT adicional.
7. Responsividade em desktop, notebook e celular, com menu compacto, tabelas roláveis somente localmente quando necessárias, sem scroll horizontal da página. Testar cards longos, filtros, modal, legenda, rodapé e simulação com valores extremos. Manter ícones consistentes, sem depender de fontes externas obrigatórias.

8. Benchmark de apresentação 3T26: recuperar a apresentação e verificar o padrão de cores e gráficos. Preferir amarelo para período anterior e azul-escuro para atual quando o gráfico representa comparação temporal; manter cores consistentes por tributo quando representa composição, com legenda explícita. Usar valores sobre barras quando legíveis, variação percentual ou p.p. junto à comparação, leitura executiva breve e notas metodológicas discretas. Para CAPEX, colunas empilhadas com totais e legenda por categoria; para ponte de valores, cascata; para evolução percentual com datas equivalentes, linha ou colunas. Não confundir amplitude ou direção com desempenho favorável. Não copiar slides, logotipo, fotografias, tipografia proprietária ou gráficos completos; criar visuais próprios com dados e referência. Se o PDF não for recuperado, manter tema existente e diretrizes verificáveis, registrando a limitação. Aplicar alterações de design por componentes compartilhados, não redesenhar todas as páginas nem prejudicar a legibilidade mobile. 

**Aceite:** navegar por links diretos e Voltar/Avançar; fontes clicáveis em cada visual quantitativo; modais abrem/fecham por teclado; CSV corresponde ao contexto; impressão preserva premissas; desktop 1366×768 e mobile ~390×844 sem sobreposição ou overflow indevido; linguagem pública genérica.

## 14. V2-10 — Testes, revisão independente e gate de qualidade

Executar testes já existentes (`npm test`, `python -m unittest discover -s tests -p 'test_*.py'`, `npm run build`) e ampliar somente para cobrir riscos novos. Reutilizar fixtures, evitar auditorias repetitivas. Usar instalação reproduzível via lockfile e ambiente documentado.

| Grupo | Testes mínimos |
|---|---|
| Dados | Receita bruta − deduções = líquida conforme fonte; soma de créditos = total = circulante + não circulante; DVA soma das esferas; contingências sem dupla contagem; unidades/sinais; escopo consolidado; períodos equivalentes; ausência não vira zero |
| DIR/DIP e DFC | Totais em reais reconciliados por ano/classe; realizado vs previsto; traço vs zero preservado; ausência não vira zero; escopo regulatório distinto do contábil; DFC sinais, períodos, fonte e ausência de dupla contagem |
| CAPEX e contratos | Fixtures 10.3/10.4; seleção de ano/classe, reset, prazos, taxa zero, créditos zero, sinais de repasse e compartilhamento, limites de origem e ausência de duplicação do impacto da reforma |
| Alíquotas | Despesa/LAIR correta; base zero ou negativa não aplicável; variação em p.p.; nominal + ajustes = efetivo; comparar 9M apenas com 9M |
| Cascatas | Saldo inicial + deltas = final; positivos/negativos/zero; filtros mantêm universo; Outros não desaparece da conta; rótulos derivados |
| Créditos | VP com fixture 50/24/12/12%/0,5; prazo igual; taxa zero; prazo proposto maior; principal zero; custo maior que ganho; inputs inválidos; reset; origem dinâmica |
| Reforma | Alíquotas zero, crédito zero/100%, repasse zero/100%, saldo credor, prazo zero, resultado negativo/positivo, dados reais substituídos por hipótese; sem falsa apuração de transição; unidades e sinais; coerência de agregação |
| UI | Seis páginas, links diretos, histórico do navegador, filtros, fonte, modal, teclado, presets, reset, CSV e impressão; textos de limites e períodos visíveis; sem travamento |
| Regressão | Preservar indicadores e fontes válidos da V1; sem quebra de URL, build ou workflows; testar alterações de fixture para encontrar números fixos |
| Publicação | Build/Actions aprovados; HTML/JS/CSS/JSON públicos sem autenticação, sem erro de recursos ou console da aplicação; links externos relevantes conferidos |

Revisão visual: abrir páginas e simuladores em navegador real/cloud quando disponível; capturar todas as telas essenciais em desktop 1366×768 e 1920×1080 e mobile 390×844 (ou viewport equivalente), validar em larguras menores se viável. Chrome/Edge prioritários, Firefox/Safari quando ferramentas permitirem. Conferir contraste, cortes, legibilidade, rótulos, fonte e impressão. Medir carregamento inicial em condição documentada, com meta de até 3 s, sem inventar resultados. Otimizar bundle apenas se necessário. Testes por iframe/viewport não equivalem a aparelho físico.

Revisão de conteúdo: conferir fontes e legislação, datas, natureza, fórmula e limite de toda afirmação quantitativa; verificar que insight não afirma causalidade sem evidência; nenhum valor sugere promessa de economia; nenhuma identificação indevida da empresa/demonstração profissional no texto público. Validar documentação sanitizada; links e documentos oficiais autênticos preservados.

**Gate antes do merge:** zero erros materiais conhecidos nos números e simuladores apresentados, zero regressões críticas, testes e build aprovados, revisão de todas as páginas e evidências registradas. Se navegador indisponível, não alegar teste executado; tentar alternativa e reportar limitação para decidir se é necessária intervenção. Problemas não críticos podem permanecer em backlog com impacto explícito; nenhum dado crítico inválido deve chegar à produção.

## 15. V2-11 — Publicação e entrega

1. Atualizar README, `docs/METODOLOGIA.md`, `docs/FONTES_STATUS.md`, `docs/TESTES.md`, `docs/STATUS.md`, `docs/BACKLOG.md` e roadmap publicável com alterações, evidências, pendências e versão. Registrar status real, não marcar tarefas como concluídas por mera implementação sem teste.
2. Revisar diff e arquivos públicos; nenhuma credencial, informação pessoal desnecessária, documento interno ou cópia integral não autorizada. Preservar referência de rollback. Executar merge conforme permissões e publicar pelo workflow Pages existente, sem mudar URL ou ativar cobrança.
3. Validar URL anônima após deploy: verificar HTML, assets e JSON sem cookies/Authorization; abrir em navegador e testar navegação, dados recentes, cascatas, fontes, simuladores e reset. Confirmar que o commit publicado corresponde ao testado. Se deploy falhar, investigar logs e corrigir; se regressão grave, restaurar V1 pelo mecanismo de versionamento seguro. Não apagar histórico.
4. Entregar ao patrocinador: URL final, versão/SHA, resumo das mudanças, indicadores incluídos, fontes verificadas, testes efetivamente executados, comparação V1/V2, limitações, custo de infraestrutura, pendências e recomendação de prontidão para encaminhamento. Não enviar o painel à público avaliador automaticamente.

## 16. Definição de pronto e limites de escopo

A V2.1 deve demonstrar diagnóstico atual, explicação das variações, eficiência tributária e preparação para reforma, com três business cases e cenários interpretáveis. Deve incluir DIR/DIP conciliados, visão de caixa quando fonte validada, CAPEX com análise de prazo e sensibilidade comercial normalizada, sem adicionar módulos principais. Planilha tarifária é complemento condicionado à validade; a alternativa normalizada é parte da entrega. Benchmark visual é refinamento incremental, não mudança de identidade. A finalidade é avaliação gerencial, não operação fiscal. A ausência de ANTT/DIRBI, série 2022–23, ato complementar ou detalhamento interno não é motivo para fabricar dado ou prolongar indefinidamente a entrega. Documentar o que não foi possível e usar fontes válidas alternativas.

Fora desta versão: reconstrução em Power BI/PPT, conversores, benchmarking amplo, dados operacionais por rota sem base válida, integração SAP real (o mapa conceitual de integração permanece no escopo), autenticação, banco remoto, ML, agentes de IA, atualização legislativa universal, simulações fiscais em nível de documento, projeto de automação interna com indicadores inventados. Novos serviços ou custos exigem autorização. Não ampliar escopo para completar artificialmente o roadmap.

### Checklist de rastreabilidade da avaliação V1

- [ ] Indicadores 9M de IR/CS e dados ITR revisados — V2-01.
- [ ] Premissas e interpretação da reforma revistas — V2-06.
- [ ] Valores e datas duplicados eliminados — V2-02.
- [ ] Fontes clicáveis e natureza dinâmica — V2-02/09.
- [ ] DVA, compensações, cascata de créditos e contingências — V2-04.
- [ ] Operações ferroviárias e CAPEX — V2-05.
- [ ] Matriz de impactos — V2-07.
- [ ] Três business cases — V2-08.
- [ ] Variações nos KPIs, comparativos e presets — V2-03/06.
- [ ] Hierarquia visual, navegação, filtros, exportação, impressão e responsividade — V2-09/10.
- [ ] Acesso anônimo, regressão, documentação e entrega — V2-10/11.

- [ ] Benchmark 3T26 com fonte recuperada ou limitação e padrão executivo implementado — V2-03/09.
- [ ] Prioridades publicamente discutidas refletidas na matriz e nos casos sem afirmar diagnóstico interno — V2-07/08.
- [ ] DIR 2025 e DIP 2027–29 conciliados; dados realizados e planejados distintos — V2-01/05.
- [ ] Pagamentos DFC conciliados ou indisponibilidade justificada; DVA reconciliada quanto ao conceito — V2-01/04.
- [ ] Sensibilidade de prazo do CAPEX com hipóteses, fontes e teste numérico — V2-06.
- [ ] Comparação de repasse e agenda de contratos; planilhas tarifárias inspecionadas ou fallback documentado — V2-06/07.
- [ ] BC02/BC03 conectados aos cenários e mapa conceitual de integração, sem implementar ERP — V2-08.
- [ ] Novos testes, acessibilidade, fontes, documentação sanitizada e publicação sem regressão — V2-10/11.


Marcar como concluído somente com evidência; se bloqueado, registrar causa, alternativa tentada, impacto e encaminhamento. Não usar percentual de aderência ou nota subjetiva como substituto de teste.

## 17. Política de execução autônoma no Work

Executar tarefas de ponta a ponta no mesmo projeto, usando ferramentas disponíveis de GitHub, navegação, execução e testes. Avançar entre etapas automaticamente; resolver erros, testar novamente e documentar. Não pedir confirmações sobre decisões consolidadas, nem exigir que o patrocinador copie comandos, baixe fontes públicas, faça merges ou execute rotinas que o Work pode realizar. Quando uma fonte complementar falhar, prosseguir com atividades independentes; preferir alternativa oficial e limitar tentativas desproporcionais.

Solicitar intervenção apenas para autenticação pessoal obrigatória, autorização exigida pela ferramenta, custo possível, mudança material de escopo, ação destrutiva não autorizada ou bloqueio incontornável. Nunca afirmar que executou o que não foi efetivamente executado. Registrar limitações sem impedir entregas parciais seguras. Manter a V1 publicada até a V2 passar no gate; não alterar outros projetos. O patrocinador fará a avaliação final e eventual contato profissional.

## 18. Prompt de retomada para o Work

> Continue a implementação do projeto Inteligência Tributária no repositório existente `alvarobonifacio1980/inteligencia-tributaria`. Leia o arquivo `Inteligencia_Tributaria_Roadmap_V2_1_Consolidado.md` anexado, que substitui a V2.0 e consolida a avaliação da V1 e o benchmark institucional posterior. Se parte da V2 já foi implementada, concilie o estado atual com a V2.1 e aplique somente as diferenças. Utilize-o como especificação principal de evolução, preservando o Roadmap V1 e as decisões posteriores não conflitantes. Consulte os arquivos e o histórico do chat de implementação para identificar o estado real atual. Não recrie o projeto do zero e não altere outros repositórios.
>
> Execute autonomamente as etapas V2-00 a V2-11, priorizando correção dos dados e simuladores, valor estratégico, experiência executiva e publicação validada. Incorpore DIR/DIP, DFC validada, benchmark 3T26, agenda comercial/contratual, sensibilidade de CAPEX e preços e business cases conectados às funções de negócio. Não transforme as referências públicas em afirmações de prontidão, processos ou prioridades internas; use fallback normalizado se planilhas tarifárias falharem. Confira números candidatos diretamente nas fontes oficiais; não transforme estimativas ou hipóteses em fatos. Preserve o painel V1 até a aprovação dos testes da nova versão. Mantenha orçamento de infraestrutura R$ 0,00, princípio KISS, identidade visual existente, referências clicáveis, português BR e identificação pública genérica como Empresa Ferroviária. Não mencione demonstração profissional ou empresa nominalmente nos materiais públicos; preserve fontes oficiais autênticas.
>
> Faça a coleta, desenvolvimento, testes, correções, commits, merges autorizados pelo escopo, documentação e publicação usando as ferramentas disponíveis. Avance sem pedir comandos “pp” ou confirmação a cada etapa. Em caso de erro, investigue e corrija; se uma fonte complementar falhar, registre e prossiga com alternativas válidas. Só solicite minha intervenção por necessidade obrigatória de autenticação/autorização, possibilidade de custo, mudança significativa de escopo, ação destrutiva ou bloqueio incontornável. Não contrate serviços, não ative trials e não contate a público avaliador.
>
> Ao concluir, apresente a URL pública validada, versão publicada, resumo das melhorias, fontes conciliadas, testes realizados, limitações, backlog residual e recomendação de prontidão. Não produza outro planejamento extenso: inicie a execução pela V2-00 e siga os critérios de aceitação deste roadmap.

## Registro de execução V2.1

Requisitos confrontados em ACEITE_V2.md; entregas antecipadas da V1 reaproveitadas. Release a23e86b publicada após testes, CI isolada, coleta online e inspeção de qualidade.39 testes finais, build/deploy aprovados e acesso público verificado. Limites explícitos em BACKLOG.md e TESTES_V2.md; nenhuma identificação nominal no texto editorial, fontes oficiais preservadas.
