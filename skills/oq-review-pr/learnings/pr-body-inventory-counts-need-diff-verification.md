---
status: active
dimension: general
date: 2026-10-06
---

# A PR body's "complete inventory, re-verified by grep" claim is itself a reviewable artifact — recount its numbers against the diff, never by trusting the prose

Why: recount mechanically (e.g. `git diff | grep -c` on the removed/added lines): in the evidence PR the body claimed 7 same-namespace `use` removals (including one import that never existed on master — the file already used an unqualified `::class` reference) and 13 NEON registration changes, while the diff contained exactly 6 and 15. The code was correct; only the prose count was wrong. Wrong counts in a "complete inventory, re-verified" claim undermine every other verification claim the body makes, and mechanical recounting catches them for free.
Evidence: shoptet/cms4#45783 (task MIN-33, review 2026-10-06) — body claims vs diff counts (6 use-removals, 15 NEON changes).
