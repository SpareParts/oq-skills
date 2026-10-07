---
status: active
dimension: code-quality
date: 2026-10-07
---

# Every element of a new public API (optional parameters included) must have either a production caller or a direct test; grep the call sites before repeating a PR body's API claims

Why: an optional `?int $excludedRedirectionId = null` added "for" Update's self-exclusion shipped dead — Update pre-filtered the list instead, the PR body's claim was false, the branch was unreachable in every test, and the default-null semantics (`?int` id, `null === null` skip) silently change loop detection for unpersisted rows if ever used (PR #45868 review). Dead flexible knobs on a new class also seed divergent idioms: two exclusion mechanisms for the next caller to puzzle over.
Evidence: shoptet/cms4#45868 (task MIN-37, review 2026-10-07); RedirectionValidator.php:36,57; UpdateRedirectionService.php:95–106; DomainRedirection.php:8 (`?int $id`).
