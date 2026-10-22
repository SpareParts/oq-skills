---
status: active
dimension: domain-integrity
date: 2026-10-21
---

# An event dispatched inside runInTransactions() reaches subscribers pre-commit — a subscriber's cache delete opens a re-warm window

Why: an event dispatched by a domain/service call inside transactionGuardOrchestrator->runInTransactions() reaches subscribers BEFORE the commit; a subscriber's cache delete opens a window where a concurrent reader misses, reads the still-uncommitted OLD row under MVCC, and re-caches it for the full TTL. Cache invalidation for such writes belongs after the try/catch in the command handler — the repo's "Only after the commit" idiom (CreateMarketWizardCommandHandler, SetMarketAsPrimaryCommandHandler).
Evidence: shoptet/cms4 PR #46759, commit 0f2a8845dd replacing 4dcf2f507e's InvalidatePrimarySalesChannelIdCacheSubscriber (task MIN-104, 2026-10-21); MarketPrimaryService::setAsPrimary dispatches inside the transaction.
