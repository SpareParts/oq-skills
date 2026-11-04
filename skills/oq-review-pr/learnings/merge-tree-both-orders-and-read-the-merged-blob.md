---
status: active
dimension: general
date: 2026-11-04
---

# A collision report for open PRs touching the same file needs `git merge-tree` in BOTH orders plus a read of the merged blob — "GitHub says MERGEABLE" only means against each PR's own base

Why: two open PRs can each be green and MERGEABLE against their own bases while being textually unmergeable with each other in both directions — `git merge-tree --write-tree A B` and `git merge-tree --write-tree B A` both report conflicts — especially when one PR's base is a stacked branch 8 commits behind master. "Not a conflict today" is then technically true and practically false: the textual conflict exists the moment either PR lands.

The actionable report has three parts: (a) both directions' results, (b) the exact hunks that conflict, and (c) what the merged blob proves about the *non*-conflicting hunks. (c) is what makes the report useful — in the evidence case two `orderBy('domain')` calls survived cleanly into the other PR's tree while only one deleted method conflicted, turning a scary "both files conflict" into a mechanical two-hunk resolution.

Always read the merged blob, not just the conflict list: it exposes resolution traps the diff alone does not. In the evidence case the auto-merged test file kept a new test that would call the method the other PR deletes — a fatal suite failure that neither PR's description mentions, and that a conflict-only report would have missed.

Evidence: shoptet/cms4#47509 vs #46939 (task MIN-162 review, 2026-11-04) — merge-tree conflicts in both orders localized to `findCanonicalsByProject`; the merged blob kept both `orderBy` calls and the new project-variant test, and that test is the trap.
