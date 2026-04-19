# Roadmap: Grãos Institucional

## Overview

Esta roadmap cobre o próximo ciclo de evolução do site institucional da Grãos S.A. Partimos de um produto já em produção, com catálogo e admin existentes, e organizamos o trabalho restante em quatro fases: sanear dados do catálogo, endurecer mídia/SEO, tornar captação mais confiável e fechar lacunas de segurança operacional no admin.

## Phases

- [ ] **Phase 1: Catálogo Confiável** - Completar e normalizar os dados críticos do catálogo ativo.
- [ ] **Phase 2: Mídia e SEO Resilientes** - Corrigir a camada de imagens, qualidade visual e indexação.
- [ ] **Phase 3: Captação Auditável** - Fazer o fluxo de leads gerar resultado real e verificável.
- [ ] **Phase 4: Admin Endurecido** - Reduzir riscos operacionais e de segurança no painel administrativo.

## Phase Details

### Phase 1: Catálogo Confiável
**Goal**: Garantir que o catálogo ativo esteja consistente em conteúdo, mídia associada e dados comerciais essenciais.
**Depends on**: Nothing (first phase)
**Requirements**: CAT-01, CAT-02, CAT-03
**Success Criteria** (what must be TRUE):
  1. Produtos ativos não exibem imagem quebrada, slug inconsistente ou categoria inválida.
  2. O time consegue identificar com clareza quais produtos ainda carecem de apresentação ou mídia.
  3. Seed, banco e catálogo público deixam de divergir nos campos essenciais.
**Plans**: 2 plans

Plans:
- [ ] 01-01: Auditar integridade do catálogo e mapear lacunas por produto.
- [ ] 01-02: Corrigir dados comerciais essenciais e alinhar base/seed/admin.

### Phase 2: Mídia e SEO Resilientes
**Goal**: Tornar o pipeline de imagem previsível em desenvolvimento e produção, sem perder qualidade nem indexação.
**Depends on**: Phase 1
**Requirements**: MID-01, MID-02, MID-03
**Success Criteria** (what must be TRUE):
  1. Uploads novos e legados servem URLs válidas em todos os ambientes suportados.
  2. Robots, sitemap e serving de imagens deixam de se contradizer.
  3. O pipeline não faz upscale desnecessário em imagens quadradas ou recortadas.
**Plans**: 2 plans

Plans:
- [ ] 02-01: Corrigir pipeline e serving de imagens.
- [ ] 02-02: Ajustar SEO técnico relacionado a mídia e cache.

### Phase 3: Captação Auditável
**Goal**: Transformar os pontos de contato em canais reais de captação com rastreabilidade mínima.
**Depends on**: Phase 2
**Requirements**: LEAD-01, LEAD-02, LEAD-03
**Success Criteria** (what must be TRUE):
  1. CTA principal continua funcional e configurável por settings.
  2. O formulário de contato produz um resultado operacional real para o negócio.
  3. Eventos de conversão continuam mensuráveis sem gerar falsas confirmações ao usuário.
**Plans**: 2 plans

Plans:
- [ ] 03-01: Implementar destino real para o formulário de contato.
- [ ] 03-02: Revisar tracking e feedback de conversão.

### Phase 4: Admin Endurecido
**Goal**: Fechar lacunas básicas de segurança e operação no painel sem descaracterizar a simplicidade do sistema.
**Depends on**: Phase 3
**Requirements**: ADM-01, ADM-02, ADM-03
**Success Criteria** (what must be TRUE):
  1. O admin não depende mais de segredos default inseguros em produção.
  2. Fluxos de escrita sensíveis possuem proteção mínima contra requests indevidos.
  3. A operação diária do catálogo continua simples para o time interno.
**Plans**: 3 plans

Plans:
- [ ] 04-01: Endurecer segredos e autenticação administrativa.
- [ ] 04-02: Adicionar proteção para formulários e ações de escrita.
- [ ] 04-03: Validar impacto operacional e ajustar UX do admin.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Catálogo Confiável | 0/2 | Not started | - |
| 2. Mídia e SEO Resilientes | 0/2 | Not started | - |
| 3. Captação Auditável | 0/2 | Not started | - |
| 4. Admin Endurecido | 0/3 | Not started | - |
