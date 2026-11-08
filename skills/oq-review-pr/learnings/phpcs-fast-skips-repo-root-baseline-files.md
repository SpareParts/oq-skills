---
status: active
dimension: general
date: 2026-11-08
---

# composer phpcs:fast never lints repo-root files like phpstan-l10-baseline.php — its pre-existing violations are invisible to CI and must not be attributed to a PR

Why: `composer phpcs:fast` (what cms4's CI "Code Sniffer" workflow runs on PRs) pipes
`git diff --name-only … '*.php'` through a path-prefix filter
(`^admin|^applications|^build|^cms|^scripts|^tests|^common_root|^crm`), so
`phpstan-l10-baseline.php` at the repo root is never linted even when a PR modifies it. Two
consequences: (1) a PR whose only "source" change is the baseline can truthfully claim "phpcs
clean" and CI's Code Sniffer job passes; (2) a reviewer who runs phpcs DIRECTLY on the baseline
file sees ~2500 pre-existing tab-indent violations (master 2504, the reviewed head 2500 — the PR
deleted 4) and must not attribute them to the PR; the baseline also sits in the release
deploy-ignore filter. Before drawing any phpcs conclusion about a repo-root file, check whether it
is inside the phpcs:fast path filter.
Evidence: MIN-182 (nightly code study 2026-11-08) review of shoptet/cms4#47745 — the PR modified
`phpstan-l10-baseline.php` (deleted one 6-line block), CI Code Sniffer passed, and a direct local
phpcs run showed 2504 pre-existing tab-indent errors on master versus 2500 at head; review artifact
b55d9f84.
