---
status: active
dimension: general
date: 2026-10-11
---

# Recount "N usage sites" claims by diffing identifier reads, not constant deletions

Why: a PR body that deletes a handful of constants and claims "10 usage sites" converted is routinely wrong in both directions — the author counted the constants, or every docblock mention, instead of the actual `self::CONST` reads. A wrong count misleads the reviewer's completeness check ("were any usages missed?"), which is the very check the inventory exists to support. Recount mechanically: `git grep -c 'self::<NAME>'` on the base for each deleted identifier, then confirm zero remain at the head; the converted reads, not the deleted declarations, are what the claim counts. Distinct from `pr-body-inventory-counts-need-diff-verification` (which recounts diff totals): this trap is counting the wrong thing — identifier reads vs deletions — even when the arithmetic on the wrong thing is correct.
Evidence: shoptet/cms4#46102 (MIN-51, review 2026-10-11) — body said 10 usage sites; the diff converts 7 sites / 8 property reads (master DomainRoutingAuditJob.php:331,333,334,339,342,346,525).
