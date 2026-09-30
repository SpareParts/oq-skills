---
status: active
dimension: general
date: 2026-09-30
---

# To re-run a repo's vendor tools against a PR head from a read-only checkout, `git archive` the PR ref into /tmp and `cp -r` (NOT `cp -al`) the repo's vendor/ next to it

Why: hardlinks fail across the /workspace→/tmp overlay boundary, and a symlinked vendor resolves `__FILE__` to the real repo, silently analyzing master instead of the PR. Update for pnpm workspaces (cms4 admin-web): mirror the app's directory depth in /tmp and symlink the REPO-ROOT node_modules (not the package's) so the relative per-package symlinks (`../../../../node_modules/.pnpm/...`) resolve; also copy the repo-root `tsconfig.base-fe.json`, `frontend/libs/`, and symlink `cms/` for template-JSON imports. Running vitest this way against a head-exact tree (working tree + `git show pr-ref:` overlays of the changed files) verified PR behavior without touching the workspace.
Evidence: shoptet/cms4#45372 review (2026-09-29) — /tmp tree at mirrored depth, `node_modules -> /workspace/repos/cms4/node_modules`, page tests 3/3 pass + toast/inline probe.

- Note: the pre-approved temp dir `/tmp/opencode` can be root-owned and unwritable in the Minions reviewer runtime (`mkdir` → Permission denied). The pattern is the point, not the path: `git archive` the PR ref into any writable /tmp directory (e.g. `/tmp/pr<N>-review`) and `cp -r` (never `cp -al`) vendor/ next to it. Verified again on shoptet/cms4#45505 (2026-09-30): full archive + 537M vendor copied, scoped phpunit green.
