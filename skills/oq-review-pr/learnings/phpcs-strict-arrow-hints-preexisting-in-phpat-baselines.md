---
status: active
dimension: code-quality
date: 2026-11-07
---

# A new `ArrowFunctionDeclaration.DisallowedReturnTypeHint` hit under `phpcs-strict.xml` that mirrors an existing PHPat baseline arrow function is pre-existing pair polish, never a blocker — CI's Sniffer job runs the default standard where both are clean; report it as optional and never "fix" one half of a mirrored pair

Why: PHPat architecture tests build their selectors with `array_map(static fn (string $class): SelectorInterface => …)`. When a PR mirrors the neighbouring SalesChannel arrow function to add a same-shaped rule, the new line inherits the same `phpcs-strict.xml` hit the baseline line already has — a second occurrence of a rule that only the local-only `phpcs:strict` composer script runs. CI's `Cms4 Code Sniffer` job runs the default standard (`phpcs.xml.dist`), under which master and head are both clean, so the hit changes nothing about mergeability. Flagging it as blocking sends the author to "fix" one half of a mirrored pair — either by dropping the return type from the twin, which breaks the mirror that makes the two rules read alike, or by touching the pre-existing baseline line, which is outside the PR's scope. Report it as optional polish and leave the pair intact.
Evidence: shoptet/cms4#47732 review (task MIN-178, 2026-11-07, "freeze the nine legacy Multishop orchestrators with a PHPat rule") — the reviewer's Proposed learnings block records it (artifact e9dbd2cb-1324-420c-a668-d0231ab9ded9); `tests/architecture/Multishop/MultishopOrchestrationShapeTest.php` (new arrow fn next to the pre-existing SalesChannel one), `phpcs.xml.dist` vs `phpcs-strict.xml`.
