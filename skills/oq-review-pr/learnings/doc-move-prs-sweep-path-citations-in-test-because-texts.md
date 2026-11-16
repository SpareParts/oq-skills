---
status: active
dimension: general
date: 2026-11-05
---

# A PR that moves a docs tree must sweep test/docblock citations of the moved paths — PHPat because-texts and @see prose go stale silently and CI stays green

Why: #46505 moved `cms/packages/Multishop/docs/coding/` to `docs/multishop/coding/`, and `MultishopSynchronizationShapeTest.php:17`'s because-text still cites the old `cms/packages/Multishop/docs/coding/best-practices.md` — the citation justifies a normative rule ("per the Multishop convention in …"), so the justification now points at a file that no longer exists. Extends `type-move-prs-must-grep-short-names-in-comments.md` from types to doc paths: grep the moved root (`git grep 'packages/Multishop/docs'`) across tests/, .claude/, and *.md in the same PR that does the move.
Evidence: shoptet/cms4#46216 rebase review (task MIN-64, 2026-11-05) found the stale citation at tests/architecture/Multishop/MultishopSynchronizationShapeTest.php:17, identical on master and untouched by the PR; the move itself was #46505.
