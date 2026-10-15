---
status: active
dimension: general
date: 2026-10-10
---

# In a read-only snapshot review, dead-path greps must target the pinned PR ref — the working tree is the base branch, not the head

Why: the reviewer's checkout stays on master, so `grep -rn`/`git grep -- paths` against the working tree answers questions about the BASE, silently producing false positives (the "deleted" class is right there in the tree) or false all-clears. Run `git grep <pattern> <pinned-ref> -- <paths>` (and `git diff master...<ref>` for the diff); only grep the working tree for files the PR does not touch. Complements `class-move-prs-reference-proof-via-master-working-tree` (a master-tree grep is valid exactly when every hit outside the PR's changed files would falsify the claim) and `reviewer-extract-pr-trees-to-tmp-with-cp-r` (tool re-runs need a head-exact tree).
Evidence: shoptet/cms4#46087 review (MIN-48) — working-tree grep for `CountryDetailView\b` returned the deleted class's definition; the same grep against `refs/pr-review/46087` returned zero non-orchestrator hits.
