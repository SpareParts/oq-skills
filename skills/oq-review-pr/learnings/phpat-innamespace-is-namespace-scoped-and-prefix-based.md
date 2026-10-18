---
status: active
dimension: testing
date: 2026-10-18
---

# PHPat's `Selector::inNamespace` matches the extracted NAMESPACE (non-regex, by prefix), not the FQCN — nested doubled namespaces need their own selector, and a regex selector is matched against the namespace

Why: a non-regex `inNamespace('Shoptet\SalesChannel\Domain')` matches classes whose extracted namespace has that string as a prefix, so a nested doubled namespace such as `Shoptet\SalesChannel\SalesChannel\Domain` is NOT covered by the parent selector — the descendant path `...\Domain` matches the parent prefix, but the doubled one does not. A future "deduplication" that collapses the two selectors into one therefore silently unguards the nested subtree while the architecture suite stays green. The same namespace-scoping applies to a regex `inNamespace('/^....$/')`: it is matched against the extracted namespace (FQCN minus the class name), not the full FQCN. Verify both directions when judging a layering rule's scope: enumerate the classes each selector actually matches before trusting that a guard covers what its name promises.

Evidence: shoptet/cms4#46562 (task MIN-82) `tests/architecture/Multishop/SalesChannelCqrsShapeTest.php:22-23,81-82` — the review verified the nested selector is genuinely required and suggested exactly one comment line saying so. Distinct from `phpat-innamespace-selector-matches-the-namespace-not-the-fqcn` (open-PR sibling on the MIN-30 branch): that file covers the regex-matches-namespace-vs-FQCN half; this one is about prefix-based matching and nested doubled namespaces needing their own selector.
