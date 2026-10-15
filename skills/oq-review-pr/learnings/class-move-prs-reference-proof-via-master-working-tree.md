---
status: active
dimension: general
date: 2026-10-03
---

# A class-move PR's reference completeness can be proven from the master working tree

Why: a move PR changes N files; every other file is byte-identical on master and the PR ref, so the proof is cheap and complete without a full PR-ref tree grep (expensive in a blobless clone): grep the OLD FQCN over the master working tree (exclude vendor/node_modules/.git/temp), then check every hit is in the PR's changed-file list — a hit outside it is a missed reference, and no hit outside it means zero remain post-move. Also grep the short name with namespace disambiguation (same-named exception twins are common), the path form, and — if the parent changed — the catch sites of the NEW parent.

Evidence: shoptet/cms4#45684 — 18 hits (16 use-lines + 2 phpstan neon entries), all inside the 22 changed files; PR-ref grep confirms zero remaining references.
