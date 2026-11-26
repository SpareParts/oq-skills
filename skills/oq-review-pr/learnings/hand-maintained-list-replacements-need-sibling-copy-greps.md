---
status: active
dimension: general
date: 2026-11-26
---

# Hand-maintained-list replacements need sibling-copy greps

Why: a hand-maintained name or prefix list drifts from the contract it approximates, and the drift rarely lives in one place — UI mirrors, scripts and helpers carry shallower copies of the same logic. When a fix replaces the list with the canonical contract mapping, grep the repository for the old list's tokens (family names, prefixes, the regex itself) to find those copies: they keep the original miss and the backend fix does not touch them. In the platform review that produced this rule, the worker's platform-tool regex missed five tool-contract families, and the web session view carried a client-side copy of the same dedup with the same first-underscore-only miss — pre-fix events kept rendering duplicated after the worker fix.

Evidence: shoptet/multishop-software-factory PR #180 / task MIN-1003 — apps/worker/src/worker.ts PLATFORM_TOOL (removed; missed github/jira/retrospective/code_study/platform) vs apps/web/src/lib/session.ts platformName; found by the review round's sibling grep.
