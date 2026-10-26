---
status: active
dimension: general
date: 2026-10-26
---

# A cms4 `Tests / Integration` run red on exactly `TrialRepositoryTest` with a ~3600-second gap is the integration runner's DB-clock drift — check the last master runs before blaming the PR

Why: the signature is two failures at `tests/phpunit/cms/packages/Project/Trial/Repository/TrialRepositoryTest.php:675` asserting a timestamp exactly one hour (3600 s) behind the deadline the database computes, e.g. "Failed asserting that 1792920802 is equal to 1792924402 or is greater than 1792924402". It reproduces on master: runs 40181114156, 40181099534 and 40181080533 (2026-10-25, master 9232f865ab and the two SHAs before it) all failed with exactly those two assertions, while `Api Shoptest`, `Cms4 Acceptance Tests` and `Cypress Cms4` were green on the same master head the same morning — so it is that runner's DB clock, not a repo-wide date flake. When the reviewed diff cannot reach `Project/Trial`, treat it as pre-existing and confirm against recent master integration runs before reporting the PR as red. A red `Cypress Cms4` is a different signature (a devenv provisioning step, no spec executed); do not fold the two together.
Evidence: review of shoptet/cms4#46957/#46958 (task MIN-124), plus the retrospective's verification of the three master integration runs and their sibling suites (2026-10-26).
