# Evidências de validação

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
- Registro de publicação ampliada será consolidado após conclusão do deploy.
