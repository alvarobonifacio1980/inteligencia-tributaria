# Status — Inteligência Tributária V2.1

Data de revisão: 27/11/2026. URL estável: https://alvarobonifacio1980.github.io/inteligencia-tributaria/

Baseline recuperável V1: a961724182664b0baef92c0eebea2a1432c8bf4c. Evolução na branch v2-melhorias; produção preservada durante desenvolvimento e validação. Gate pré-publicação aprovado: testes locais, inspeção funcional/visual e CI isolada aprovados. Publicação e verificação anônima registradas ao final.

Entregas antecipadas na V1 preservadas: financeiro 9M, histórico controladora, DIRBI, contexto operacional, regras, simuladores, matriz e business cases. Diferenças executadas: DVA/DFC, compensações, riscos recentes, DIR/DIP, executivo recente, gráficos e subabas, cenários CAPEX/contratos, origem dinâmica, exportação/impressão e casos calculados.

39 testes aprovados (23 JS + 16 Python); build aprovado; validações funcionais e móveis em TESTES_V2.md. Matriz de confronto requisito a requisito em ACEITE_V2.md. Limites de fontes e aplicação real em BACKLOG.md.

A modelagem visível da reforma usa regime pleno hipotético, com cronograma legal separado. Transição aproximada continua apenas na biblioteca legada testada, sem aparência de apuração real na interface. CAPEX independente do agregado; contratos são alternativa normalizada, nunca soma duplicada ao efeito da reforma. Suspensão específica exige hipótese explícita e validação documental.

Sem custo de infraestrutura contratado, contato externo, informação privada, alteração de outros repositórios, força sobre branch ou reescrita de histórico.

Coleta online ampliada aprovada no run 46046414220, sem reutilização de snapshot nessa execução. CI da branch aprovada no run 46046447545, sem deploy na branch. Snapshot inválido testado e rejeitado; 39 testes finais locais aprovados. Limitação visual: captura 1920 falhou por timeout, mas largura renderizada 1905/1905 sem overflow; desktop1366 e móvel inspecionados.

Integração aprovada via PR1; commit de release a23e86bf5f3c17d55a907732343b790078ae7d4d. Deploy automático run46047253655. Registro final HTTP e navegador concluído abaixo. Rollback: reverter o merge a23e86b por novo commit preservando histórico, ou construir o snapshot V1 do commit a961724. Nunca force push.

## Entrega publicada

V2.1.0 publicada e verificada. Release `a23e86bf5f3c17d55a907732343b790078ae7d4d`; run `46047253655` aprovado. Mesma URL pública, sem autenticação. Testes:39 (23 JS +16 Python); build, coleta online, inspeção visual/funcional, CSV e impressão conforme TESTES_V2.md. HTTP público e comparação dos assets em HTTP_PUBLICO_V2.json.

Pronta para avaliação gerencial, observados os limites de dados e simulação. Permanecem ANTT sem integração validada, comparação com sustentabilidade bloqueada por403, elegibilidade/operações internas não disponíveis e ausência de teste físico/Safari/Firefox. Captura1920 limitada por timeout; layout1366 e móvel inspecionados. Nenhum custo de infraestrutura contratado.
