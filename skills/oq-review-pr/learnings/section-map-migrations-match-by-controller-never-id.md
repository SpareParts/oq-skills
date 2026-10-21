---
status: active
dimension: general
date: 2026-10-20
---

# `cms2_admin_section_map` migrations must resolve rows by controller, never by a hardcoded id — ids hold only in one environment's id-space, and baseline provenance must be checked per row

Why: the section map is a per-environment global table whose `AUTO_INCREMENT` ids follow that environment's insert history, so a migration matching by hardcoded id (`WHERE id IN (1980, 2001, …)`) silently no-ops on environments whose ids differ — production kept `module='multishop'` and the DNS pages 404ed until a follow-up migration re-ungated by controller. The established pattern is `UPDATE cms2_admin_section_map SET module = NULL WHERE controller = 'X' AND module = 'multishop'` (idempotent via the module guard). This extends `cms4-h1-vs-breadcrumb-section-map-columns.md`'s "resolve pageId by controller subquery" from lng-row inserts to UPDATE/DELETE predicates. Second trap when writing the root-cause story: `database/migration-zero/st_cms.sql` is a dump of a long-lived devenv that already records many later migrations as done (22304 done 2025-09-18 with rows 2001/2004 present), so "inserted after the migration-zero baseline" is false for rows a migration-date heuristic would call late — verify each row against the baseline dump, not against release dates.
Evidence: shoptet/cms4#46733 (CZ3MUL1-1099, task MIN-99, review 2026-10-20); `migrations/2026/multishop/cms/CZ3MUL1-1083/expose_dns_section_to_all_merchants_drop.sql`; `database/migration-zero/st_cms.sql:2716-2717`.
