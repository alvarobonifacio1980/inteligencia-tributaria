# Validação V2.1 — 27/11/2026

Ambiente: Node 24, Python 3.12 (runtime analítico com Pandas/openpyxl), Chrome cloud. Mantidos os testes da V1.

## Automatizados

- 23 testes JS aprovados: VP original, transição legada preservada na biblioteca, excedentes, CAPEX condicional, fluxo ICMS, novos CAPEX/contratos e fixtures, CBS 0/100, vazio/inteiro, natureza, LAIR não aplicável, ponte com cruzamento de zero, alteração de fixture e CSV seguro.
- 15 testes Python aprovados: originais e novas somas DIR/DIP, traços/zero, DVA e sinal negativo, DFC com valor original, riscos sem duplicação, reconciliações 9M e fórmulas independentes.
- Build Vite aprovado; pacote cerca de 845 kB / 279 kB gzip, sem fonte externa ou mídia obrigatória. Medição de prontidão separada de tamanho do pacote.
- scripts/evoluir_v2.py executado sobre arquivos oficiais válidos, confrontando CVM e PDFs; data/conciliacao_v2.json contém hashes, valores e inspeção das planilhas.
- Script não é um parser universal: valores de controle e mapeamentos exigem revisão diante de novo documento/versão. Divergência de conteúdo interrompe; falha de conectividade pode preservar snapshot com aviso e motivo, se opção explícita.

## Fontes e inspeção

DIR/DIP: página única renderizada e conferida visualmente; inteiros e notas originais preservados. Apresentação 3T26 p.6 renderizada, p.17 extraída/conferida; cores de comparação e rótulos influenciaram ajustes incrementais, sem copiar marca ou slides.

DFC consolidada ITR p.30 (não p.28, que é controladora); DVA ITR p.33 (não p.32, controladora). DVA anual DFP p.46. Valores conciliados à CVM com CNPJ, maior versão, moeda REAL, escala MIL e período acumulado correto. Planilhas sem execução de macros; nenhum vínculo externo encontrado. E16 = arredondar(fixa + variável × distância, 2) reproduz o cache, sem ICMS. Campo de vigência conservado sem inventar início/fim de validade.

## Funcional e visual executado

- V1 pública mantida enquanto a V2 era inspecionada localmente; baseline a961724.
- Visão executiva inicia 9M2026; filtro 2025 e nove meses preserva séries equivalentes; alíquota recente 33,10% e diferença 5,62 p.p.
- Reconciliação anual preservada; seleção 9M2026 apresentou 428,676 mi; detalhamento separado dos ajustes anuais.
- Créditos: campo vazio gerou aviso e conservou o último resultado válido, sem zero implícito.
- Reforma: receita pública tornou Híbrido; editar referência para 100 restaurou Sintético; CBS zero apresentou cenários 0/0/2 sem travamento.
- CAPEX: seleção Material Rodante/2028 vinculou 256,512139 mi e impediu edição; modal abriu com valor, transformação, fórmula e fonte; Escape fechou.
- Navegação por hash, Voltar/Avançar e título testados; estado dos cenários preservado na navegação da sessão.
- 390×844 por iframe: seis subabas de diagnóstico, duas de eficiência, matriz, reforma plena, CAPEX, contratos, business cases e fontes verificadas com largura útil 375 px e scrollWidth=clientWidth=375. Capturas executivas e de controles móveis inspecionadas. Não equivale a aparelho físico.
- Logs consultados até aqui: erros observados eram de extensão Chrome, não da origem da aplicação.

## Gates finais

Desktop 1366/1920, estilo de impressão, CSV efetivamente baixado, desempenho, CI da branch e acesso público após deploy: registros acrescentados conforme verificação; não presumir aprovação por implementação.

Sem teste em Safari/Firefox ou dispositivo físico; não se alega auditoria integral de operações reais.
