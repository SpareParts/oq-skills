---
status: active
dimension: testing
date: 2026-10-12
---

# A fixture override knob dies with its last test caller

Why: delegatedPageProps-style override parameters exist only for tests; when a PR deletes the last test that passes the override, the parameter, its union member and its `?? fallback` arm become dead in the same commit. Keeping the knob "for future tests" is speculative surface a reviewer must keep parsing, and when a sibling knob is removed in the same PR the survivor looks intentional.
Evidence: PR #46174 (MIN-59), frontend/apps/admin-web/src/Core/vitest/msw/admin/multishop/dns-settings/responses.ts:93-114 — the `emailRecords` override lost its only caller (page.test.tsx flag-off test trimmed to `{ emailManagedByShoptet: false }`); `omitEmailFields` was removed, `emailRecords` stayed.
Rule: when a PR deletes the last consumer of a fixture-factory override, delete the override in the same commit; the unconditional default emission alone carries the wire-contract story.
