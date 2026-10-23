---
status: active
dimension: general
date: 2026-10-22
---

# A new test under tests/phpunit/ runs in the Integration workflow, not the Unit workflow — name the suite that is the evidence

Why: cms4's `composer tests:unit` runs `phpunit -c tests/unit/phpunit.xml`, whose testsuite
covers only `tests/unit` and `applications/*/tests/unit`; a test file under `tests/phpunit/` is
run by `tests/phpunit/phpunit.xml` (`defaultTestSuite="integration"`) through the **Cms4
Integration Tests** workflow. Both suites can be green on the head while the review names the
wrong one as the execution evidence. Naming the wrong green workflow is easy to do and easy to
catch: read `composer.json`'s `tests:unit`/`tests:run` scripts and the file's directory before
writing "the Unit workflow runs this test".
Evidence: shoptet/cms4#46823 review (MIN-111) — `TokenControllerTest` under `tests/phpunit/`
ran green in the Integration workflow (run log: "Running: tests/phpunit/…/TokenControllerTest.php",
9 tests, 30 assertions), not "Cms4 PHP Unit Tests" as the PR's reviewers first assumed.
