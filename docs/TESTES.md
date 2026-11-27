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

## Ainda em execução

Publicação Actions/Pages e teste HTTP anônimo. Não foi medida meta universal de 3 s; nenhum teste Safari/Firefox ou celular físico é alegado.
