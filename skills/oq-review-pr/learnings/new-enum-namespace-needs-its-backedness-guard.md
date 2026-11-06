---
status: active
dimension: testing
date: 2026-11-06
---

# A PR that introduces a new Enum namespace should pin that namespace's backedness in the architecture test class it already touches

Why: the existing Contracts-side rule (`MultishopApplicationContractsTest::test_enums_are_backed`) selects `Shoptet\Contracts\Multishop.*\Enum` and does not follow an enum into another package tree, so a new Presentation-side enum is guarded only by its unit test's data provider and nothing stops it becoming int-backed or unbacked. In the evidence PR a 15-value string-backed wire enum shipped next to a shape test for a neighbouring concern but with no backedness rule for its own namespace, parked as a follow-up. Treat that follow-up framing as a finding, not a deferral: if the namespace is expected to grow the guard is more valuable, and the project rule phpat-guards-structural-changes says the introducing PR adds or extends the architecture test for a structural rule it introduces. The gap is cheap to close — mirror the Contracts rule with a Presentation selector, about 10 lines in the same test class.
Evidence: shoptet/cms4#47637 (task MIN-172) — tests/architecture/Multishop/MultishopPresentationShapeTest.php + `Shoptet\Multishop\Presentation\Dns\Enum\DnsErrorCode`.
