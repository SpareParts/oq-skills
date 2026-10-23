---
status: active
dimension: testing
date: 2026-10-23
---

# PHPat shouldBeInvokable() proves __invoke exists, not that it is public — visibility-blind, so because-texts must not promise "public __invoke"

Why: PHPat's `shouldBeInvokable()` asserts `hasMethod('__invoke')` via `InvokableExtractor`,
which is visibility-blind: a `private` or `protected` `__invoke` passes the rule. In a dispatch-shape
guard the attribute rule (`shouldApplyAttribute(AsMessageHandler::class)`) is the enforced half of
the contract; `shouldBeInvokable` only pins the existence half. A test method or because-text that
promises "handlers have a public __invoke" overstates the guarantee. When visibility genuinely is
the rule, PHPat has no `shouldBePublicMethod()`: the closest real assertions are
`shouldHaveOnlyOnePublicMethod()` / `shouldHaveOnlyOnePublicMethodNamed('__invoke')`, and both
require `__invoke` to be the class's only public method besides `__construct` — too strong for a
typical handler. The safe wording is existence only, or a plain unit test asserting
`(new ReflectionMethod($handler, '__invoke'))->isPublic()`.
Evidence: shoptet/cms4#46880 review (MIN-112) — `MultishopCqrsShapeTest.php:96-101`; verified
experimentally on the PR tree that a private `__invoke` passes `shouldBeInvokable`
(vendor/phpat/phpat/src/Rule/Extractor/Declaration/InvokableExtractor.php); the assertion list is
`src/Test/Builder/ConstraintStep.php` (`shouldBeInvokable`:107, `shouldHaveOnlyOnePublicMethod`:195,
`shouldHaveOnlyOnePublicMethodNamed`:203) and the sole-public-method requirement is
`src/Rule/Extractor/Declaration/PublicMethodNamedExtractor.php`.
