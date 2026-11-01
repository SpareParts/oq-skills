---
status: active
dimension: domain-integrity
date: 2026-11-01
---

# A "replace own stale row" heal must remove UNCONDITIONALLY and inside the insert's transaction — its ownership list may come from a different table than the unique key guarding the insert

Why: the list the validation iterates and the constraint that rejects the insert can come from different tables. In the evidence PR the assert walked `findByProjectId()` — active `project_domains` redirect rows — while the insert was guarded by a global `UNIQUE KEY fromHost` on legacy `domain_redirects`. A legacy row with no active `project_domains` twin is invisible to that snapshot: it passes the filtered assert (filter and assert share normalizer and identity), survives a delete conditioned on "the snapshot showed an own row", and trips the unique key at `save()`. The symptom is a duplicate reported for a host the project does own — or, where the caller swallows `RedirectionAlreadyExistsException` as "another project took it", a replace that silently does nothing. Correct shape: unconditional delete scoped by the write repository's own predicate (`fromHost IN hostVariants AND projectId = own`), inside the same `runInTransaction` as save and the insert, so a failed save rolls the delete back. Ask which table produced the validated list before accepting a condition on it.

Evidence: shoptet/cms4#47336 (task MIN-147, review 2026-11-01, artifact `980f6c0d`), `CreateRedirectionService.php::createRedirection()` — head `c19391005d` vs commit `980f8951e1`: the first implementation conditioned `removeByFromHost()` on the `findByProjectId()` snapshot and ran it before the transaction; the review caught the no-active-twin case and commit 2 moved the unconditional remove inside the `runInTransaction` owning `save()` + `attach()`. Distinct from `dibi-guard-passes-but-runtime-leak-remains` (a guard missing the failure mode).
