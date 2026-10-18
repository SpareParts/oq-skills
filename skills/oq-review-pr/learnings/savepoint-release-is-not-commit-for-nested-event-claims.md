---
status: active
dimension: domain-integrity
date: 2026-10-18
---

# A batch write inside an outer orchestrator transaction that claims "event dispatched only after commit" must say which commit

Why: `BaseDatabase::runInTransaction` commits its own nesting level, and under `nest_transactions` that is a SAVEPOINT release when the call is nested — so the "after commit" event fires before the outer transaction actually commits. The pattern is benign only when every subscriber's writes re-join the same connection / outer transaction (check `getSubscribedEvents` and the subscriber's own `runInTransaction`); otherwise an event can survive a rolled-back outer transaction while its writes are discarded — a phantom event. When a PR body claims a dispatch happens "only after commit", cite the path explicitly (top-level transaction vs nested savepoint) rather than leaving the blanket phrasing that overclaims on the nested path.

Evidence: shoptet/cms4#46565 (task MIN-85) — the review read `BaseDatabase.php:22-82` in full, verified the single subscriber (`SyncOptionsToGlobalSubscriber`) re-joins the outer transaction, and flagged the blanket "after commit" phrasing as overclaiming on the wizard path.
