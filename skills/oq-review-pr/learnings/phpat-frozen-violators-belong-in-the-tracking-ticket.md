---
status: active
dimension: testing
date: 2026-10-19
---

# A PHPat exclusion's @see tracking issue must itself name the frozen violators, or the pointer decays into "somewhere in that PR"

Why: the phpat-guards rule requires naming a tracking issue in the test docblock, but if the issue only describes the PR's scope and never enumerates the excluded classes, the maintainer who eventually picks up the ticket must recover the list from the test constant or the PR body — the pointer is live (issue open, right axis) yet under-specified. Extends `issue-pointer-axis-and-state-check` (which checks the pointer's validity) with a completeness check: the issue should carry the class list the exclusion freezes.
Evidence: shoptet/cms4#46567 review (MIN-89, 2026-10-19) — `MultishopWriteRepositoryShapeTest.php:13` `@see CZ3MUL1-1092` vs the ticket text (0 hits for the four laggard class names).
