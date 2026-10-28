---
status: active
dimension: general
date: 2026-10-28
---

# When a PR body justifies a decision with "tests pin X", grep the cited tests for the assertion that actually pins X — a test named after the contract can pin only a weaker property

Why: a test name describes the scenario, not the guarantee; only the assertion inside it does. "Four tests pin the redirect message" was refuted by opening the file: the four cited tests pin only the exception TYPE (`expectException(InvalidArgumentException::class)`), and `expectExceptionMessage` appears zero times in the whole file — any message, or none, keeps them green. The claim therefore justified a decision with a guarantee that does not exist, and a reviewer who repeats the body's justification without opening the assertions signs off on a pin nobody can break. The check is mechanical and cheap: take the cited test names or line numbers, grep the file for the assertion that would fail if the claimed property changed (here: `expectExceptionMessage`), and if it is absent, say which weaker property the tests actually pin. Same family as `pr-body-inventory-counts-need-diff-verification` — verify the artifact behind the claim rather than trusting the prose — applied to causal justifications ("this is safe because tests pin it") rather than to counts.

Evidence: shoptet/cms4#47142 review (task MIN-135, 2026-10-28). The PR body claimed "four tests pin the redirect message"; the four `testConstructorThrowsWhenARedirectRow*` tests in `tests/unit/cms/packages/Multishop/Domain/ProjectDomain/Model/ProjectDomainTest.php:18-80` pin only the exception type (`expectException` at :20/:40/:60/:80), verified: zero `expectExceptionMessage` occurrences in the file. The proposed learning came from the review artifact and was verified first-hand against the file before being written here.
