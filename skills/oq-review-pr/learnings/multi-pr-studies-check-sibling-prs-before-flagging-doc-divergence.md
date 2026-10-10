---
status: active
dimension: general
date: 2026-10-10
---

# When a code PR's effect makes a normative doc sentence stale, check the same study's sibling PRs before flagging — the divergence may already be fixed there

Why: nightly studies routinely ship a docs PR next to a code PR; a code deletion that orphans a doc claim ("keep a single __invoke") can draw the same ⚠️ from most dimensions independently, each unaware the sibling PR rewords the exact sentence. The real residual is then only merge order (which PR lands first), not the diff. Fetch the sibling head (`git fetch origin pull/<N>/head`) and diff the cited sentence before repeating the finding as actionable.
Evidence: shoptet/cms4#46087 review (MIN-48) — 4/7 dimensions flagged orchestrators.md:45/:26 staleness; sibling PR #46086 head cba50d5ce7 already softens both sentences to wording that remains true post-#46087; finding downgraded to a merge-order note.
