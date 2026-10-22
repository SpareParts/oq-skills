---
status: active
dimension: general
date: 2026-10-22
---

# A cms4 NEON parameter list merges by APPENDING — an override needs the `!` suffix, and a quoted integer silently disables a strict in_array gate

Why: Nette merges parameter lists by appending, so a config.local.neon override of e.g. `newRoutingProjectIds: [222222]` yields the default PLUS the new value, and a plain `newRoutingProjectIds: []` yields the unchanged default (the merge loop never runs) — an attempted rollback by "setting an empty list" does nothing. Full replacement needs `newRoutingProjectIds!: []` (verified: gives []). In the same gate, a quoted NEON ID ('159821') stays a string and strict in_array(int, [string], true) never matches — the project silently stays on the old path; IDs must stay unquoted integers. Verified empirically in the review by three config.local.neon merge experiments.
Evidence: shoptet/cms4#46804 rollout-gate review (task MIN-106, 2026-10-22) — config/app/multishop-services.neon:2-6, MarketDetectionMiddleware.php:46.
