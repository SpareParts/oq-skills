---
status: active
dimension: naming
date: 2026-10-12
---

# When deleting an options parameter, grep test titles for its vocabulary

Why: test names written to contrast with a deleted option ("X by default", "X when the option is set", parentheticals explaining the option's mechanism) survive as traps: a maintainer reads "by default" and hunts for an override that no longer exists. The tests still pass and look fine in a green run.
Evidence: PR #46174 (MIN-59) — recordsTable.test.tsx:15/19/23 kept "by default" after `showStatusColumn` was deleted (pre-#46009 names had no qualifier); page.test.tsx:114 kept "(they are not e-mail-checked)" describing the deleted verdict mechanism.
Rule: in the same commit that deletes an options parameter, grep test titles for the option's name and its contrast vocabulary, and rewrite the stale qualifiers.
