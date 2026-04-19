# Requirements: Grãos Institucional

**Defined:** 2026-04-19
**Core Value:** Catálogo de produtos atualizado e acessível que converte visitantes em contatos de WhatsApp para vendas B2B ao por mayor.

## v1 Requirements

### Catálogo e Conteúdo

- [ ] **CAT-01**: Todo produto ativo deve exibir imagem válida, nome, categoria e slug público funcional.
- [ ] **CAT-02**: Todo produto ativo deve exibir apresentação comercial quando essa informação existir na base.
- [ ] **CAT-03**: O catálogo deve refletir as prioridades da Curva ABC sem inconsistências visíveis entre seed, banco e admin.

### Mídia e Performance

- [ ] **MID-01**: Uploads do admin devem gerar imagens otimizadas e servir URLs válidas tanto em desenvolvimento quanto na Railway.
- [ ] **MID-02**: O site deve evitar regressões de indexação de imagens entre `/static/uploads` e `/uploads`.
- [ ] **MID-03**: Hero e imagens de produto devem manter qualidade aceitável sem upscale desnecessário.

### Captação de Leads

- [ ] **LEAD-01**: Toda CTA pública relevante deve levar a um número de WhatsApp configurável nas settings.
- [ ] **LEAD-02**: O formulário de contato deve gerar um resultado real e auditável para o time comercial.
- [ ] **LEAD-03**: Eventos principais de conversão devem permanecer rastreáveis sem quebrar a UX.

### Admin e Operação

- [ ] **ADM-01**: O painel admin deve continuar permitindo CRUD de categorias, produtos e configurações sem depender de ferramentas externas.
- [ ] **ADM-02**: A autenticação administrativa deve deixar de depender de credenciais default inseguras.
- [ ] **ADM-03**: Fluxos administrativos de escrita devem ter proteção mínima contra ações indevidas e regressões básicas.

## v2 Requirements

### Expansão

- **EXP-01**: Adicionar workflow de importação em lote para novos produtos e mídia.
- **EXP-02**: Disponibilizar métricas de catálogo e leads diretamente no admin.
- **EXP-03**: Evoluir o contato para integrações externas como e-mail transacional ou webhook comercial.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Checkout e carrinho | O modelo comercial atual fecha via WhatsApp e atendimento B2B |
| Conta pública de cliente | Não faz parte da proposta institucional atual |
| SPA/frontend com build | A stack atual privilegia simplicidade operacional em Flask SSR |
| Blog/editorial pesado | O foco do produto é catálogo e conversão, não conteúdo recorrente |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CAT-01 | Phase 1 | Pending |
| CAT-02 | Phase 1 | Pending |
| CAT-03 | Phase 1 | Pending |
| MID-01 | Phase 2 | Pending |
| MID-02 | Phase 2 | Pending |
| MID-03 | Phase 2 | Pending |
| LEAD-01 | Phase 3 | Pending |
| LEAD-02 | Phase 3 | Pending |
| LEAD-03 | Phase 3 | Pending |
| ADM-01 | Phase 4 | Pending |
| ADM-02 | Phase 4 | Pending |
| ADM-03 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0

---
*Requirements defined: 2026-04-19*
*Last updated: 2026-04-19 after GSD brownfield initialization*
