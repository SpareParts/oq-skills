---
status: active
dimension: general
date: 2026-09-29
---

# In admin-web, a useForm/useAjaxMutation onError that renders field errors inline does not suppress the default error toast — suppression requires an errorNotification override returning []

Why: `useAjaxMutation.onError` runs `notifyError(error)` in `finally` (`Core/hooks/fetching/useAjaxMutation.ts:141-142`), and the default FetchError toast maps every `responseData.errors` entry to one toast (`useAjaxNotifications.ts:191-201`). A component's `onError` that also calls `setError(field, …)` therefore shows the same message twice — inline and as a toast. Reviewers seeing "duplicate toast" should check whether suppression was intended and removed, not assume a double-render bug; conversely, a test asserting exactly one occurrence (`toHaveLength(1)`) is pinning active suppression wiring.
Evidence: shoptet/cms4#45372 head 017aff6e9b — maintainer's reshape removed the `errorNotification` override; probe on a head-exact tree showed the domain-conflict message twice (`systemMessage__notification` toast + `v2FormField__error` inline); pre-reshape page test had pinned `toHaveLength(1)`.
