---
status: active
dimension: general
date: 2026-09-29
---

# Verify "dead path" claims in CODEOWNERS/doc cleanups with glob expansion and sibling near-misses, not just exact-path ls

Why: A CODEOWNERS rule like `/scripts/cron/ManageMultipleLanguages` (no wildcard) can be dead while the team-doc bullet `/scripts/cron/ManageMultipleLanguages*` still matched the real `ManageMultipleLanguagesJob.php` — "dead" must be tested against each pattern AS WRITTEN in each file. A case-variant glob can also match a sibling file the change doesn't mention: `ls admin/controllers/Multishop*` matched `MultishopSettingsController.php` even though the intended target was `MultiShop/` (capital S) — glob-test old/removed patterns with the shell and grep for near-miss siblings before agreeing a removal loses nothing. For ADDED rules, check CODEOWNERS last-match-wins: no rule AFTER the edited block may match the same paths.
Evidence: shoptet/cms4#45440 review (MIN-12, 2026-09-29) — PR body claimed old doc bullets matched "nothing"/were "dead"; glob tests disproved both characterizations; the only later scripts/cron rule (OpenAiProductFeedJob.php) had no overlap so no override.
