---
status: active
dimension: general
date: 2026-11-09
---

# The contents API returns `encoding: none` (empty `.content`) for files over 1 MB; fetch raw instead

Why: `gh api repos/<owner>/<repo>/contents/<path>` caps at 1 MB: bigger files come back with
`"encoding": "none"` and no base64 body, so `base64 -d` yields nothing and a line-citation check
silently "fails to find" evidence that is there. Use
`gh api -H 'Accept: application/vnd.github.raw' 'repos/.../contents/<path>?ref=<ref>'` on the same
path and the bytes arrive; pin the ref so the cited lines are the ones the claim names.
Evidence: MIN-188 review of SpareParts/oq-skills#39 — cms4's `database/migration-zero/st_cms.sql`
(2.3 MB) decoded empty; the raw Accept header returned the page-1204 row at line 2291 at once.
