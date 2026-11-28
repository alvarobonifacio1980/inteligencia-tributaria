# Status — Inteligência Tributária V2.1

Data de revisão: 27/11/2026. URL estável: https://alvarobonifacio1980.github.io/inteligencia-tributaria/

Baseline recuperável V1: a961724182664b0baef92c0eebea2a1432c8bf4c. Evolução na branch v2-melhorias; produção preservada durante desenvolvimento e validação. Gate pré-publicação aprovado: testes locais, inspeção funcional/visual e CI isolada aprovados. Publicação e verificação anônima registradas ao final.

Entregas antecipadas na V1 preservadas: financeiro 9M, histórico controladora, DIRBI, contexto operacional, regras, simuladores, matriz e business cases. Diferenças executadas: DVA/DFC, compensações, riscos recentes, DIR/DIP, executivo recente, gráficos e subabas, cenários CAPEX/contratos, origem dinâmica, exportação/impressão e casos calculados.

39 testes aprovados (23 JS + 16 Python); build aprovado; validações funcionais e móveis em TESTES_V2.md. Matriz de confronto requisito a requisito em ACEITE_V2.md. Limites de fontes e aplicação real em BACKLOG.md.

A modelagem visível da reforma usa regime pleno hipotético, com cronograma legal separado. Transição aproximada continua apenas na biblioteca legada testada, sem aparência de apuração real na interface. CAPEX independente do agregado; contratos são alternativa normalizada, nunca soma duplicada ao efeito da reforma. Suspensão específica exige hipótese explícita e validação documental.

Sem custo de infraestrutura contratado, contato externo, informação privada, alteração de outros repositórios, força sobre branch ou reescrita de histórico.

Coleta online ampliada aprovada no run 46046414220, sem reutilização de snapshot nessa execução. CI da branch aprovada no run 46046447545, sem deploy na branch. Snapshot inválido testado e rejeitado; 39 testes finais locais aprovados. Limitação visual: captura 1920 falhou por timeout, mas largura renderizada 1905/1905 sem overflow; desktop1366 e móvel inspecionados.

Integração aprovada via PR1; commit de release a23e86bf5f3c17d55a907732343b790078ae7d4d. Deploy automático run46047253655. Registro final HTTP e navegador concluído abaixo. Rollback: reverter o merge a23e86b por novo commit preservando histórico, ou construir o snapshot V1 do commit a961724. Nunca force push.

## Entrega publicada

V2.1.0 publicada e verificada. Release `a23e86bf5f3c17d55a907732343b790078ae7d4d`; run `46047253655` aprovado. Mesma URL pública, sem autenticação. Testes:39 (23 JS +16 Python); build, coleta online, inspeção visual/funcional, CSV e impressão conforme TESTES_V2.md. HTTP público e comparação dos assets em HTTP_PUBLICO_V2.json.

Pronta para avaliação gerencial, observados os limites de dados e simulação. Permanecem ANTT sem integração validada, comparação com sustentabilidade bloqueada por403, elegibilidade/operações internas não disponíveis e ausência de teste físico/Safari/Firefox. Captura1920 limitada por timeout; layout1366 e móvel inspecionados. Nenhum custo de infraestrutura contratado.

Ajuste visual: seleção de período da visão executiva convertida em botões com fundo azul-escuro e seleção amarela. Períodos derivados dos dados e comparação existente preservados. Desktop e viewport móvel390 conferidos;375/375 sem overflow. Build aprovado; publicação automática pelo workflow existente.

Leituras complementares adicionadas ao final de Fontes e metodologia: artigo de gestão, Tax Summit, Brasil nos Trilhos e referências técnicas oficiais. Cada card informa contexto, evidência, limites e links. CSV do catálogo inclui as referências; cálculos e dados preservados.


Menu Sobre acrescentado como último item: resumo do projeto, tecnologias, © 2026 e links distintos para aplicação e repositório. Não exibe exportação CSV. Indicadores e simuladores preservados.


## V2.1.1 — refinamento executivo

Linha de base recuperável: `a615259a18b0ab3dd08f0bd205c0a9bdd49ed277`; desenvolvimento isolado em `v2-1-1-refinamento`. A publicação estável foi preservada durante a validação.

Antes: quatro indicadores, mensagens após gráficos e descrição tecnológica restritiva. Depois: cinco indicadores (DIP calculado e com explicação), três mensagens estratégicas antes dos gráficos, dois caminhos de aprofundamento, README atualizado e Sobre com independência e uso de IA. Mesmos dados financeiros, fórmulas, gráficos, fontes e simuladores. CSV executivo inclui alíquota, créditos e DIP com seus próprios períodos e unidades.

Testes e revisão documental registrados em TESTES_V2.md e METODOLOGIA.md. Rollback: reverter o merge da V2.1.1 por novo commit, ou construir a linha de base indicada, sem force push. Não republicar documentos de planejamento removidos. Limites de fontes, simulação econômica e navegadores da V2.1 permanecem. Sem contratação de serviços ou alteração de URL.


## Monitoramento de audiência — preparado, aguardando conta

Branch isolada `audiencia-privada`, base `ac1ff55bf570f27de5c07d2fa866d92de765a0aa`. Aplicação pública preservada. Coletor assíncrono sem dependências novas, navegação por hash normalizada, eventos limitados, preferências opcionais no Sobre e exclusão por navegador. Configuração permanece desabilitada e sem ID até validação da conta Hobby. Não houve contratação, trial, cartão ou publicação desta integração.

47 testes (31 JS +16 Python) e build aprovados. Controles de permissão/retirada conferidos em desktop e viewport390, sem overflow375/375. Nenhum script externo carregado em localhost. Testes isolados validam payload mínimo, ausência de valores, deduplicação, falha do serviço, retirada de permissão e rotas. Registro real no Umami, privacidade da conta e validação pública ainda dependem da autenticação do administrador. Guia em AUDIENCIA.md.


Retomada: conta Hobby e site configurados, ID público salvo; coleta continua desativada. Sessão administrativa perdida após reinício do ambiente. Recebimento real dos testes ainda não confirmado; não houve merge/publicação da branch. Demais evidências e passos de retomada em AUDIENCIA.md.


## V2.1.2 — audiência validada para publicação

Recebimento confirmado na conta Hobby:3 visualizações e9 categorias de eventos, uma ocorrência cada, em rota isolada de teste.47 testes e build aprovados; consentimento, exclusão, minimização, falhas do serviço, hash e frequência cobertos. Configuração ativa apenas no domínio/caminho oficial e mediante permissão. Rollback: reverter merge de audiência ou enabled:false. Linha de base estável anterior: ac1ff55. Guia, limites e evidências em AUDIENCIA.md.
