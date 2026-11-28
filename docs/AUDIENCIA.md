# Audiência privada — política vigente

## Coleta automática com opção de desativação — 28/11/2026

Por orientação do responsável, a coleta inicia automaticamente sem clique para novos visitantes. Não há botão de permissão no rodapé; permanece link discreto para privacidade. No Sobre, o visitante pode desativar ou reativar. Recusas anteriores (`negado`) continuam impedindo toda coleta; não são apagadas ou reinterpretadas. O modo automático vale apenas na ausência de preferência ou com ativação explícita anterior.

Continuam: payload mínimo, sem valores digitados, URLs livres ou IDs próprios; sem cookies de rastreamento, replay ou anúncios; DNT/GPC e exclusões de teste; localStorage indisponível mantém coleta desativada. Remoção do script e bloqueio dos envios ao desativar, sem excluir eventos já recebidos. Não recupera visitas passadas. `?sem_estatisticas=1` impede coleta desde a abertura.

### Avaliação de legítimo interesse

- Finalidade: medir interesse agregado nas análises e melhorar navegação/funcionalidades deste estudo público. Não identificar visitantes, tomar decisões sobre pessoas ou cruzar dados com candidaturas, contatos e bases externas.
- Necessidade: rotas conhecidas e ocorrência de ações, sem conteúdo dos campos; uma interação de simulador por30s. Dados técnicos do provedor apenas para métricas de sessão/geografia aproximadas. Sem ferramentas publicitárias ou gravação.
- Balanceamento: benefício limitado à melhoria do produto; navegação pública pode gerar expectativa de estatísticas mínimas. IP e User-Agent recebidos pelo provedor e sequência de sessão estimada não são tratados como dados absolutamente anônimos. Baixo volume de acessos permite inferências indevidas: não atribuir identidade por horário, origem ou localização.
- Salvaguardas: aviso transparente, desativação simples, recusas preservadas, DNT/GPC, acesso administrativo privado, retenção de seis meses no Hobby, sem identificador próprio ou vinculação entre dispositivos. A configuração anterior exigia consentimento; essa mudança não deve reativar quem recusou.
- Risco residual: terceiro no exterior, geolocalização imprecisa e sessões estimadas. Revisar esta avaliação se forem ampliados dados, finalidade, rastreamento ou serviços. Não constitui certificação de conformidade nem parecer jurídico integral.

Referência: [ANPD — Cookies e proteção de dados pessoais](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf), medição de audiência e legítimo interesse em contextos específicos; ausência de cookies não dispensa os demais requisitos. [DPA Umami](https://umami.is/dpa).

48 testes (32 JS +16 Python) e build aprovados, incluindo visita sem preferência, recusa legada, desativação/reinício, falha do serviço e prevenção de duplicidade. Dados financeiros e simuladores inalterados. Rollback: reverter o commit deste ajuste; alternativamente enabled:false para interrupção geral.

## Histórico da implantação anterior (consentimento prévio)

Os registros abaixo descrevem o estado anterior à mudança para coleta automática. A política vigente é a indicada acima.



Estado: integração validada para ativação na V2.1.2. Coleta condicionada à permissão do visitante. Testes isolados e recebimento pelo SDK oficial registrados separadamente abaixo.

## Serviço e orçamento

Consulta em27/11/2026: [Hobby](https://umami.is/pricing), US$0/mês,1 site, até100 mil eventos/mês e6 meses de retenção. [FAQ](https://docs.umami.is/docs/cloud/faq): visitas e eventos contam; propriedades adicionais também consomem franquia. Sem API administrativa no Hobby. Integração usa só ID público de coleta; nunca token privado. Não ativar trial/upgrade, cartão ou cobrança de excedentes. Conferir Subscription/Usage na conta antes de ativar; limite não deve ser contornado por mudança de plano. Um único site gratuito não cobre automaticamente todo o portfólio.

## Dados e eventos

Cada rota normalizada é uma visualização, inclusive módulo/subaba, Voltar/Avançar e Sobre. Renderizações repetidas da mesma rota não contam novamente. Não há captura de texto/valor de input, query, fragmento livre, URL completa de origem, identificação própria, gravação, cookies publicitários ou identificação entre dispositivos.

| Evento | Ocorrência |
|---|---|
| simulador_acesso | Entrada na subaba de simulador |
| simulador_interacao | Alteração de controle; no máximo uma por30s em cada subaba |
| cenario_predefinido | Preset, uso de referência ou restauração |
| business_case | Entrada na carteira ou abertura de ficha |
| metodologia | Abertura da explicação |
| fonte | Clique em referência documental |
| exportar_csv | Clique para exportar |
| imprimir | Evento beforeprint, inclusive comando do navegador |
| repositorio | Link do código no Sobre |

Nomes terminam em `:modulo/subaba`. Não enviamos propriedades adicionais: a categoria e rota bastam. Não classificamos pessoa pelo conteúdo acessado. Debounce/deduplicação de ações evita repetição em1s; interações têm janela30s. Eventos de clique demonstram intenção, não leitura ou conclusão do download/impressão.

## Privacidade e preferências

Adotado consentimento opcional antes da primeira requisição ao Umami, dada a transmissão a terceiro e a identificação probabilística de sessões. Sem alegação de dispensa universal de consentimento por ausência de cookies. O [guia da ANPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf) e o [DPA do provedor](https://umami.is/dpa) são referências; isso não constitui parecer jurídico integral. Preferência funcional salva localmente apenas para lembrar a escolha; não é identificador de audiência. DNT/GPC respeitados quando presentes. Fluxo continua integralmente disponível após recusa.

O provedor recebe IP e User-Agent no transporte e usa dados técnicos para estimar geografia/sessões; não prometer anonimato absoluto ou ausência de processamento de IP. Não enviamos IP por parâmetro ou valores digitados. Dados de infraestrutura e backups seguem DPA/suboperadores; região US/EU não equivale a processamento exclusivamente regional. Ao configurar, conferir a região e suas condições. Estatísticas apenas no login privado; não habilitar Share URL, equipes ou dashboards públicos.

Excluir acessos: no Sobre, escolher “Excluir meus acessos neste navegador” (ou “Continuar sem estatísticas”). Aplicável a cada navegador/dispositivo; não remove visitas já registradas. Para abrir sem coletar desde a primeira página, usar `?sem_estatisticas=1` antes do hash. Também respeita `umami.disabled=1` no localStorage. Localhost, domínio incorreto, webdriver, recusa e configuração desativada não carregam script. Testes automatizados podem acrescentar o parâmetro; não há garantia de detectar todos os bots.

## Consulta e limitações

Após ativação, acessar a conta privada, selecionar o site e intervalo. Ajustar preferência de fuso para America/Sao_Paulo ou UTC−03:00; confirmar horário de visita teste. Consultar Overview, Realtime, páginas, eventos e Journey, conforme recursos efetivamente disponíveis no Hobby. Usage mostra consumo da franquia. API/MCP, replay e heatmap não são dependências desta integração.

Visitantes únicos são estimativas; redes compartilhadas, VPN, bloqueadores e recusa alteram contagens. Retorno não é identificação longitudinal confiável; não criamos ID persistente para melhorá-lo. Sequência é a das rotas/eventos da sessão estimada. Duração depende de eventos observados; tempo da última página e abandono não são relógio exato. Não enviar heartbeats contínuos para aumentar artificialmente o consumo. Não identificar quem acessou nem inferir identidade de pessoa por cidade/horário.

## Ativação e recuperação

`public/data/audiencia.json`: `enabled`, UUID público do site, script oficial, hostname e basePath. `src/audiencia.mjs` isolado do React e reutilizável mediante troca de rotas/configuração; `Privacidade.jsx` cuida das preferências. Automático desabilitado; envio manual com campos permitidos e before-send adicional. Falha do script/serviço descartada sem bloquear UI; sem fila persistente/reenvio de dados antigos.

Antes do merge: criar/configurar conta Hobby, verificar estatísticas privadas, ID e primeiro recebimento real; testar rotas/eventos e ausência de valores/duplicação. Revogar permissão e verificar interrupção. Executar testes/build e publicar só após aceite. Desativação: `enabled:false`; rollback completo por reversão do merge, preservando base `ac1ff55`. Não reescrever histórico nem modificar outros projetos.


## Conta configurada — aguardando confirmação de recebimento

Hobby confirmado na interface administrativa: US$0/mês,100K eventos/mês,1 site e6 meses. Site Inteligência Tributária criado; ID público inserido na configuração, ainda com enabled:false. Compartilhamento sem registros; replay/heatmap dependentes de Business não ativados. Região observada: US(Oregon). Fuso America/Sao_Paulo, idioma português do Brasil.

Uma rotina local isolada foi iniciada para validar o SDK com rotas /__validacao_audiencia__/; a confirmação de recepção não foi concluída antes do reinício do ambiente. Esses registros, se recebidos, são testes e devem ser excluídos por filtro de caminho na análise. Não houve redefinição ou exclusão de dados. Nova autenticação administrativa necessária para verificar o resultado; integração não publicada enquanto pendente.


## Recebimento confirmado — 28/11/2026

Após nova autenticação, interface privada confirmou1 visitante de teste,3 visualizações e9 eventos distintos (cada qual com1 ocorrência), nas rotas /__validacao_audiencia__/. Nove categorias da tabela recebidas. O teste controla SDK/serviço; testes isolados cobrem a ligação dos eventos da aplicação. Não houve acesso orgânico demonstrado por essa evidência. Para leitura de audiência real, filtrar caminho contendo `/inteligencia-tributaria/`, que exclui o prefixo de teste. Não se apagaram registros.

Administrador: https://cloud.umami.is/analytics/us/websites/b154e677-76cb-45a6-abaf-95a8be728cdd . Acesso por login; compartilhar esse endereço não torna estatísticas públicas. Share URL permaneceu desativado. Idioma/fuso são preferências do navegador administrador; confirmar pt-BR/America/Sao_Paulo ao acessar por outro navegador.

Configuração ativa com ID público de coleta. Estatísticas dependem de consentimento, DNT/GPC, bloqueadores e disponibilidade do serviço. Não recupera acessos anteriores à ativação. ID público não concede acesso administrativo. Código de teste HTML local não integra o build nem o repositório.


## Publicação confirmada — 28/11/2026

V2.1.2 publicada via PR4, release `2fcad2742573fc1ea04fd13657f74ce200169aa4`, workflow `46103524891` com validação e deploy aprovados. URL original acessada em navegador sem autenticação; versão2.1.2 e controles no Sobre presentes. Permitir/recusar e retorno à visão executiva funcionaram. A preferência final do navegador de QA foi recusa, impedindo novas coletas.

O SDK foi carregado nessa sessão pública ao permitir estatísticas; esse navegador não expôs a automação via webdriver. Logo, a visita de QA pós-publicação pode integrar as métricas reais além da visita isolada com prefixo de teste. Não considerar essas verificações como interesse orgânico. Para testes futuros, abrir com `?sem_estatisticas=1` antes do hash; webdriver é proteção complementar, não universal. Nenhum registro foi apagado.

Recepção no serviço comprovada pelo teste isolado (3 visualizações e9 eventos). A inspeção pós-publicação comprovou interface/configuração e preferências; não foi feita nova leitura autenticada dos eventos dessa sessão pública. Não há identificação de pessoas ou recuperação de acessos anteriores à ativação. Estatísticas dependem de permissão e bloqueadores.
