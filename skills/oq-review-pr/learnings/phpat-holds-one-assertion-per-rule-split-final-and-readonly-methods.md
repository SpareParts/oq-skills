---
status: active
dimension: architecture
date: 2026-10-05
---

# PHPat holds exactly ONE assertion per rule — a final+readonly shape guard needs two test methods each, and each method name must name its single assertion

Why: PHPat's `AssertionStep` stores one `assertion` per `RelationRule` and every `shouldBe*()` both overwrites it and returns `TipOrBuildStep` (a build step), so `->shouldBeFinal()->shouldBeReadonly()` is unrepresentable — the type system rejects the chain. The practical trap seen on cms4#45695's intermediate commit: three methods named `..._are_final_readonly` each asserted only `shouldBeFinal()`, so the readonly lag was entirely unguarded while the names promised it; the head fixed it with six methods whose names match their assertion (`..._are_final` → shouldBeFinal, `..._are_readonly` → shouldBeReadonly). Review shape guards by opening the builder, not the method names.
Evidence: shoptet/cms4#45695 commits f3df4d78bd → df99a28f53; vendor/phpat/phpat/src/Test/Builder/AssertionStep.php:53-79; sibling pattern tests/architecture/Marketplaces/MarketplacesApplicationContractsTest.php (test_dto_classes_final / test_dto_classes_readonly).
