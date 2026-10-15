---
status: active
dimension: general
date: 2026-10-12
---

# Verify a revert against the pre-feature baseline, not the forward diff

Why: a revert PR's forward diff (base→head) shows what changed since master, which includes the feature being reverted; only diffing the head against the pre-feature parent (`git show <pre-feature-commit>:<file>`) proves the revert is complete and nothing else rode along. Byte-identity of the restored regions is the strongest evidence a revert is "true"; intentional deviations from the baseline (e.g. keeping a named-options signature that post-dates it) must be named in the PR description, or the next reviewer cannot tell drift from design.
Evidence: PR #46174 (MIN-59) — schema.ts at head is byte-identical to c166200d25^; recordsTable.tsx and DnsSettingsGeneralNameServer.tsx differ from the pre-#46009 baseline only in the options-object signature (an improvement the PR description implies but does not call out against the baseline).
