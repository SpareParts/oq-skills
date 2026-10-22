---
status: active
dimension: general
date: 2026-10-06
---

# A PR body's "complete inventory, re-verified by grep" claim is itself a reviewable artifact — recount its numbers against the diff, never by trusting the prose

Why: recount mechanically (e.g. `git diff | grep -c` on the removed/added lines): in the evidence PR the body claimed 7 same-namespace `use` removals (including one import that never existed on master — the file already used an unqualified `::class` reference) and 13 NEON registration changes, while the diff contained exactly 6 and 15. The code was correct; only the prose count was wrong. Wrong counts in a "complete inventory, re-verified" claim undermine every other verification claim the body makes, and mechanical recounting catches them for free. A subtler variant is a count that is correct as a total but misattributed ("49 imports of the old FQN rewritten" when 49 is the total of changed sites and only 47 were old-FQN rewrites) — recount by category (rewrites / new imports / in-file-of-deleted), not only by total, and check the sentence's attribution, not just its arithmetic. Counts of the pre-existing code state ('12 of 17 sites pass it') are the same failure without a diff: the recount must name its counting frame, because the conclusion can be true while the figure is wrong.
Evidence: shoptet/cms4#45783 (task MIN-33, review 2026-10-06) — body claims vs diff counts (6 use-removals, 15 NEON changes).
Evidence: shoptet/cms4#46018 (task MIN-45, review 2026-10-09) — "49 rewrites" was 47 rewrites + 2 new imports.
Evidence: shoptet/cms4#46805 review (task MIN-107, 2026-10-22) — "12 of 17 sites do" matched no counting frame (23 catch-and-log sites / 17 catch(Throwable) sites / 18 catch+logger->error sites all give different figures); counts of the PRE-EXISTING code state need a stated counting frame, not only diff counts — the conclusion was independently true while the figure was wrong.
