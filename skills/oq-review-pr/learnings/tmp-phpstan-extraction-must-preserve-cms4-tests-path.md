---
status: active
dimension: general
date: 2026-10-01
---

# A /tmp git-archive phpstan re-run must keep the `cms4/tests` path segment or test helpers falsely fail shoptet.forbidStaticMethod

Why: `ForbidStaticMethodRule::isTestCode()` exempts a file when `str_contains($fileName, 'cms4/tests')`
(vendor/shoptet/phpstan/src/Rule/ForbidStaticMethodRule.php:62-64). The /tmp extraction learning
(git archive + cp -r vendor) produces paths like `/tmp/pr45569-review/tests/unit/...` that lack the
segment, so the rule fires on static fixture helpers that in-repo and CI runs correctly skip —
a reviewer then reports a PHPStan failure the PR author and CI legitimately never see, and the
author's "phpstan clean" claim looks false when it is true. The same heuristic means test support
classes must never be moved outside the tests tree: the exemption is path-based, not class-based.
Evidence: PR cms4#45569 review — first run reported `Possibly impure method ...Test::buildLegacyCurrency
can not be static`; moving the same tree to a path containing `cms4/tests` gave [OK] No errors;
CI "Cms4 PHPStan" on the same head: success.
