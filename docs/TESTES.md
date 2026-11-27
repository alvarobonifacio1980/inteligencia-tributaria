Estado atual V2.1:39 testes, evidências atualizadas em [TESTES_V2.md](TESTES_V2.md). O registro abaixo preserva as validações históricas da V1.

# Evidências de validação

Estado atual: 19 testes aprovados (11 JS + 8 Python), build e deploy ampliado aprovados; HTTP público e navegação conferidos. A seção Ampliação registra os testes mais recentes; seções anteriores preservam a evolução.

27/11/2026, ambiente Work, Node 24.22.3 e Python 3.12.

## Executados

- `npm test`: 6 testes aprovados: VP incremental, prazo igual/taxa zero, negativos/NaN, créditos zero/100%, repasse, transição e extremos.
- `python -m unittest discover -s tests -p 'test_*.py'`: 4 testes aprovados: conciliação receita/créditos/reconciliação, escopo/alíquota, provisão e detecção de base inválida.
- `npm run build`: aprovado; pacote JS inicial ~771 kB, gzip ~256 kB. Sem fonte externa ou mídia remota obrigatória.
- `python scripts/coletar.py`: PDFs baixados, tipo verificado, extração `pdftotext`, âncoras numéricas verificadas e hashes registrados.
- `scripts/cvm.py` com Pandas: 4 contas oficiais conciliadas contra RI (receita, LAIR, IR/CS, crédito circulante).
- Chrome desktop (~1350 px): tela executiva inspecionada visualmente; gráficos renderizados; filtro 2025→9M2026 apresentou 9M2025/9M2026, valores corretos e alíquota indisponível sem substituição indevida.
- Chrome: navegação até cenários, principal 50→0 resultou em benefício R$ -0,5 mi (custo inicial), sem quebra.
- Responsividade: iframe de 390 × 844 (375 px úteis com scrollbar), desktop cloud browser. Captura visual inspecionada; menu e conteúdo legíveis. `scrollWidth=clientWidth=375` na visão executiva e em cenários. Não equivale a teste em aparelho físico.

## Limites de cobertura

Não foi comprovada a meta de carregamento inicial de 3 s; nenhum teste Safari/Firefox ou celular físico é alegado. Publicação e acesso sem autenticação foram concluídos conforme registros abaixo.

## Publicação verificada

- Actions run `46020318841`: validação aprovada. Deploy inicial falhou 404 porque Pages ainda não estava habilitado; configuração ativada e job reexecutado com sucesso (`140578704982`).
- URL: https://alvarobonifacio1980.github.io/inteligencia-tributaria/
- GET sem cookies, Authorization ou sessão GitHub: HTML, JS, CSS e JSON retornaram HTTP 200; evidência em `HTTP_PUBLICO.json`. Tempo total dos quatro requests sequenciais ~23 s no ambiente remoto; não é medida de carregamento do navegador ou comprovação da meta de 3 s.
- Navegador na URL publicada: cinco módulos + fontes abriram com título correto; sem login/cadastro. Console consultado: mensagens de erro observadas pertenciam à extensão do navegador, não à origem da aplicação.
- Fonte adicional: extração estrutural reproduzida em `data/extracao_validada.json`: 4 períodos de receitas e 3 datas de composição de créditos.

## Validação final em nuvem

- Run coleta `46021113127`: concluído com sucesso, incluindo download de PDFs, extração estrutural, validação, conciliação CVM/Pandas, testes Python e artifact de evidências.
- Build/deploy do commit `35c58b6`: aprovado (workflow #2).
- Na versão publicada: botão de 10% do ICMS mudou a natureza para Híbrido e principal para R$ 27,8 mi; restauração recuperou o exemplo de R$ 50 mi e benefício de R$ 4,3 mi.

## Ampliação — 27/11/2026

- `npm test`: 11 testes aprovados, incluindo transição federal/estadual, créditos excedentes, CAPEX sem dupla contagem, fluxo ICMS e fixtures comuns.
- Unittest Python: 8 testes aprovados, incluindo conciliação 9M, segregação histórica, soma DIRBI e cálculo independente das fixtures JS/Python.
- Build Vite aprovado; pacote principal cerca de 806 kB / 266 kB gzip.
- Navegador desktop: 9M2026 mostra 33,10%; cenários respondem aos controles; REPORTO em 2030 mantém resultado condicionado; DIRBI IRPJ filtra para R$ 9,53 mi e janela explica fonte, chave, conversão e soma.
- Capturas desktop e viewport móvel inspecionadas visualmente. Nas seis páginas, iframe 390×844 com 375 px úteis: scrollWidth = clientWidth = 375. Mesma limitação de não ser aparelho físico.
- Janela Adaptado aberta e fechada pelo botão acessível Fechar explicação. As janelas e fontes anteriores foram preservadas.
- Deploy ampliado aprovado: run 46040278129, commit 17fa4c4. HTML, JS, CSS e JSON públicos HTTP 200 sem cookies/Authorization; evidência atual em HTTP_PUBLICO.json.
- Navegador na URL pública confirmou DIRBI, histórico, cascata e simuladores. CAPEX com hipótese habilitada: R$ 0,28 mi; crédito alternativo imediato: R$ -0,20 mi (custo). Restauração volta a resultado condicionado.
- Coleta ampliada local reproduzida com cache oficial completo e hashes: scripts/ampliar_fontes.py --offline. Execução em nuvem 46040317265 falhou por conexão encerrada pela DIRBI; novas tentativas e cliente TLS alternativo implementados e reexecutados (46040589527), sem desativar validação de certificado.

- Reexecução 46040589527 confirmou bloqueio TLS do portal DIRBI também com cliente alternativo. Implementado fallback opcional e explícito: teste local com falha de rede simulada confirmou preservação exata dos 12 registros, flag de reutilização e hash/data original. Sem fallback para divergência de conteúdo. Coleta continuará CVM e testes, registrando DIRBI reaproveitada como aviso.

## Encerramento da ampliação

- Build/deploy final aprovado: [run 46040961358](https://github.com/alvarobonifacio1980/inteligencia-tributaria/actions/runs/46040961358), commit 2cfed46.
- Coleta recuperada aprovada: [run 46041005921](https://github.com/alvarobonifacio1980/inteligencia-tributaria/actions/runs/46041005921). PDFs, CVM anual e ampliada, testes Python e artefato de evidências concluídos. DIRBI explicitamente preservada do snapshot revisado por indisponibilidade TLS, conforme aviso do job; não houve download novo dessa fonte no runner.
- Caminho de leitura integral DIRBI reproduzido localmente com o script final e arquivo oficial completo em cache; executado com sucesso. Caminho de indisponibilidade também testado localmente e confirmado na nuvem.
- Documentação final, dicionário, fórmulas, backlog e estado de fontes atualizados. Sem modificação em outros repositórios, custo ou contato externo.
