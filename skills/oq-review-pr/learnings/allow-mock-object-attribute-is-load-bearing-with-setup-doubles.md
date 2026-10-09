---
status: active
dimension: testing
date: 2026-10-08
---

# #[AllowMockObjectsWithoutExpectations] is load-bearing (not cargo-cult) whenever a setUp() double goes unused in at least one test — deleting it fails the run under failOnPhpunitNotice

Why: the green-scoped-run learning says the runner enforces expectations on doubles, but a test class whose setUp() creates a shared mock (e.g. CommandBus) that some tests never exercise (matches()-only tests) needs the class-level attribute precisely: without it, PHPUnit 12.5 emits "No expectations were configured for the mock object" notices and `failOnPhpunitNotice="true"` (tests/unit/phpunit.xml:12) fails the suite. Verified empirically by deleting the attribute on a head-exact tree (exit 1) and restoring it (green). So for sibling-shaped test classes with shared setUp doubles, the attribute is required, not stylistic — and reviewers can prove either direction with a /tmp tree.
Evidence: shoptet/cms4#45938 review (MIN-41, 2026-10-08) — tests/unit/cms/packages/Multishop/Application/Synchronization/PartialSynchronizers/ShippingMethodsSynchronizerTest.php:15-25 (setUp CommandBus mock; two matches() tests never touch it).
