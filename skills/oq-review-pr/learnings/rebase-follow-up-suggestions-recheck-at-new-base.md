---
status: active
dimension: general
date: 2026-11-05
---

# After a rebase (or any time gap) between PR-body writing and the CR reply, re-verify the body's open "follow-up suggestions" against the new base — a merged follow-up makes the suggestion stale

Why: a PR body's follow-up section names a guard gap ("Contracts commands have no final/readonly assertion") that was true when written but was closed by an unrelated master PR (#46880) that landed before the rebase — the rebased PR then ships a suggestion to do work that is already done, and the CR reviewer reading the body may believe the gap is live. A rebase changes not just paths but the truth value of prose claims about the repo state. Re-grep each follow-up claim at the new merge-base before replying to a CR; either strike it or say "already fixed by #N".
Evidence: shoptet/cms4#46216 rebase review (task MIN-64, 2026-11-05) — PR body "Suggestions / follow-ups" vs tests/architecture/Multishop/MultishopCqrsShapeTest.php:99-107 added by #46880 (07fa761658), an ancestor of rebase base 0b6932db17.
