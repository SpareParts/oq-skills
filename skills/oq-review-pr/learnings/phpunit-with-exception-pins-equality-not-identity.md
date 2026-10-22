---
status: active
dimension: testing
date: 2026-10-22
---

# PHPUnit with(['exception' => $e]) pins equality, not identity — an equal fresh instance of the same exception class passes

Why: with() wraps plain values in IsEqual, which short-circuits on identity but otherwise falls back to ObjectComparator; ExceptionComparator strips file/line/trace/string before comparing, so for property-less domain exceptions a newly constructed instance is "equal" to the thrown one. PR bodies and commit messages claiming the context carries "the exact instance" overstate the pin; the assertion still catches wrong class / wrong message, but a handler that logged a fresh SameException() instead of the caught one would pass. Say "an equal exception instance", or wrap the expectation in self::callback with === if identity is the contract.
Evidence: shoptet/cms4#46805 review (task MIN-107, 2026-10-22) — vendor/phpunit/phpunit/src/Framework/MockObject/Runtime/Rule/Parameters.php:46, vendor/sebastian/comparator/src/ExceptionComparator.php; probe: two distinct MultishopWaitlistOptionMissingException instances satisfy IsEqual.
