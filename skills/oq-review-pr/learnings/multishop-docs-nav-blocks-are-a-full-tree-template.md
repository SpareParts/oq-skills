---
status: active
dimension: readability
date: 2026-10-11
---

# A new Multishop docs page must copy the full navigation tree into its emoji nav block — truncating it to a few entries breaks the byte-identical house template every sibling carries

Why: all ten sibling pages under `cms/packages/Multishop/docs/` carry the same nav tree (Main README, "What is Multishop?", the Clean Code section with its Architecture / Message Bus / Controllers / Orchestrators children, the Tests subsection, plus the "Here we are!" self-marker), with the marker moved onto the page's own line. A new page that lists only a subset looks house-styled at a glance but silently drops navigation — and if no sibling nav lists the new page, it is discoverable only from `Multishop.md`. Copy the full tree, move the marker, and add the new page to the siblings' navs (or accept and note the index-only discoverability).
Evidence: shoptet/cms4#46101 (MIN-51, 2026-10-11) — `cms/packages/Multishop/docs/dns-validation.md:5-11` vs `coding/orchestrators.md:6-16`, `coding/queries-and-commands.md:7-17`, `Multishop.md:4-16`; flagged independently by three review dimensions. Verified still true at the final head `becc8a3bd4`.
