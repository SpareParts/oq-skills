---
status: active
dimension: general
date: 2026-10-18
---

# Run Prettier from the extracted repo root, not from an out-of-tree directory

Why: an out-of-tree Prettier spot-check (running `prettier --check` on files extracted to /tmp without the repo's `.prettierrc` / `.prettierignore` and its directory context) produces false positives — the check runs with default config instead of the repo's, and files that are clean in CI show as unformatted. When verifying formatting on an extracted head-exact tree, run from the extracted repo root with the repo's config files present, or expect to chase formatting "findings" that are artifacts of your own tooling.

Evidence: shoptet/multishop-software-factory#101 review (task MIN-86, artifact 92d8833e) — the reviewer's first out-of-tree prettier spot-check produced 5 false positives; re-running from the extracted repo root (config in place) produced zero, and the whole head tree passed `prettier --check .`.
