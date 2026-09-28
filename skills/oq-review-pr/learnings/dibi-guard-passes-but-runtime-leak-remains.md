---
status: active
dimension: domain-integrity
date: 2026-09-28
---

# A source-reference layering guard (PHPat/Dibi) passes after a catch is removed even while untranslated vendor exceptions still flow through the class at runtime — always check collaborators called outside the new try/catch, not just imports

Why: MultishopDibiRulesTest only sees `use Dibi\Exception` in Domain/Application source, so removing the reference keeps the guard green while MarketReadRepository::find() still lets DibiException escape through ChangeMarketStatusOperation on the (currently undispatched) validation path. A green layering guard proves the import is gone, not that the vendor exception cannot reach callers — after any new try/catch, check the class's collaborators for calls made outside it that can re-leak the vendor exception.
Evidence: shoptet/cms4#45407, cms/packages/Multishop/Domain/Market/Operation/ChangeMarketStatusOperation.php:25-39, cms/packages/Multishop/Infrastructure/Persistence/ReadRepository/MarketReadRepository.php:21-31 (task MIN-10, independent review 2026-09-28).
