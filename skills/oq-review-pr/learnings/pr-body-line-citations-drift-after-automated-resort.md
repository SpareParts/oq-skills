---
status: active
dimension: general
date: 2026-10-08
---

# PR-body file:line citations go stale after the PR's own automated re-sorts — recount them at the head

Why: a PR that triggers phpcbf/use-block re-sorting changes the line numbers of exactly the use-import lines its own reference list cites, so a "re-verified by grep" inventory can mix base-state and head-state citations (shoptet/cms4#45996: body cited the orchestrator use at :42 and the test use at :10 — head had :38 and :9 after the alphabetical re-sort, and at head the cited test line pointed at the WRONG import; the Problem section even mixed :168 base-state and :169 head-state for the same throw). The code is fine; the record lies. Extends pr-body-inventory-counts-need-diff-verification (counts) to line citations: recount every cited file:line against the HEAD revision, not the branch point.
Evidence: shoptet/cms4#45996 head 594f26279c vs merge-base eaf8bc5758 (task MIN-41, review 2026-10-08) — MarketSettingsSubmitOrchestrator.php use block, SetMarketAsPrimaryCommandHandlerTest.php use block.
