---
status: active
dimension: domain-integrity
date: 2026-10-07
---

# A unit suite that pins each fail-fast step with a single-violation test does not pin their ORDER; a refactoring that moves a step between others stays green on both orders, so diff exception precedence on multi-violation inputs

Why: a single-violation test constructs one broken input per rule, so it never observes which exception fires when two rules are violated at once. In the evidence PR, moving the create-only source-is-active-domain check after the whole extracted validator changed which exception fires for inputs violating two rules — a different merchant-visible message — while every test stayed green (PR #45868 review). Catch it by constructing the pairwise intersections (source violates rule A + target violates rule B) and asserting the master-order exception before and after the refactor.
Evidence: shoptet/cms4#45868 (task MIN-37, review 2026-10-07); CreateRedirectionService master :119–125 vs head :106–119; MultishopDomainRedirectionCreateController.php:60–68 maps the two exceptions to different messages.
