---
status: active
dimension: testing
date: 2026-10-06
---

# When a PR vacates a legacy namespace, the shouldNotExist() guard must cover every namespace the PR emptied — or its method name must honestly scope itself to the subset it guards

Why: otherwise the vacated-but-unguarded namespace silently re-grows behind a green architecture suite. In the evidence PR the new PHPat rule `test_legacy_admin_controllers_namespace_should_not_exist` guarded only `Shoptet\Admin\controllers\MultiShop` while the PR also vacated `Shoptet\Admin\controllers\Localization` — nothing anywhere in tests/architecture referenced that second namespace, so classes could return to it without failing any architecture test. Both directories are owned by the same team per CODEOWNERS, so extending the guard was in scope. The reviewer flags were raised by 5 of 7 dimension subagents independently.
Evidence: shoptet/cms4#45783 (task MIN-33, review 2026-10-06), tests/architecture/Multishop/MultishopBoundaryTest.php:91-95.
