---
status: active
dimension: general
date: 2026-10-26
---

# In the cms4 blobless clone, `git grep <pattern> <rev> -- '*.php'` (pathspec-only) can time out; scope the rev-grep to top-level directories instead

Why: a pathspec-only grep against a rev fetches blobs for every matching file across the whole tree on demand; on the multi-gigabyte cms4 clone that exceeded the 120 s tool timeout twice in one review run (pattern `getCdnUserDomain` repo-wide at a rev). Scoping the same grep to the relevant top-level directories (`-- 'cms' 'admin' 'tests' 'docs'`) completed in seconds, and greping **master's worktree** for remaining callers (per the class-move learning) needs no blob fetches at all. Combine: rev-scoped grep on the directories you must compare (head vs master), worktree grep on master for the caller inventory.
Evidence: shoptet/cms4#46938 review (MIN-129, 2026-10-26) — `git grep -n "getCdnUserDomain" refs/pr-review/46938 -- '*.php' '*.md' '*.tpl'` timed out at 120 s; `-- 'cms' 'admin' 'tests' 'docs'` returned instantly (0 hits at head, 13 on master).
