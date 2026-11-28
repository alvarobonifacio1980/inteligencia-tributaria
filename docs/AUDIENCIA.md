# Audiência privada — Umami Cloud

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
