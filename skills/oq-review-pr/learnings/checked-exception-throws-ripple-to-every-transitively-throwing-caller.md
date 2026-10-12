---
status: active
dimension: general
date: 2026-10-12
---

# A new `throw` of a checked exception ripples `missingType.checkedException` onto every caller that transitively propagates it, so the same PR must add `@throws` to (or catch in) each of those production callers

Why: cms4's PHPStan L10 CI (`phpstan-l10-ci.neon`, `missingType.checkedException`) fails on the CALLING methods, not on the method that throws — the static analyser walks each method's uncaught throw set and demands an `@throws` (or a catch) wherever the checked type escapes. So a PR that makes a handler throw a `Contracts` `CheckedException`-based exception (which `extends \Exception`) is red in the full-repo run even when the changed file itself is clean, until every production caller whose method now transitively throws it carries `@throws` or a catch. A scoped "PHPStan on the changed files" verification cannot see this: the errors live in files the diff does not touch, and only the full-repo CI run surfaces them. Before accepting the change, walk the call graph from the throwing site and check `extends` of the exception (`Contracts` `CheckedException extends \Exception` → checked → ripple); do not rely on a files-only run.
Evidence: shoptet/cms4#46107 (MIN-54, review 2026-10-12) — handler throw added; full-repo PHPStan L10 CI run 38185752048 red with exactly 3 caller-side `missingType.checkedException` errors (`UpdateCashDeskCommandHandler.php:90`, `UpdateInStoreSalesChannelCommandHandler.php:69`, `MarketSettingsSubmitOrchestrator.php:233`) while the implementer's scoped files-only run was clean. Distinct from `two-checkedexception-bases-differ` (which twin class an exception extends) and `phpat-docblock-throws-dependencies-are-guarded` (PHPat, not PHPStan).
