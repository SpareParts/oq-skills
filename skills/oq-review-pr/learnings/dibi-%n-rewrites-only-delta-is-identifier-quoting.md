---
status: active
dimension: testing
date: 2026-11-10
---

# A dibi-safety rewrite from raw string interpolation to %n/Dibi\Expression can be A/B-verified with no database, and %n's backtick quoting is the only legitimate delta

Why: "the SQL is byte-identical" is cheap to claim and hard to trust by eye, but the vendored `Shoptet\PHPStan\Dibi\FakeMySqliDriver` makes it mechanical: instantiate the old and the new builder against it and diff the emitted SQL over every caller's call shape. The only expected difference is `%n`'s identifier quoting, because `delimite()` splits on `.` and escapes each part, the repo defines no dibi substitutions, and `Fluent::as($string)` already auto-binds `%N`, so alias columns were quoted before the rewrite too. Any other delta is a semantic change that must be justified, not normalized away in the diff.
Evidence: shoptet/cms4#47852 review (task MIN-191, 2026-11-10) — 18 caller call shapes diffed, 0 semantic deltas, quoting-only.
