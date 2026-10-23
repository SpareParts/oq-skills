---
status: active
dimension: testing
date: 2026-10-23
---

# PHPat shouldBeInvokable() proves __invoke exists, not that it is public — visibility-blind, so because-texts must not promise "public __invoke"

Why: PHPat 0.11.x's `shouldBeInvokable()` asserts `hasMethod('__invoke')` via `InvokableExtractor`,
which is visibility-blind: a `private` or `protected` `__invoke` passes the rule. In a dispatch-shape
guard the attribute rule (`shouldApplyAttribute(AsMessageHandler::class)`) is the enforced half of
the contract; `shouldBeInvokable` only pins the existence half. A test method or because-text that
promises "handlers have a public __invoke" overstates the guarantee — either add
`shouldBePublicMethod()` when the visibility genuinely is the rule, or word the because-text as
existence only.
Evidence: shoptet/cms4#46880 review (MIN-112) — `MultishopCqrsShapeTest.php:96-101`; verified
experimentally on the PR tree that a private `__invoke` passes `shouldBeInvokable`
(vendor/phpat/phpat/src/Rule/Extractor/Declaration/InvokableExtractor.php).
