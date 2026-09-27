---
status: active
dimension: general
date: 2026-09-26
---

# Chained zod checks surface the first failing check per field, mirroring BE Assert\Sequentially

Why: In admin-web (zod 4.3.6 + @hookform/resolvers 5.4.0, criteriaMode firstError), a chain like `.min().max().regex().regex()` collects all issues but the resolver maps the FIRST issue per field to `error.message`. A reviewer seeing "multiple regex checks could produce two errors on one input" should not flag it: the FE effectively shows one message, in the same priority order as the BE `Assert\Sequentially` compound. Verified empirically for shoptet/cms4#45366.
Evidence: PR shoptet/cms4#45366, frontend/apps/admin-web/src/MultiShop/pages/ConnectCustomDomain/createDomainFormSchema.ts.
