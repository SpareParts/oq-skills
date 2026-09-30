---
status: active
dimension: domain-integrity
date: 2026-09-30
---

# A strict_types addition to a pass-through handler is behaviour-preserving by construction when every scalar it passes originates from a natively-typed readonly DTO property — check the DTO once, not each call site

Why: strict mode only changes call-site coercion inside the edited file. When a handler merely forwards promoted, natively-typed (`int`/`bool`/`string`) properties of readonly Query/Command DTOs into typed repository/mapper parameters, the runtime types are already exact when read, so no call site can newly throw; array-typed parameters have no call-boundary coercion semantics in either mode. Verify the Query DTO property declarations once instead of re-deriving per call site.
Evidence: shoptet/cms4#45505 review (MIN-17, 2026-09-30) — all 9 changed handlers checked against `SalesChannelReadRepository::findAll/findById/findByUuid/findByIds/findBy/findByType/findAllWithDeleted/findOnlyDeleted` + `SalesChannelDtoMapper` methods; zero risk sites.
