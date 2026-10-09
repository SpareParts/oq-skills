---
status: active
dimension: general
date: 2026-10-07
---

# A PR head can move while the review is in flight — re-pin the head, verify ancestry, and re-read CI before reporting

Why: the author can push a CI fix mid-review, so both the findings and the "CI is red" headline can be stale by the time the report lands. Before reporting: fetch `pull/<N>/head` again, verify the delegated SHA is an ancestor of the new head (`git merge-base --is-ancestor` exit 0) so the review still applies to the tree being merged, diff the assertions across the reshape commit rather than reading its title — a "test fix" can silently weaken a contract (see `reshaped-tests-can-unpin-previous-contracts.md`) — and re-read CI for the new SHA; red integration on the delegated head does not survive a green pinned head, and findings against removed code must be dropped.
Evidence: shoptet/cms4#45914 (task MIN-40, review 2026-10-07) — delegated head 4c151860 (integration red) vs pinned head 42b54e90 (all green); the reshape diff kept all assertions, so the review's substance survived but the CI headline did not.
