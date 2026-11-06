---
status: active
dimension: general
date: 2026-11-06
---

# An endpoint-documentation PR that registers error codes "answered by these endpoints only" must grep the whole repository for other emitters of those code strings before "only" ships

Why: wire error codes are shared vocabulary, not per-endpoint constants — the same literal is routinely produced by several response factories on other routes, so an exclusivity claim derived from the documented controllers' catch ladders alone is false. In the evidence PR two codes registered as exclusive were also emitted by two other endpoints through other factories, and the human review's fix was to drop "only" and name the overlap; before PR 1 of the evidence task consolidated them, the same literal lived in six factories. Grep the literal repo-wide (response factories included, not just the documented controllers) and write the overlap down, or keep the word "only" out of the sentence.
Evidence: shoptet/cms4#47636 at the reviewed head `aa6fbfe` (task MIN-172), human review 5794972733 — docs/multishop/endpoints.MD:527 at that head ("These codes are answered by the four endpoints above only") vs `UpdateMarketEmailManagementResponseFactory` and `WizardDnsRecordsResponseFactory` emitting the same codes on other routes.
