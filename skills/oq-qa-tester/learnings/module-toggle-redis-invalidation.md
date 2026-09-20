**Trigger:** Toggling a module on/off for a project by inserting/deleting a row in `st_<projectId>.modules` (single column `indexName`).

**Rule:** Also delete the Redis cache keys `<projectId>:modules` and `<projectId>:modules:ts` via `./docker/dev compose exec keydb redis-cli DEL "<projectId>:modules" "<projectId>:modules:ts"`. After that, propagation to admin requests is immediate (verified per-request) — no service restart needed. Section-map visibility (`cms2_admin_section_map.module` + `hideInactiveModule=1`) follows the same cache, so gated pages appear/disappear right away.
