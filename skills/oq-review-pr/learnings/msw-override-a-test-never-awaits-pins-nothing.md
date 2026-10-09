---
status: active
dimension: testing
date: 2026-10-08
---

# A page test that registers an MSW override for a polled endpoint but asserts only static-payload UI pins nothing about the override

Why: the poll fires on a 5s interval after the synchronous assertions pass, so the overridden body may never be fetched/parsed before the test ends; a schema rejection of the new body would not reliably fail. Await a poll-derived cue or assert the query state.
Evidence: PR shoptet/cms4#46009 review (task MIN-44, 2026-10-08); `page.test.tsx:143-151` vs `useDnsValidationStatus.ts` / `dnsStatusPolling.ts`.
