---
status: active
dimension: general
date: 2026-10-20
---

# When a past commit changed both a query-level filter and a presentation-layer guard, read the whole commit — the guard hunk alone makes a later rewrite look like a dropped filter

Why: a study that reconstructs the read path from one diff hunk of a historical "bugfix" commit can produce a premise that the code never supported: the guard hunk shows a filter being added, but the same commit may also have added the query flag that makes the guard irrelevant, so a later rewrite of the guard looks like a regression ("silently dropped the parent filter") while the deployed read path never changed. Read the commit whole, then re-derive the deployed read path at the current head — flags, filters and construction sites — before stating either the original defect or the drift. Distinct from `verify-lost-vs-never-had-drift-claims-with-git-log-S-on-both-twins` (which hunts the commit that introduced a behaviour) and from `guard-parity-bug-claims-need-the-query-layer-checked` (the verification target, not the diff-reading method).
Evidence: shoptet/cms4#46741 review (MIN-100, 2026-10-20); the study's premise ("child channels were shown on the currency detail page but hidden on the language page") was derived from the guard diff of 764eadb774 without its query-flag hunks, which had excluded child channels on both pages since that commit.
