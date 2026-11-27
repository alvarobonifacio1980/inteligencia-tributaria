# Inteligência Tributária — V2.1

Planejamento estratégico e eficiência fiscal. Estudo independente aplicado a uma empresa ferroviária, sem vínculo institucional. Dados públicos e simulações identificadas; sem dados internos ou promessa de economia.

Acesso público: https://alvarobonifacio1980.github.io/inteligencia-tributaria/

## Produto

Cinco módulos: visão executiva, diagnóstico, eficiência, reforma tributária e cenários/projetos. Fontes e metodologia transversais. Filtros temporais coerentes, composição de créditos, reconciliação de IRPJ/CSLL, simuladores de antecipação, parcelamento de ICMS, CAPEX/REIDI/REPORTO e sensibilidade ao consumo, fichas de business case, CSV e impressão da página selecionada.

## Execução

Node 24; Python 3.12; `pdftotext` (poppler-utils). Dependências gratuitas e versões fixadas.

```sh
npm ci
python -m pip install -r requirements.txt
python scripts/coletar.py           # baixa PDFs e valida âncoras e tabelas; conserva base se falhar
python scripts/cvm.py               # conciliação por CNPJ/conta com Pandas
python scripts/ampliar_fontes.py     # CVM 2022–23/9M e DIRBI; exige PDFs extraídos
python scripts/evoluir_v2.py --online # DIR/DIP, DVA/DFC, riscos e referências; exige cache CVM/PDF
python -m unittest discover -s tests -p 'test_*.py'
npm test
npm run dev
npm run build
```

`python scripts/coletar.py --offline` valida o snapshot revisado e gera o JSON de publicação. Não inventa novas competências. Uma mudança nos documentos que invalide os valores esperados exige revisão do mapeamento: o coletor interrompe em vez de atualizar silenciosamente. Notas explicativas foram transcritas e conferidas por escopo; a automação não interpreta alterações contábeis ou legais.

## Publicação e custo

GitHub Pages a partir de GitHub Actions, repositório público, runners padrão Ubuntu. Nenhum serviço contratado, cartão, domínio pago ou agendamento recorrente. Build em push; coleta por execução manual. O workflow de coleta gera evidências por 7 dias e não altera automaticamente dados revisados. Sem servidor, banco ou API própria.

## Dados

DFP Empresa Ferroviária 2025 (comparativo 2024), ITR 3T2026 (comparativo 9M2025), CVM DFP 2023/2025, ITR 2026 e DIRBI 2024. Histórico 2022–2023 segregado como controladora; demais dados financeiros consolidados., valores normalizados em R$ milhões; precisão de R$ mil nos arquivos. Fontes e localizadores em `data/base_revisada.json`, hashes em `data/coletas.json`, conciliação em `data/conciliacao_cvm.json`.

## Limitações

ANTT sem integração validada; indicadores operacionais publicados pela empresa como alternativa identificada. DIRBI 2024 integrada, sem equiparar declaração a caixa. REIDI/REPORTO com simulação condicional, sem afirmar elegibilidade de aquisição real. Simulador de reforma é sensibilidade econômica simplificada, com substituição federal e transição estadual/municipal explícitas, não cálculo legal de recolhimento. Sem projeções de margem/EBITDA nem economia atribuída à Empresa Ferroviária. Não há Power BI, PowerPoint ou conversores.

Consulte [status](docs/STATUS.md), [backlog](docs/BACKLOG.md), [testes](docs/TESTES.md), [metodologia](docs/METODOLOGIA.md) e [roadmap original](docs/ROADMAP_V1.md).

Coleta ampliada: hashes e conciliação em `data/conciliacao_expandida.json`; base complementar em `data/complementos_revisados.json`. O workflow manual gera artefato revisável; não faz commit automático. `scripts/preparar_base.py` apenas valida a base canônica, evitando regressão. Regras e fórmulas: [REGRAS_E_CENARIOS.md](docs/REGRAS_E_CENARIOS.md).

Se o portal DIRBI bloquear o runner, o workflow usa `--permitir-snapshot-dirbi`: mantém os registros de 2024 já revisados, emite aviso e registra reutilização/motivo com o hash e a data da coleta original. Não declara download novo. As fontes CVM continuam conciliadas; divergências contábeis ou arquivo DIRBI válido porém incoerente interrompem a execução. Execução direta sem essa opção permanece estrita.

V2.1: DVA/DFC, compensações, riscos recentes, DIR/DIP, comparações recentes, subabas/hash, cenários CAPEX/contratos e business cases ligados aos cálculos. Ver [confronto requisito a requisito](docs/ACEITE_V2.md), [testes V2](docs/TESTES_V2.md) e [roadmap publicável](docs/ROADMAP_V2_1.md). Sem novo módulo principal ou mudança de URL. A biblioteca anterior permanece testada; a interface da reforma privilegia regime pleno, com CAPEX independente.
