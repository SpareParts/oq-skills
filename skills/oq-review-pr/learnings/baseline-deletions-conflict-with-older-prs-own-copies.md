---
status: active
dimension: general
date: 2026-11-10
---

# A PHPStan baseline-block deletion clean against master can still schedule a second conflict with an older open PR that carries its own copy of the same entries

Why: baseline files are merge hotspots, so "the neighbouring PR's entries are untouched" is a claim about this diff only. An older open PR branched from a previous master carries its own copy of the same entries at different line numbers at its head, so merging either side breaks the other even though the reviewed diff conflicts with nothing. When a PR description makes that claim, read the sibling open PRs' baseline state at their heads, not just master, and say in the report that the conflict is scheduled.
Evidence: shoptet/cms4#47852 deletes 8 `SalesChannelQueryBuilder` entries; open #46741 (older, already CONFLICTING with master) carries its own 10-entry block for the same file at its head (`:3974+`) — task MIN-191 review, 2026-11-10.
