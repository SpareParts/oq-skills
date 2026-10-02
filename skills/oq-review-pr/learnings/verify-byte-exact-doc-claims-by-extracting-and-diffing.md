---
status: active
dimension: general
date: 2026-10-02
---

# Verify "byte-exact from <real file>" doc-example claims by extracting the fenced block and diffing — never by reading alone

Why: cms4 docs PRs increasingly ground their examples in real files and claim byte-exactness. The check is mechanical: `git show <pr-head>:<doc.md>`, extract the fenced block, then diff / md5 / substring it against the real file at the PR head — a PR body's Verification section cannot prove byte-exactness, and reading alone misses silent drift. For ghost sweeps in docs (extends `codeowners-dead-path-claims-need-glob-tests.md` and `deletion-prs-with-short-name-twins-need-namespace-discriminating-greps.md`), grep bare strings (e.g. `GetMarketsHandler`), not FQCNs — the bare name hides behind `GetMarketsQueryHandler` in an FQCN grep.
Evidence: PR shoptet/cms4#45627 (task MIN-22) — all 4 byte-exact claims TRUE; 10-pattern ghost sweep 0 hits.
