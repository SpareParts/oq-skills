---
status: active
dimension: testing
date: 2026-10-07
---

# A test double for a method returning Dibi\Fluent must return a real Fluent — an array double type-errors at iteration, and the production return type is never the thing to relax

Why: `Dibi\Fluent` is a lazy query builder, so a double that returns an array looks equivalent until the code iterates the stub's return value and PHPUnit (honouring native return types) fails with a TypeError instead of a test result — a CI failure that never reproduces locally when the author only ran the scoped suite against the real test DB. Build the real Fluent against the seeded test DB, seeded with an id sentinel (e.g. a value no other fixture row uses) so the test keeps exclusive control of the returned list without stubbing the query at all. Relaxing the production return type to `Fluent|array` for testability broadens the public contract and must be rejected in review even though it silences the failure.
Evidence: shoptet/cms4#45914 (task MIN-40, review 2026-10-07) — head 4c151860 failed workflow run 37623238013 in CI while the scoped local suite passed; fixed at head 42b54e90 by returning a real Fluent; the stubbed method is declared at cms/packages/Miscellaneous/MoveToDomainChecker.php:31.
