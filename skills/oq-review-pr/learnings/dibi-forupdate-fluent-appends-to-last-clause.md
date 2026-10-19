---
status: active
dimension: general
date: 2026-10-18
---

# dibi's `Fluent::forUpdate()` is a `__call` pseudo-clause appending FOR UPDATE to the last-touched clause — reviewers verifying locking must read call order, not the flag name

Why: dibi's `Fluent::forUpdate()` appends the `FOR UPDATE` string to the cursor of the last-touched clause (WHERE if `where()` came last, FROM otherwise, LIMIT after `limit()`). Correct rendering therefore depends on call order (`where()->forUpdate()`), and `fetch()` after `forUpdate()` emits `… FOR UPDATE LIMIT n` — invalid in MySQL, hence the `fetchAll()` idiom. Reviewers verifying "does this lock?" must read the clause order, not just the flag name.
Evidence: shoptet/cms4#44496 rebase review (MIN-88, 2026-10-18) — `vendor/dibi/dibi/src/Dibi/Fluent.php:124-215`, `MarketUpdateRepository.php:164`, `MarketReadRepository.php:156-161`, `SalesChannelLanguageReadRepository.php:21-26`.
