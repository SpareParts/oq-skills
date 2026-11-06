---
status: active
dimension: testing
date: 2026-11-06
---

# A PR that introduces a new Enum namespace should pin that namespace's backedness in the architecture test class it already touches

Why: the existing Contracts-side rule (`MultishopApplicationContractsTest::test_enums_are_backed`) selects `Shoptet\Contracts\Multishop.*\Enum` and does not follow an enum into another package tree, so a new Presentation-side enum is guarded only by its unit test's data provider and nothing stops it becoming int-backed or unbacked. In the evidence PR a 15-value string-backed wire enum shipped next to a shape test for a neighbouring concern but with no backedness rule for its own namespace, parked as a follow-up. Treat that follow-up framing as a finding, not a deferral: if the namespace is expected to grow the guard is more valuable, and the project rule phpat-guards-structural-changes says the introducing PR adds or extends the architecture test for a structural rule it introduces. Do not copy the Contracts rule's shape blindly: its `NOT(Selector::isEnum())` cannot fail an unbacked enum, because PHPat 0.11's `isEnum()` is true for every enum, backed or not — a mirrored rule would stay green when the invariant breaks. Select unbacked enums (for example every enum in the namespace that does not implement `BackedEnum` should not exist), keep it in the same test class (about 10 lines), and prove the guard with a negative control before teaching it: drop `implements BackedEnum` on a scratch copy and watch the rule fire.
Evidence: shoptet/cms4#47637 (task MIN-172) — tests/architecture/Multishop/MultishopPresentationShapeTest.php + `Shoptet\Multishop\Presentation\Dns\Enum\DnsErrorCode`.
