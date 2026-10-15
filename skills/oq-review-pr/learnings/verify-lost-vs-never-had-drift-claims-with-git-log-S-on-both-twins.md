---
status: active
dimension: general
date: 2026-10-12
---

# A PR claiming a dead twin "lost" or "drifted from" a behavior must test the claim with `git log -S'<behavior>'` on BOTH twins — "never had" and "lost" are different stories, and the wrong one recurs

Why: in #46199 the PR body (and commit message, inherited verbatim from the delegation chain) said the dead Contract twin "silently lost" the `onlyVisible` branch "when it was introduced in c8d3777f03"; git shows c8d3777f03 birthed the twin with a bare `findAll()` (matching its live twin at that date), and the branch arrived only in a8c2bdb634 five months later, updating the live handler but not the dead one — the twin never had anything to lose. The deletion was still correct (arguably stronger: duplicate-from-birth, drifted by omission), but the prose is a false claim reviewers and maintainers may repeat. This is the third wrong-narrative instance in deletion PRs (#45504 "predates", #46199 "lost") — the existing check (`git log --diff-filter=A` for birth order) must extend to `git log -S` for behavior-drift claims: run it on the live file AND the dead file before letting "lost/drifted from <sha>" into a PR body.
Evidence: shoptet/cms4#46199 (MIN-60 review, 2026-10-12) — c8d3777f03 (2025-07-15) vs a8c2bdb634 (2025-12-16); extends deletion-prs-with-short-name-twins-need-namespace-discriminating-greps.md.
