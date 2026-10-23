---
status: active
dimension: general
date: 2026-10-22
---

# A Copilot "restore the legacy lookup" comment can restate the PR's own intent — read the commit titles and the approval timeline before confirming a regression

Why: automated reviewers (Copilot) comment per-commit and read like regression reports, but a
"you removed X, this will break Y" finding may describe exactly what the PR set out to do.
Before confirming it as a defect, check three things: whether the removal is its own dedicated
commit with a title stating the intent, whether a test pins the new behaviour, and whether a
human approval postdates that commit. When all three hold, the comment is a restatement of the
PR's intent, and the finding reduces to naming any residual edge the team should consciously
accept rather than a blocker.
Evidence: shoptet/cms4#46823 review (MIN-111) — Copilot's "Hosts stored only in projects.url now
resolve to null" read as a regression until the commit list showed removal commit `1718ed0658`
("Stop reading projects.url…"), test `testStoresNoProjectForAHostKnownOnlyFromProjectsUrl`
pinning the null outcome, and a human approval 28 minutes after the commit.
