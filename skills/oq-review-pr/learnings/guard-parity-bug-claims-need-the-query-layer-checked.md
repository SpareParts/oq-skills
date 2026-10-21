---
status: active
dimension: domain-integrity
date: 2026-10-20
---

# A claim that two presentation builders diverge in user-visible behaviour must be traced through the repository/query layer of each actual read path, not judged from the builders alone

Why: the same historical "bugfix" commit may have fixed the problem at the SQL layer (e.g. a `onlyRootChannels: true` query flag becoming `WHERE channel.parentId IS NULL`), which makes the later guard drift latent: the builders differ, but neither page can ever receive the input that would expose the difference. Check the query flags at every construction site of the builders before repeating "page X shows what page Y hides".
Evidence: shoptet/cms4#46741 review (MIN-100, 2026-10-20) — 764eadb774 added `onlyRootChannels: true` to `CurrencyDetailController:143/176` and `LanguageDetailOrchestrator:33` in the same commit that rewrote the currency twin's guard, so the twin divergence was never visible on either page; the PR body (and the Jira ticket) claimed a user-visible bug that did not exist.
