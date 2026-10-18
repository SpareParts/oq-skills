---
status: active
dimension: general
date: 2026-10-18
---

# Verify a rebase by union, not by diff silence

Why: a clean three-dot diff after a rebase proves the branch changed, not that the conflict resolution kept both sides — a silently dropped side (a deleted row, a reverted hunk) still produces a perfectly clean diff against the new base. After a rebase with conflicts, prove the resolution mechanically: byte-compare every non-conflicted file against the pre-rebase commit (`git diff <pre-rebase> <rebased> -- <files>` must be empty), and for the conflicted file, normalize both sides (sort or re-render with the repo's formatter) and diff the whole file against a union expectation — the deltas must be exactly the intended ones, nothing else. "The diff looks right" is not verification; "exactly N deltas, all listed" is.

Evidence: shoptet/multishop-software-factory#101 (task MIN-86) — a rebase onto a main that had gained 20 commits, with one conflicted table (docs/verification.md). The independent review (artifact 92d8833e) audited it with a normalized 350-row whole-file diff showing exactly 2 deltas (the PR's extended row and Prettier re-padding), and byte-compared the six non-conflicted files against the pre-rebase commit. Earlier the same night, MIN-78's rebase of #90 used the same reasoning to prove a conflict resolution kept both sides' rows.
