---
status: active
dimension: general
date: 2026-10-18
---

# A CODEOWNERS claim of a per-file cron job must also claim its direct unit test

Why: the per-file job / per-file test pairing is an established repo convention — cms4's CODEOWNERS claims the job and the matching test in the same team's block (the ai-rnd orange blocks pair `/scripts/cron/<X>Job.php` with `tests/unit/scripts/cron/<X>JobTest.php`). A rule that claims only the job leaves the test unowned, which is exactly the test-only-PR refusal mode the CODEOWNERS change cites as its motivation: a later PR that touches only the test cannot be reviewed by the team that owns the job, so a test-only fix is either blocked or routed to the wrong owner. When reviewing a CODEOWNERS diff that adds or edits a per-file job claim, check the sibling test path in the same block and flag it if it is missing.

Evidence: shoptet/cms4#46561 (task MIN-82) claims `/scripts/cron/DnsValidationJob.php` (line 680) but not `tests/unit/scripts/cron/DnsValidationJobTest.php` (`#[Group('Multishop')]`), while claiming the analogous `LanguageOptionMismatchJobTest.php` in the same block. The independent review (artifact 8f4cbb65) flagged it as the one finding four dimensions independently surfaced.
