---
status: active
dimension: general
date: 2026-10-03
---

# Check an @see issue's axis, state and actual class list before citing it as documentation

Why: house-style copying propagates stale pointers silently. In cms4, `tests/architecture/Multishop/*` docblocks (@see #32911 "for known violations to fix") point to an issue that tracks PACKAGE-BOUNDARY violations, is closed (2026-03-23), and never mentions the internal-layering or Dibi violators the exclusion lists actually contain. A PR that asserts "the N known violators documented under #X" then makes a false claim in its own body. Before reusing an issue link in a new file or PR description: open the issue and confirm (a) it is open or has a live successor, (b) its violation axis matches (package boundary vs internal layering vs persistence), (c) it names the exact classes. If nothing tracks them, open a follow-up issue and point at that instead.

Evidence: shoptet/cms4#45684 (MultishopDomainLayeringTest docblock + PR body vs issue #32911); pre-existing in MultishopBoundaryTest/MultishopDibiRulesTest docblocks; no repo issue mentions the 3 excluded classes (gh search issues: []).
