---
status: active
dimension: testing
date: 2026-10-15
---

# Per-instance stubbing of value-object parameters requires willReturnMap — pairs of with() fail in reverse-registration order even for value-distinct objects

Why: PHPUnit matches expectations for the same method in REVERSE registration order, and `with()` uses equality. For a `final readonly` value object like `Market`, two `createMarket(id: 1)` / `createMarket(id: 2)` instances are equal enough that the first invocation is checked against the LAST registered expectation, and the pair-of-`with()` idiom cannot express "one return per distinct instance" (verified empirically on PR #46373: expected id 2 vs actual id 1 failure at the first map() call). `willReturnMap` matches by strict `===` parameter identity (ReturnValueMap.php:39-49), so each row binds to the exact instance, and `expects(exactly(n))` still pins the call count. It is the repo's established idiom (43 uses under tests/unit). When a handler maps over a list of value objects, review for `willReturnMap` + `assertSame` on the whole result list — it pins identity AND order in one assertion.
Evidence: shoptet/cms4#46373 — tests/unit/.../GetMarketsQueryHandlerTest.php:57-68; probe ProbeWithExpectationsTest failing on a head-exact tree; vendor/phpunit/phpunit/src/Framework/MockObject/Runtime/Stub/ReturnValueMap.php.
