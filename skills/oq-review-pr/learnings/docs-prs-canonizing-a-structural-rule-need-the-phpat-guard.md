---
status: active
dimension: testing
date: 2026-10-11
---

# A docs PR that states a normative structural rule ("a rule, not a description") should extend the PHPat guard in the same PR — "documentation only, no structural rule introduced" contradicts the doc's own words

Why: the `phpat-guards-structural-changes` project rule triggers on a change that "introduces or relies on" a PHPat-expressible rule, and its fit-list already includes final/readonly across many classes. A doc canonizing such a rule introduces it at the doc level even when the code already complies — the repo's own precedent guards the analogous rule exactly this way, citing the doc in its because-text. When all implementers already comply, the guard is a zero-code-change regression test that passes immediately; declaring "PHPat not applicable" because the diff has no code leaves the fresh doc rule unguarded against the next strategy added without `final readonly`. Check the PR body's PHPat justification against the doc's own normative sentences before accepting it (same family as `phpat-guard-should-match-vacated-namespace-scope`, which guards a namespace the change emptied).
Evidence: shoptet/cms4#46101 review (MIN-51, 2026-10-11) — doc line 105 "Every implementer is final readonly — a rule, not a description" vs PR body "PHPat not applicable: documentation only"; precedent `tests/architecture/Multishop/MultishopCqrsShapeTest.php:24-73`; the follow-up commit added `MultishopDnsValidationShapeTest` with two proven negative controls.
