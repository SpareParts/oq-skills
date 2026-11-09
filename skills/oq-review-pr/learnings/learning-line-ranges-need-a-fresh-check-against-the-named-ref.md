---
status: active
dimension: general
date: 2026-11-09
---

# A learning's cited line range is re-checked against the named ref before it lands, and cites the load-bearing line, not a neighborhood

Why: hand-copied ranges drift — either approximate at write time or stale after the cited file
moves — and a future reviewer who lands one line off starts doubting the whole learning.
Cite the smallest range that still shows the mechanism (the condition line for a branch, not a
band around it), and re-derive the numbers from the ref the text names before committing.
Evidence: MIN-188 review of SpareParts/oq-skills#39 —
`permission-403-test-must-enable-the-page-module.md` originally cited `PageAdmin.php:236-238` for
the inactive-module branch whose condition sits at 235 (comment 236, `allowedAccess = true` 237) on
cms4 master; the neighboring `pr-body-line-citations-drift-after-automated-resort.md` covers
automated resort drift, a different mechanism.
