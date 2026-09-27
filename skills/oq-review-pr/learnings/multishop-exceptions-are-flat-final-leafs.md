---
status: active
dimension: domain-integrity
date: 2026-09-25
---

# Multishop domain exceptions are `final` leaf classes — catch-ordering analysis can stop at the `extends` clause

Why: every exception under cms/packages/Multishop and cms/packages/Contracts/Multishop extends `CheckedException extends \Exception` directly and is `final`, so no catch can shadow another and regrouping a multi-catch never changes semantics. Verify the `extends` line and stop; don't re-derive the whole hierarchy per PR.
Evidence: PR shoptet/cms4#45383, cms/packages/Multishop/Domain/DomainRedirection/Exception/*.php, cms/packages/Contracts/Multishop/**/Exception/*.php.
