---
status: active
dimension: testing
date: 2026-11-09
---

# A permission-403 functional test must enable the page's module, or setRights' inactive-module branch masks the 403

Why: `PageAdmin::setRights()` grants `allowedAccess = true` for a logged-in user while the page's
module is inactive (cms/packages/Layout/Model/PageAdmin.php:235-237, the "show module order
screen" branch) — BEFORE the permission-level and `admin_user_permissions` lookups run. A 403 test
on a gated admin page therefore fails confusingly (passes with 200) when the section-map row's
`module` is not active in the test environment: the test sees the module-order branch, not the
permission branch. The page's module comes from the `cms2_admin_section_map` row (column 7), not
from the controller. So the Cest must `enableModule('<the page's module>')` (snapshot + restore
in `_before`/`_after`), and the reviewer must check which module the section-map row names, not
what the controller requires.
Evidence: shoptet/cms4#47750 — the new 403 case gates SaveProjectLanguagesOrderController behind
page 1204 (`cms2_admin_section_map`, st_cms.sql:2291, `module = 'foreignLanguages'`), which forced
`$I->enableModule('foreignLanguages')` in the Cest's `_before`; without it the inactive-module
branch would answer 200 and the permission path would never run.
