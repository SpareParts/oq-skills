---
status: active
dimension: testing
date: 2026-10-18
---

# Once a duplicate is collapsed into delegation, a parity test's remaining job is to catch re-inlining of a divergent local copy, not source drift

Why: after dedup the parity assertion is satisfied by construction — the delegee IS the source of truth, so asserting that both sides agree can no longer detect drift in the source. What it still catches is re-inlining: a merge-conflict resolution, a "simplification", or a copy-paste that puts a divergent local copy back next to the delegation. Because the test looks vacuous once you understand the mechanism, state its post-dedup job explicitly in the PR body so a later reviewer does not delete it as redundant, and prove it with a re-inline negative control (inject one divergent branch and show exactly which cases fail). A parity test whose only remaining value is the negative control should carry that control at review time.

Evidence: shoptet/cms4#46564 (task MIN-85) — the reviewer proved it empirically: injecting a single drifted `MERCHANT_NAME` arm makes exactly 1 of 14 cases fail, confirming the surviving test still pins the delegation boundary.
