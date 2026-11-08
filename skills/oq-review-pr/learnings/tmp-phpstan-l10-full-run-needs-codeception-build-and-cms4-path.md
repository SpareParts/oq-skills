---
status: active
dimension: general
date: 2026-11-08
---

# A /tmp phpstan re-run of the FULL phpstan-l10 config is not reproducible without Codeception's generated traits and a `cms4/tests` path — scope L10 to the changed files instead

Why: the `/tmp git-archive + vendor` extraction pattern works for the PHpat-only config
(`phpstan-architecture.neon`: vendor + `build/phpstan.constants.neon` + an empty touched
`build/phpstan.local.neon` is enough, and it runs green on a head-exact tree). The full L10 config
(`phpstan-l10.neon`) needs two more things a read-only checkout cannot supply: (a) the tree under a
path containing the `cms4/tests` segment, because `shoptet.forbidStaticMethod` exempts test code by
path only — see `tmp-phpstan-extraction-must-preserve-cms4-tests-path.md`; without the segment the
rule fires on 800+ test helpers — and (b) Codeception's `_generated` tester traits, which are build
artifacts absent from git, so a full /tmp L10 run dies in thousands of broken-environment errors
that are NOT evidence against the PR. Scope L10 to the changed files with `-c phpstan-l10-ci.neon`
(that works in the extracted tree) and let CI's own L10 run carry the full-repo
baseline-unmatched verification.
Evidence: MIN-182 (nightly code study 2026-11-08) independent review of shoptet/cms4#47745 and
#47744 — a full `phpstan -c phpstan-l10.neon` on the /tmp tree produced thousands of
environment-amplified errors (missing `_generated` traits, `shoptet.forbidStaticMethod` on test
helpers) while the phpat-only config ran green at the same head and CI's L10 run was green; review
artifact b55d9f84.
