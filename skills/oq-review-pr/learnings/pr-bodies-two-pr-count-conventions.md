---
status: active
dimension: general
date: 2026-11-06
---

# When one PR body narrates the same quantity in two places (problem statement and diff), recount both against the diff — the diff-true number must win in both places

Why: the Why section's motivating count and the change inventory are usually produced by two different conventions (call sites counted before the consolidation vs delegations after it), so each number can be internally defensible while the pair contradicts itself; a wrong motivating count is worse than a wrong inventory because it is the number the reader uses to judge whether the PR is worth reading. In the evidence PR the Why section said "33 call sites" while the diff carried 35 delegations, both describing the same removed duplication. Recount every figure the body attributes to the change and make both sentences use the diff-true one, or say explicitly which convention each uses. Extends pr-body-inventory-counts-need-diff-verification (merged; not amended) from single-inventory PRs to the Why section's motivating count.
Evidence: shoptet/cms4#47637 (task MIN-172) — "33 call sites" (Why) vs 35 `$this->errors->error(` delegations in the diff (9 Add, 10 Update, 6 Remove, 2 ZoneRecords, 4 Wizard, 4 UpdateMarketEmailManagement).
