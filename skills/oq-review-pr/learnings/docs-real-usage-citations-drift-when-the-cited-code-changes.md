---
status: active
dimension: general
date: 2026-11-02
---

# Docs "Real usage: file (line N)" sentences are live cross-references — a PR that changes the cited behaviour must reword them, and sibling PRs that avoid the line create a merge-order obligation

Why: a docs file that pins a "Real usage" example to a file:line is a live cross-reference, not prose: the cited code can change under it, and then the docs teach the wrong thing while reading fine. When one PR removes or rewrites the cited behaviour, the sentence must change in the SAME PR — and when two sibling PRs deliberately split the doc's lines to keep their hunks disjoint, the PR that leaves the line behind must still be checked: after the sibling merges, its head cites behaviour that no longer exists, so whichever PR merges second needs a one-line docs rebase. Reviewing each diff against its own base hides this; check the cited line against BOTH heads.
Evidence: shoptet/cms4#47338/#47339 (task MIN-150, review 2026-11-02) on docs/multishop/coding/queries-and-commands.md — #47339 removes the MarketsCountChecker try/catch that :142 cites while #47338 leaves :142 untouched; disjoint hunks, both merge orders textually clean, but #47338-merged-after needs the one-line reword.
