---
status: active
dimension: general
date: 2026-10-04
---

# A phpstan-files-l10 verification of a PR must list every new test file too, not only production files

Why: `make phpstan-files-l10 FILES="…"` runs whatever the caller lists; `tests/unit/cms/packages/Multishop` (and several other tests paths) are permanently in phpstan-l10.neon's `paths`, so CI analyzes new test files at L10 with phpstan-strict-rules active — a PR whose verification only lists its production files reports "[OK] No errors" while CI goes red on a rule the author never ran (here: `staticMethod.dynamicCall` on `$this->createStub()`, a `final protected static` PHPUnit method since 12.5). The PR body's "Left to CI: full unit suite + full PHPStan" then understates the gap: the failing rule is deterministic, not flaky.
Evidence: shoptet/cms4#45686 head 5d07fe1c05 — CI run 37161728961 "PHPStan L10 PHP 8.5" failed with 3× staticMethod.dynamicCall; fix commit b1560c2cca (self::createStub) went green; the PR body's L10 claim covered only the 6 production/arch files.
