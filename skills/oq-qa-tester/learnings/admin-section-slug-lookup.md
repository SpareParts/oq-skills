**Trigger:** Need the admin URL for a legacy controller name (e.g. `ModulesListing`, `CurrencyDetail`).

**Rule:** Query `st_cms`: `SELECT m.controller, l.indexName FROM cms2_admin_section_map m JOIN cms2_admin_section_map_lng l ON l.pageId = m.id WHERE m.controller = '<Name>' AND l.language = 'cs'` — the slug is `l.indexName` (note the join column is `pageId`, not `sectionId`/`id`). URL is `/admin/<indexName>/`.
