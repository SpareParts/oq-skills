---
status: active
dimension: domain-integrity
date: 2026-10-12
---

# Before claiming "callers believe the write succeeded", read each caller's pre-read null handling at HEAD, not at the base

Why: a fail-loud PR's problem statement is usually written against the base's line numbers, and the "phantom success" motivation drifts stale by the time the PR reaches review. At head, a caller may already null-check its own pre-read — an orchestrator that gates the follow-up event on `$salesChannel !== null` never records a phantom success — so the claimed motivation applies to fewer callers than the body says. Callers that throw their own not-found before the dispatch make the new throw nearly unreachable for them (defense in depth), not the fix the body claims to need. Recount BOTH the citations (line numbers, method names) AND the motivation against the pinned head; otherwise the PR body oversells the bug it fixes, and a reviewer who verifies only the diff cannot tell the difference.
Evidence: shoptet/cms4#46107 vs `cms/packages/Multishop/Application/Market/MarketSettings/Orchestration/MarketSettingsSubmitOrchestrator.php:232-236` at head (task MIN-54, review 2026-10-12) — the orchestrator already null-tolerates the pre-read, and `InStoreSalesChannel`/`CashDesk` throw their own not-found before the dispatch. Distinct from `pr-body-line-citations-drift-after-automated-resort` (the PR's own tools re-sort lines) and `pr-body-inventory-counts-need-diff-verification` (wrong totals).
