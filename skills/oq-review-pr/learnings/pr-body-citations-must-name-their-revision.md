---
status: active
dimension: general
date: 2026-10-10
---

# PR bodies quoting pre-edit text must cite pre-edit line numbers, and label which revision each citation refers to

Why: doc-sync PRs quote the old text (Problem section) and the new text (Change section) in one body; citing the old text with post-edit line numbers produces citations that match neither revision, and reviewers verifying against either state flag the whole body as inaccurate. State the revision (master vs head) per citation, or cite each quote against the revision it describes. Extends `pr-body-line-citations-drift-after-automated-resort` (re-sort drift) and `pr-body-inventory-counts-need-diff-verification` (counts): the common rule is that a PR body's citations are reviewable artifacts tied to a named revision.
Evidence: PR shoptet/cms4#46086 body (MIN-48) — Problem section cites master text at head line numbers (":47" for master :45, ":49" for master :47, ":32-41" for master :32-39); Change-section citations all recount correctly at the head.
