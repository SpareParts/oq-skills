---
status: active
dimension: domain-integrity
date: 2026-10-18
---

# Nested `runInTransaction` on one connection is savepoint nesting in cms4 — a repository method that "opens its own transaction" composes with an outer application transaction

Why: in cms4, nested `BaseDatabase::runInTransaction` on one connection is savepoint nesting (`nest_transactions => true` in the default driver config; custom `MySqlDriver` savepoint stack), so a repository method that "opens its own transaction" composes with an application-level transaction on the same connection: locks held to the outermost commit, inner commit a no-op, inner throw unwinds savepoints first. Do not flag "nested transaction" in shoptet codebases as double-BEGIN without checking `nest_transactions`. Distinct from `savepoint-release-is-not-commit-for-nested-event-claims`, which is about "event dispatched after commit" claims on the nested path; this one is about transaction composition and locking semantics.
Evidence: shoptet/cms4#44496 rebase review (MIN-88, 2026-10-18) — `vendor/shoptet/lib-common/src/Database/Database.php:298`, `vendor/shoptet/lib-common/src/Database/MySqlDriver.php:200-283`, `cms/packages/Connectors/BaseDatabase.php`.
