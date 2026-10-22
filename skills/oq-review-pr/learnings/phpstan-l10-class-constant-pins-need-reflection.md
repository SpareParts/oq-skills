---
status: active
dimension: testing
date: 2026-10-22
---

# To pin a class constant's value under cms4 PHPStan L10, read it via ReflectionClass::getConstant — the naive assertSame is rejected as always-true

Why: self::assertSame('literal', SomeClass::CONSTANT) errors at L10 ("…will always evaluate to true", identifier staticMethod.alreadyNarrowedType; a bare === probe reports identical.alwaysTrue) because PHPStan resolves the constant. (new \ReflectionClass(SomeClass::class))->getConstant('CONSTANT') returns mixed, so the identical assert is not statically known-true and the pin survives L10 while still failing on a constant rename (verified by negative control: renaming to a different literal fails exactly the pinning test). One in-repo precedent exists (MultishopModuleActivationSubscriberTest.php:81, private method pin).
Evidence: shoptet/cms4#46805 review (task MIN-107, 2026-10-22) — HubSpotMultishopWaitlistGatewayTest.php:19; L10 probes of both shapes on a head-exact tree.
