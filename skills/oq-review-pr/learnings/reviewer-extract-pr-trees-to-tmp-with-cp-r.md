---
status: active
dimension: general
date: 2026-09-28
---

# To re-run a repo's vendor tools against a PR head from a read-only checkout, `git archive` the PR ref into /tmp and `cp -r` (NOT `cp -al`) the repo's vendor/ next to it

Why: hardlinks fail across the /workspace→/tmp overlay boundary, and a symlinked vendor resolves `__FILE__` to the real repo, silently analyzing master instead of the PR.
Evidence: MIN-10 independent review run (2026-09-28), used for shoptet/cms4#45406 and #45407.
