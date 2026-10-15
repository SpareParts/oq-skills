---
status: active
dimension: architecture
date: 2026-10-05
---

# PHPat's Selector::inNamespace regex matches the NAMESPACE (FQCN minus class name), not the class — enumerate matches with the built regex before trusting a shape guard

Why: a rule written as `/^App\\.*\\(QueryHandler|CommandHandler)$/` looks like it guards "all handlers" but silently misses any handler whose namespace lacks the suffix — e.g. a live `#[AsMessageHandler]` named `UpdateMarketScalarDataCommandHandler` sitting directly in `…\Application\Contract` escaped both handler rules of cms4's new CQRS shape guard, while the same selector simultaneously matched MORE than intended (15 message and 15 contract classes vs the 11-file sweep). The fix is mechanical: re-build the exact regex string the test constructs, run it over every class's namespace (pop the class name off the FQCN), and diff the match list against the intended surface; class-name-shaped rules need `Selector::classname(...)` (which matches the FQCN) instead.
Evidence: shoptet/cms4#45695 — vendor/phpat/phpat/src/Selector/ClassNamespace.php:25-36 + helpers.php extractNamespaceFromFQCN; tests/architecture/Multishop/MultishopCqrsShapeTest.php:84-96; cms/packages/Multishop/Application/Contract/UpdateMarketScalarDataCommandHandler.php:12.
