---
status: active
dimension: testing
date: 2026-11-09
---

# An `is_numeric()` guard is the house idiom for `(int)` on `grabFromDatabase()`, not a bare cast

Why: `$I->grabFromDatabase()` is annotated `@return mixed` (Codeception module-db), so a bare
`(int)` cast fails PHPStan L10's `cast.int` rule ("Cannot cast mixed to int.") and turns CI red on
a file the author often never analyzed locally. The repo's established pattern is the guard:
`$raw = $I->grabFromDatabase(...); $value = is_numeric($raw) ? (int) $raw : <sensible default>;`
— seen in tests/functional/Admin/Customer/CustomerDefaultDeliveryAddressCest.php:221 and
tests/functional/Admin/Products/ManualCsvImportDeletedPricelistCest.php:149-150. Prefer it over
`intval()` or asserting the type first; it keeps the strict-rules suite green and states the
fallback explicitly.
Evidence: shoptet/cms4#47750 — CI run 42543075670 ("Cms4 PHPStan", job "PHPStan L10 PHP 8.5")
failed with `cast.int` on the new Cest's `(int) $I->grabFromDatabase(...)` snapshot at
tests/functional/Admin/Localization/MultishopSaveProjectLanguagesOrderControllerCest.php:21;
fix commit 71f92ad0c2 switched to the `is_numeric()` guard and the same workflow went green.
