---
status: active
dimension: testing
date: 2026-09-27
---

# Committed tests must not use real domain names — require a made-up or reserved one

Why: repro steps often name a real domain (a dev instance or a tester's host), and copying it into a committed fixture leaks a real-world identifier into the repo. Tests should use a reserved RFC 2606 name (`www.example.com`) or the repo's conventional fake domain (`example.cz` in cms4); real domains belong in manual repro steps, not in committed fixtures. Flag any registrable real-looking domain in test constants, MSW fixtures or assertions and ask for it to be replaced.
Evidence: MIN-6 — operator correction in Slack 2026-09-25 ("Don't use real domain name in the test. Make something up instead."); fixed in shoptet/cms4 commit f1a930747b, where the MSW fixture TEST_DOMAIN in frontend/apps/admin-web/src/MultiShop switched from the repro domain to `www.example.com`.
