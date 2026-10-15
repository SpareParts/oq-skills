---
status: active
dimension: domain-integrity
date: 2026-10-10
---

# A maintenance rule the existing code cannot satisfy without breaking production is rule-text overreach, not deployed lag

Why: the teach-the-rule learning ("keep the rule, note the lag") pushes reviewers to flag any softening of a doc rule as weakening. But when the rule as written is unfollowable for a maintained class — e.g. "single public entry point" for an orchestrator whose extra public method is pinned by a published Contracts interface and called in production — keeping the rule text would instruct breaking the contract. Distinguish: deployed code lagging a satisfiable rule (rule stays, lag noted) vs rule text misdescribing its object (correct the text, keep the norm, note the exception). Amends the boundary of `multishop-docs-teach-the-rule-not-deployed-lag`, not its rule.
Evidence: shoptet/cms4#46086 (MIN-48 review) — orchestrators.md:45→:49 "single `__invoke` entry point" unfollowable for CountryDetailViewOrchestrator (Contracts-pinned getMappedMarkets called at admin/controllers/CountryDetailController.php:252); reviewer adjudicated the softening as the rule honored, not weakened.
