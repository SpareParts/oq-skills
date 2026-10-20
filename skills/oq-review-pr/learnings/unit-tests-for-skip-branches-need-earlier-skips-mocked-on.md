---
status: active
dimension: testing
date: 2026-10-19
---

# A test that exercises skip branch N of a guard must stub every earlier skip condition to the enforcing value, or it stays green with that branch deleted

Why: a skip chain short-circuits at the first falsy condition, so a test aimed at branch N proves nothing unless every preceding condition is forced to the enforcing value — an un-stubbed module mock returning falsy stops the chain earlier and the assertion passes for the wrong reason. Verified by mutation in the evidence PR: deleting the `isAdminApi && use_cookies === 0` block kept the test green because the earlier module check already short-circuited. For each new skip branch, mutation-test it: delete the branch and the suite must fail. If it stays green, the test was never reaching the branch.
Evidence: shoptet/cms4#46656 review (task MIN-94, 2026-10-19, artifact 0aec49b4) — ControllerMiddleware CSRF test.
