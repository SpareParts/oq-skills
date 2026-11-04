---
status: active
dimension: domain-integrity
date: 2026-11-04
---

# An ORDER BY prescribed in a brief must be verified against the SELECT source's column list (the view), not the base table's

Why: a brief can name a base-table column as the tie-break for a query that selects from a view exposing no such column. In the evidence case the brief prescribed `->orderBy('id')` — `project_domains.id` — for a query selecting from the `routing_domains_active` view, which exposes exactly 8 columns (`domain, salesChannelId, isCanonical, projectId, redirectionTargetPattern, context, databaseHost, silo`) and no `id`. Implementing it verbatim would have been a production SQL error. The "obvious" escape (add the column to the view) cannot ship in the same deploy either: migrations run *after* deploy and the needed `fwd` stage is skipped by the task release (`migrations/AGENTS.md:10,18-19`), so the fix would be a two-PR sequence.

When reviewing a brief-prescribed ORDER BY: read the view definition before judging the order key — `database/views/*.sql`, the schema dump's `/*!50001 VIEW*/` line, and the latest `CREATE OR REPLACE` migration can all differ, so check the one that actually runs last. Then judge the *semantics* the implementer claims ("lowest hostname", not "oldest row") against the columns actually available, and require the body to state the real tie-break rather than the brief's wording.

Evidence: shoptet/cms4#47509 review (task MIN-162, 2026-11-04) — `database/views/st_cms.sql:161-191`, `database/schema/st_cms.sql:4268`, migrations CZ3MUL1-940/01 and CZ3MUL1-972; the implementer's correction verified true, the original brief's `->orderBy('id')` would have broken production.
