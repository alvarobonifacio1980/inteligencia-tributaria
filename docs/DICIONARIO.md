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

## Extensão V2.1

| Estrutura | Campos / unidade | Natureza / interpretação |
|---|---|---|
| v2.dva | periodo, federal/estadual/municipal/total, R$ mi | Valores publicados; participações derivadas; negativo preservado |
| v2.dfc | periodo, original_mil, valor magnitude em R$ mi | Adaptado só na inversão/conversão de sinal; pagamentos, não despesa |
| v2.compensacoes | ano, valor R$ mi | Fluxo de tese específica, não todas as compensações |
| v2.riscos | data, possivel/provavel/total, processos/recuperacao/risco/provaveis | Posição por data; possível recente = total−provável |
| v2.temas_risco_2025 | tema, valor R$ mi | Temas selecionados da perda possível anual, não nova exposição |
| v2.dir / v2.dip | codigo, classe, ano, valor_reais, original, fonte, localizador, natureza, escopo | Inteiros em reais; realizado separado de previsto; null preserva traço |
| v2.totais_dip / total_dir | total por ano e realizado em R$ | Somatório de classes oficiais; sem inferir execução cruzada |
| v2.custos_referencia | grupos contábeis, total R$ mi, avaliação, período/fonte | Escala contábil, fração elegível hipotética; não base fiscal |
| v2.reconciliacao_9m | periodo, nominal, ajustes, efetivo R$ mi | Notas consolidadas, acumulado janeiro–setembro |
| v2.tarifas | fixa R$/t, variável R$/t.km, exemplo/cache/ato/vigência | Teto de referência arquivado; sem ICMS, não preço efetivo |
| v2.inspecao_planilhas | dimensões, proteção, fórmulas, nomes, links, macros | Metadados auditáveis, sem executar macros ou republicar arquivos |

Estado dos cenários mantido no React durante navegação da sessão, sem servidor. Defaults e funções independentes dos gráficos; fixtures compartilhadas em fixtures_v2.json.
