---
status: active
dimension: general
date: 2026-10-24
---

# A PR body's superlative scope ("the only X left") must not be contradicted by its own follow-up list — scope the claim to what the change guards

Why: a Why-section sentence like "the only non-final X in the whole tree" is falsified by the
body's own Suggestions naming another X of the same shape (or by a one-command recount of the
tree). The reviewer checks the superlative against (a) the body's own follow-ups and (b) the
guarded scope of any architecture rule the PR adds — the rule typically enforces one namespace or
package, so scope the sentence to that ("the only non-final X in `Vendor\Package`") even when the
wider claim looks true. A self-contradicting body cannot be edited after creation on some
platforms, so the correction becomes a public comment and the inaccuracy stays in the record.
Evidence: shoptet/cms4#46944 (task MIN-117, review 2026-10-24) — the Why said the PR closes "the
only non-final *ResponseBody classes in the whole cms/packages tree (26 of 31)" while the body's
own Suggestions named ProjectLanguage{,List}ResponseBody (SalesChannel) as also non-final; the
new PHPat rule guards only `Shoptet\Multishop\Presentation`, which is the honest scope. Counts in
the same sentence were also off by one (30 files vs 29 classes — a trait) — see
`pr-body-inventory-counts-need-diff-verification.md` for the recount rule this extends.
