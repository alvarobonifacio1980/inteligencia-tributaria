# Status — 27/11/2026

Aplicação ampliada publicada: https://alvarobonifacio1980.github.io/inteligencia-tributaria/

## Implementação ampliada — 27/11/2026

Registro mais recente prevalece sobre lacunas históricas descritas acima. Implementados histórico controladora 2022–2023, IR/CS consolidado 9M, DIRBI 2024 (12 registros), contexto operacional, agenda regulatória com status, fluxo ICMS, comparação CAPEX com/sem suspensão e sensibilidade 2026–2033. A reforma separa substituição federal e legado estadual/municipal, créditos utilizados e excedentes; não transforma excedentes em caixa.

Matriz qualitativa e três business cases ampliados; habilitação apenas hipotética nos simuladores, sem afirmar direito real. Preservados cascata, MG não detalhado, fontes clicáveis e explicações Adaptado. 19 testes (11 JS + 8 Python) e build aprovados; navegador desktop e viewport móvel, seis páginas sem overflow global. Testes/publicação final em TESTES.md. ANTT e documentos internos permanecem limites explícitos; não caracterizam números inventados ou promessas de benefício.

## Publicação e preservação

Commit funcional `17fa4c4eb3ec1fa55006cf037888ae61da8628b6`; validação e deploy aprovados no run `46040278129`. Acesso público sem autenticação confirmado por GET de HTML/JS/CSS/JSON com HTTP 200 e navegação no painel publicado. Cenário CAPEX confirmou R$ 0,28 mi no exemplo e R$ -0,20 mi com crédito alternativo imediato, evitando falsa economia.

Pipeline manual: primeira execução ampliada encontrou conexão encerrada pelo portal DIRBI. Download foi corrigido com novas tentativas, validação ZIP e cliente TLS alternativo mantendo certificados. Nunca substitui snapshot por arquivo parcial. Reexecução confirmou bloqueio TLS no runner. Workflow preserva snapshot DIRBI de 2024 com aviso explícito, hash/data original e flag de reutilização, sem declarar nova coleta. CVM e testes continuam. Reexecuções registradas em TESTES.md.

Identidade genérica, cores, gráficos nativos, fontes clicáveis e janelas de adaptação preservados. Nenhum outro repositório alterado; nenhuma contratação ou contato externo. Sem Power BI/PowerPoint/conversores neste escopo.

Etapas 00–10 atendidas no escopo demonstrativo validado, com limites em BACKLOG.md. Atualizações não são apuração legal universal nem diagnóstico de dados internos. Revisar documentação interna antes de decisão real.
