---
status: active
dimension: architecture
date: 2026-10-12
---

# When a bug's root cause is two hand-copied predicates drifting, the fix must tie them structurally (shared helper or parity test), not with a prose comment

Why: when a review finding says "reader B forgot the gate reader A has", the tempting fix is to copy the missing condition and add `// Mirrors X's gate`. That re-arms the same bug: the tie is prose, and the next edit to either side silently re-opens the window. The cms4 MIN-44 status-endpoint fix (PR #46008, MultishopDnsStatusController vs DnsSettingsOrchestrator) is the archetype: the EMAILS freshness gate now lives in two places kept in sync by a one-line comment.
Rule: fix the class, not the instance: extract the predicate onto the state object both readers consume (e.g. a method on the DTO), or add a test that asserts both readers agree. If the duplication is accepted for now, name it in the PR description as a known drift risk so the next reviewer looks for the third reader.
Evidence: shoptet/cms4#46008 (MIN-44 single-commit review, 2026-10-12).
