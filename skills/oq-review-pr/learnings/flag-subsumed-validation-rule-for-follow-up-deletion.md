---
status: active
dimension: code-quality
date: 2026-09-29
---

# When a new same-message rule strictly subsumes an older one in a shared validation helper, name the subsumption and propose deletion as non-blocking follow-up

Why: adding a stricter rule (hostname) next to a laxer same-message rule (format) is behavior-neutral under first-error-wins mapping, so tests stay green and nothing forces the cleanup — but the vestigial rule becomes a naming trap (a maintainer edits `format` believing it the BE-mirroring syntax check, or deletes `hostname` believing `format` already covers it). In a one-concern mirror PR keeping both is fine; leaving the subsumption unnamed and unpinned is not. Verify subsumption by fuzz over the label alphabet, then flag for follow-up deletion.
Evidence: shoptet/cms4#45366; frontend/apps/admin-web/src/MultiShop/common/utils/domainValidation.ts:25-26.
