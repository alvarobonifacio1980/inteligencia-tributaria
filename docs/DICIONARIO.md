# Dicionário analítico e portabilidade

Unidade padrão: R$ milhões. Separador decimal no JSON: ponto; interface pt-BR. Ausência não equivale a zero. Dados de origem e fórmulas são independentes dos gráficos.

| Estrutura / campos | Conceito / chave | Natureza e restrição |
|---|---|---|
| financeiro: periodo, grupo, bruta, impostos, liquida | Fluxos consolidados anuais ou acumulados 9M | Real; impostos sobre serviços não são carga líquida após créditos |
| financeiro: lair, ir, lucro | LAIR, despesa corrente+diferida positiva, lucro líquido | Real; alíquota adaptada = ir/lair; não é tributo pago |
| creditos: data, icms, pis, irrf, outros, total, circulante, nao_circulante | Estoques consolidados por data | Real; não somar datas, não equivale a caixa |
| icms_uf: uf, anterior, atual | Subtotal circulante RJ/SP da nota | Real; MG ausente no quadro não é zero; diferença não rateada |
| contingencias: exposicao, provisao | Posição divulgada | Real; provisão já integra exposição, não somar |
| reconciliacao: nominal, ajustes | Nota 33 em R$ mil; converter /1000 | Adaptado; ajustes reconhecidos não são novas oportunidades |
| complementos.historico_controladora | ano, receita, lair, ir, lucro, aliquota | 2022–2023 individual; alíquota derivada; tabela separada |
| complementos.conciliacao_9m | periodo, escopo, receita, lair, ir, lucro, versao | CVM acumulada janeiro–setembro; maior versão |
| complementos.dirbi.registros | ano, uf, programa, tributo, valor | Adaptado; valor declarado /1.000.000; chave CNPJ/UF/município/programa/tributo/ano na coleta |
| complementos.operacional | periodo, volume, investimentos, fonte | Real publicado; volume em mil TU, investimentos em R$ mi; conceito gerencial |
| fontes | id, nome, url, localizador, natureza, periodo, escopo, unidade | Catálogo e trilha documental; campos adicionais quando disponíveis |
| regras.mjs | titulo, status, fundamento, link, data comum de verificação | Regras gerais e anúncios; não parecer de elegibilidade |
| Cenários | entradas editáveis no navegador | Sintético; híbrido quando usa valor público; não gravado no servidor |

Especificações: REGRAS_E_CENARIOS.md e src/calculos.mjs. Fixtures em tests/fixtures_cenarios.json, conferidas por JavaScript e Python. Uma reconstrução futura em Power BI poderá usar tabelas e fórmulas equivalentes; não há arquivo Power BI ou conversor implementado. A síntese impressa é da página selecionada, não geração de PowerPoint.
