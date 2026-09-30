---
status: active
dimension: testing
date: 2026-09-29
---

# A reshape that rewrites an exact-count assertion into a find-filter unpins the old contract — diff test semantics across the reshape commit, not just that they pass

Why: when a maintainer reshapes a PR, test edits that keep the suite green can silently drop guarantees: `expect(queryAllByText(m)).toHaveLength(1)` ("rendered inline only, toast suppressed") became `findAllByText(m).find(x => !x.closest('.systemMessage__notification'))` — same green suite, but the suppression property is no longer pinned. When reviewing a reshape commit, diff the assertions themselves (exact counts, negated queries, comments stating contracts) and report any guarantee that became tolerated rather than required.
Evidence: shoptet/cms4#45372, `git diff f1a930747b..pr-45372 -- frontend/.../page.test.tsx` — the `toHaveLength(1)` + "duplicate toast is suppressed" comment removed alongside the behavior change.
