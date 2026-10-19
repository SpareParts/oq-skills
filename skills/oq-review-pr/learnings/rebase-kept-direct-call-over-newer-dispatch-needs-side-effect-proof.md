---
status: active
dimension: general
date: 2026-10-18
---

# A rebase that keeps an old direct call over a newer command dispatch must enumerate the newer command's side effects and prove each unreachable in the bypassed path

Why: rebases regularly meet a semantic conflict where the PR deliberately calls a repository method that master has since wrapped in a command handler (event dispatch, domain movers, post-commit publishers). "The PR was written that way" is not closure: the reviewer must list every side effect the newer handler added (listeners on its event, movers, publish-after-commit steps), grep who depends on each, and prove the bypassed path cannot reach the state they exist for. If the proof depends on a single-market (or similar) invariant, that invariant must be named in the PR description, because the next feature that relaxes it silently re-opens the gap.
Evidence: shoptet/cms4#44496 rebase review (MIN-88, 2026-10-18) — `BasicInformationSynchronizer.php:77` bypasses `SetMarketAsPrimaryCommandHandler` (master #46002); only `SyncOptionsToGlobalSubscriber` listens to `MarketSetAsPrimaryEvent`; `FindMarketTrait.php:31-37` carries the load-bearing single-market invariant.
