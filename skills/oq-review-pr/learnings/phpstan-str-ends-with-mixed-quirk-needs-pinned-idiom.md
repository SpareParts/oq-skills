---
status: active
dimension: code-quality
date: 2026-10-09
---

# A rewrite dodging PHPStan's str_ends_with-as-mixed inference needs an on-site trail or a pinned package idiom — else a future "simplification" silently re-adds the baseline entry

Why: this PHPStan build infers `str_ends_with()` as mixed while `str_starts_with()`/`str_contains()` infer bool, so `: bool` methods using it need a workaround. cms4's Multishop package now carries three divergent idioms for that one gap: `@phpstan-ignore possiblyImpure.functionCall` (ZoneRecordName.php:45-46), `=== true` (InternalDomainSalesChannelIdResolver.php:57 — keeps the stdlib call and clears L10), and substr offset arithmetic (NormalizedDomain.php:99-103). Each is locally correct; none says on-site why `str_ends_with` is absent, so the next reader "simplifies" back and the deleted `return.type` baseline entry re-fires. When reviewing or writing such a rewrite, either pin one idiom package-wide or leave the one-line directive; flag idiom divergence as a convention follow-up, not a blocker.
Evidence: shoptet/cms4#46019 review (2026-10-09, task MIN-45); cms/packages/Multishop/Domain/Dns/Model/Domain/NormalizedDomain.php:99-103; counterfactual L10 probes of all three idioms.
