---
status: active
dimension: general
date: 2026-09-29
---

# "Stacked PR" must be tested with git lineage, not the PR base_ref

Why: a PR's base branch and its head's git parent are independent — setting base=<lower PR's branch> while cutting the branch off master makes GitHub compute the diff from the merge-base, pulling unrelated already-merged commits into Files-changed (here: 12 files / +435 lines of another team's filemanager work inside a 4-file FE PR), and the upper head never contains the lower PR's code, so its CI never tests the combined tree. A true stack requires `git merge-base --is-ancestor <base-head> <upper-head>` to exit 0. The intended merge order often still works (auto-retarget after the lower PR merges collapses the diff), so the defect hides until a human opens Files-changed.
Evidence: shoptet/cms4#45486/#45487 (task MIN-15, 2026-09-29): FE head c91ede3b7d's parent = master e81c15bb55, not BE head 73a960017d; PR 45487 displayed 16 files (+516/−133) while the semantic diff was 4 files (+81/−80).
