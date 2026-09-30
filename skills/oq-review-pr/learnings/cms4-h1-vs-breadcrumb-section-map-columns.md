---
status: active
dimension: general
date: 2026-09-29
---

# cms4 admin H1 comes from cms2_admin_section_map_lng.alternativeTitle (sprintf via useAlternativeTitle), the breadcrumb from the plain title column

Why: fixing a label on a cms4 admin page requires knowing which of the two lng columns feeds which UI element: `PageAdmin::setTitle` (wrapped by `useAlternativeTitle($name)`) sprintf's `alternativeTitle` (single `%s`, name htmlspecialchared) into the H1, while `BackendMapHelper::getPageQuery` selects the plain `title` for the breadcrumb/sidebar. Target the wrong column and you "fix" the H1 by corrupting the breadcrumb, or vice versa. Migrations updating these rows must resolve pageId by controller+module subquery (never LAST_INSERT_ID from an old migration) and must be deploy-order-safe (code tolerates both row states — migrations run post-deploy).
Evidence: MIN-15 migrations/2026/multishop/cms/MIN-15/01 (title → breadcrumb) + 02 (alternativeTitle → H1); cms/packages/Layout/Model/PageAdmin.php:102-121; cms/packages/Layout/Helper/BackendMapHelper.php:69-77; seeds migrations/2025/multishop/cms/22304 and migrations/2026/multishop/cms/22496.
