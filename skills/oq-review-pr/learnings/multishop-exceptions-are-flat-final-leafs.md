---
status: active
dimension: domain-integrity
date: 2026-09-25
---

# Multishop domain exceptions are `final` leaf classes — catch-ordering analysis can stop at the `extends` clause

Why: every exception under cms/packages/Multishop extends its `CheckedException extends \Exception` directly and every one under cms/packages/Contracts/Multishop extends a separate `CheckedException extends \RuntimeException` (see `two-checkedexception-bases-differ.md`); all are `final`, so no catch can shadow another and regrouping a multi-catch never changes semantics. Verify the `extends` line and stop; don't re-derive the whole hierarchy per PR.
Evidence: PR shoptet/cms4#45383, cms/packages/Multishop/Domain/DomainRedirection/Exception/*.php, cms/packages/Contracts/Multishop/**/Exception/*.php.
