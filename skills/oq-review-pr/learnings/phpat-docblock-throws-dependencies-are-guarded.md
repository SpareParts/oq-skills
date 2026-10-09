---
status: active
dimension: testing
date: 2026-10-08
---

# PHPat ShouldNotDepend tracks docblock @throws — doc-only layering references are real violations

Why: PHPat 0.11.x registers DocThrowsTagRule (and Doc*/Method/Param/Return/Var/Property/Mixin tag rules) under ShouldNotDepend, and ignore_doc_comments defaults to false — so a Domain interface whose docblock alone references an Infrastructure class violates a Domain↛Infrastructure rule and fails the run, no use statement needed. Two consequences for reviews: (1) "no remaining references" checks must grep docblocks, not just imports; (2) when the original violation was docblock-shaped (a @throws on a Domain port), the negative control should include a docblock-only fixture — an import-only control proves less than it seems. Verified on cms4 #45996: a docblock-only @throws fixture fired with identifier phpat.testDomainNoInfrastructureDependency.
Evidence: shoptet/cms4#45996 (task MIN-41, review 2026-10-08); vendor/phpat/phpat/src/Rule/Extractor/Relation/DocComment/MethodScope/ThrowsTagExtractor.php; vendor/phpat/phpat/extension.neon (ignore_doc_comments: false).
