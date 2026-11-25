---
status: active
dimension: general
date: 2026-11-25
---

# An environment claim added to an agent prompt is checked against every configured instance, not just the incident's

Why: shared prompts (platform profiles, skill texts) are read by runs in every project's
workspace, so a fact true of one project's configuration, universalized into shared prose, is
false for the rest and misleads the platform's own runs. Before approving "clones do X" /
"the environment has X" prose, grep the config knob that varies and scope the claim to it (or
state it conditionally). The prescribed action may still be universal when it is safe in every
configuration — say that instead.
Evidence: shoptet/multishop-software-factory#173 review (2026-11-25 review round) — the new
agents/coordinator.md bullet said "The clone fetches only the default branch" as a universal,
but `single_branch` is opt-in (default false, packages/contracts/src/workspace.ts:22) and only
cms4 sets it (config/projects.yaml:24); the other projects' clones are full clones. Fixed by
scoping the claim to the config knob; the explicit-fetch and explicit-lease commands stayed,
now stated as working "in every clone" (verified empirically in both clone types).
