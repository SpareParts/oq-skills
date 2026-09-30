---
status: active
dimension: testing
date: 2026-09-30
---

# A green cms4 unit run is itself evidence every double has an expectation — failOnPhpunitNotice fails expectation-less createMock, so spot-check doubles instead of hand-auditing all of them

Why: AGENTS.md (~line 305) and `failOnPhpunitNotice="true"` in tests/unit/phpunit.xml make a `createMock` that never receives `expects()` fail the run (since the PHPUnit 12.5 migration, #43020). When the scoped suite is green at the PR head, expectation-less doubles cannot be present, so hand-auditing every double duplicates what the runner enforces. Still confirm the run was really on the PR head (git archive + cp -r vendor, per the /tmp extraction learning) and that `with()`-constrained doubles keep an explicit `expects()` (`with()` on a stub is deprecated and silently drops the check).
Evidence: shoptet/cms4#45505 review (MIN-17, 2026-09-30) — 17/17 doubles compliant, scoped run OK 156/652.
