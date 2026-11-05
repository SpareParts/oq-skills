---
status: active
dimension: testing
date: 2026-11-05
---

# A test that exercises skip-branch N of a guard must stub every earlier skip/short-circuit condition to the enforcing value, or it passes with the skip's code deleted — verify the negative control by mutation

Why: a guard usually has several independent ways to bail out, and a test named after one of them proves nothing unless the guard actually reaches it. In the evidence PR, `testSkipsCsrfWhenAdminApiSessionCookiesDisabled` never stubbed `Modules::isActive('csrf')`; the un-stubbed mock returned falsy at the earlier "module inactive" check, so the guard short-circuited before the skip under test and the test stayed green with the whole skip block deleted. The fixed test stubs the module active and exercises the intended path — unsafe method, active module, no token — and the reviewer's negative control (delete the skip, rerun) is what makes the test fail. Reviewers should ask for that mutation check on any test whose name claims a skip and whose setup is silent about the earlier bail-outs.
Evidence: shoptet/cms4#46656 review and re-review (task MIN-94, 2026-11-04/05), finding m1; `ControllerMiddlewareTest.php:526-549`.
