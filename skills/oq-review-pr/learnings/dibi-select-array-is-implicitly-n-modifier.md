---
status: active
dimension: general
date: 2026-10-09
---

# dibi rewrites a single-array `select()` argument to `['%n', $array]` — an explicit `select('%n', $array)` branch is cursor-identical, exists only to satisfy shoptet.dibi.dangerousValue, and collapsing it re-triggers the entry

Why: `Fluent::$modifiers['SELECT'] = '%n'` (vendor/dibi/dibi/src/Dibi/Fluent.php:49) makes `Connection::select($array)` internally identical to `select('%n', $array)` (Fluent.php:180-190), and `Translator` case 'n' handles both assoc (col AS alias) and list shapes. A reviewer or maintainer seeing an `is_array` branch that byte-duplicates the string fall-through except for the `'%n'` argument will reasonably delete it as dead duplication — and CI goes red on a re-appeared `shoptet.dibi.dangerousValue` with nothing on-site explaining it. The `@param literal-string|...` annotation alone does NOT clear the entry (PHPStan sees the union type at the single call). The equivalence and the reason the branch exists must therefore live in the PR body (and ideally a learning) — check for them before flagging such a branch as duplication, and cite them in the PR description when writing one.
Evidence: shoptet/cms4#46019 review (2026-10-09, task MIN-45); cms/packages/Multishop/Infrastructure/Persistence/ReadRepository/MarketRepositoryQueryBuilder.php:61-69; vendor/dibi/dibi/src/Dibi/{Fluent.php:49,180-190, Translator.php:226-235}.
