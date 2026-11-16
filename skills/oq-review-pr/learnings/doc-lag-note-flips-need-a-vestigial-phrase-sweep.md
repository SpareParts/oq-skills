---
status: active
dimension: general
date: 2026-10-13
---

# When a PR updates a doc's "deployed code lags the rule" note because the code caught up, sweep the whole doc for phrases whose *reason* expired — not just the note line

Why: phrases like "shown with the required `final`" are meaningful only while the deployed code differs from the example; once the code catches up (examples become byte-exact with the deployed files), the qualifier describes an amendment that no longer exists and reads as a leftover contrast next to the corrected note. A "line N was the only stale spot" PR-body claim is therefore reviewable the same way as a count claim: grep the full doc for wording contingent on the old state (contrast markers: "shown with", "unlike the deployed", "still", "predate", "already complies"), not only for restatements of the rule.
Evidence: shoptet/cms4#46216 review (MIN-64, 2026-10-13) — queries-and-commands.md:57/:81 "shown with the required `final`" vs the corrected note at :53; examples byte-exact with GetMarketsQuery.php / GetMarketsQueryHandler.php since a894f6a37f (#45695).
