---
status: active
dimension: general
date: 2026-10-19
---

# A force-pushed rework invalidates the PR body: re-verify every claim against the new head, and flag the stale body as a major finding when `gh pr edit` is blocked

Why: after a rework deletes a design, the title and body still argue for the deleted one, which misleads the next reviewer about what the diff does — and no CI gate can catch prose. In the evidence PR the body described a port that no longer existed, a NEON alias that had been removed, "call sites unchanged", and 7 files +63/−12, while the actual diff was 8 files +290/−179 with a new command and handler. Treat the body as part of the diff: walk each claim against the head and report the mismatch. When platform tooling blocks `gh pr edit`, escalate the staleness as a major finding so the coordinator corrects it before human review. Related, not restated: `pr-body-inventory-counts-need-diff-verification` and `pr-body-line-citations-drift-after-automated-resort` cover stale counts and line numbers; this covers the whole narrative arguing a design the rework deleted.
Evidence: shoptet/cms4#46450 head 5f6a88dd (task MIN-76, 2026-10-19, artifact b5b65dcd).
