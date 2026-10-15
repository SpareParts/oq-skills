---
status: active
dimension: domain-integrity
date: 2026-10-15
---

# MarketsCountChecker's catch→0 is a market COUNT, not its public verdict — check() is inverted (1 = invalid / 0 = valid)

Why: doc sentences like "counts a project with no markets as 0" (queries-and-commands.md:142) are true of the private `countMarkets()` (`catch (MarketNotFoundException) { return 0; }`) but collide with the class's public `ProjectDataCheckerInterface` vocabulary, where `check()` returns 1 = problem found / 0 = healthy (MarketsCountChecker.php:28-55). A skimming reader of the doc sentence inverts the invariant. Reviews of Monitoring/Checker prose should name "a market count of 0", not bare "0", and never quote `check()`'s return value without naming the axis.
Evidence: shoptet/cms4#46373 — cms/packages/Multishop/Monitoring/Checker/MarketsCountChecker.php:57-64 vs :28-55; cms/packages/Multishop/docs/coding/queries-and-commands.md:142.
