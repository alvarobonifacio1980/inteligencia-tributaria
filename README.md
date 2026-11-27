# Inteligência Tributária

Planejamento estratégico e eficiência fiscal. Estudo independente da MRS Logística, sem vínculo institucional. Dados públicos e simulações identificadas; sem dados internos ou promessa de economia.

## Produto

Cinco módulos: visão executiva, diagnóstico, eficiência, reforma tributária e cenários/projetos. Fontes e metodologia transversais. Filtros temporais coerentes, composição de créditos, reconciliação de IRPJ/CSLL, simuladores de antecipação e de sensibilidade ao consumo, fichas de business case, CSV e impressão da página selecionada.

## Execução

Node 24; Python 3.12; `pdftotext` (poppler-utils). Dependências gratuitas e versões fixadas.

```sh
npm ci
python -m pip install -r requirements.txt
python scripts/coletar.py           # baixa PDFs e valida âncoras; conserva base se falhar
python scripts/cvm.py               # conciliação por CNPJ/conta com Pandas
python -m unittest discover -s tests -p 'test_*.py'
npm test
npm run dev
npm run build
```

`python scripts/coletar.py --offline` valida o snapshot revisado e gera o JSON de publicação. Não inventa novas competências. Uma mudança nos documentos que invalide os valores esperados exige revisão do mapeamento: o coletor interrompe em vez de atualizar silenciosamente. Notas explicativas foram transcritas e conferidas por escopo; a automação não interpreta alterações contábeis ou legais.

## Publicação e custo

GitHub Pages a partir de GitHub Actions, repositório público, runners padrão Ubuntu. Nenhum serviço contratado, cartão, domínio pago ou agendamento recorrente. Build em push; coleta por execução manual. O workflow de coleta gera evidências por 7 dias e não altera automaticamente dados revisados. Sem servidor, banco ou API própria.

## Dados

DFP MRS 2025 (comparativo 2024), ITR 3T2026 (comparativo 9M2025), CVM DFP 2025. Consolidado, valores normalizados em R$ milhões; precisão de R$ mil nos arquivos. Fontes e localizadores em `data/base_revisada.json`, hashes em `data/coletas.json`, conciliação em `data/conciliacao_cvm.json`.

## Limitações

ANTT e DIRBI sem integração validada. REIDI/REPORTO qualitativos até confirmar elegibilidade. Histórico 2022–2023 pendente. Simulador de reforma é sensibilidade econômica simplificada, com aproximação de transição visível, não cálculo legal de recolhimento. Sem projeções de margem/EBITDA nem economia atribuída à MRS. Não há Power BI, PowerPoint ou conversores.

Consulte [status](docs/STATUS.md), [backlog](docs/BACKLOG.md), [testes](docs/TESTES.md), [metodologia](docs/METODOLOGIA.md) e [roadmap original](docs/ROADMAP_V1.md).
