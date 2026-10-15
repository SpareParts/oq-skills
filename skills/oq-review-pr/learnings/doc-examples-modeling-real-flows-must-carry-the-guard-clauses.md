---
status: active
dimension: domain-integrity
date: 2026-10-15
---

# A doc example that names a real request class must keep the real controller's null-guards — per-identifier existence passes while the shown combination TypeErrors on a mainline input

Why: when a docs PR replaces a fictional example with a real flow, the reviewer verifies the Request↔Command↔Query COMBINATION (dispatch sites, handler throws, argument types) — but the combination check must include the *guard clauses* around each call, not only the call's own signature. In the evidence PR, every name in the rewritten JSON example was real and the catch was test-pinned, yet the example dropped the real controller's `if ($domain !== null)` guard: the named request's `string|null $domain` met a query constructor's non-nullable `string`, null passed every validation layer (Symfony constraints skip null; the handler's validator returns an empty list for null), and null-domain was the wizard's mainline "no custom domain" path (the FE sends no domain key). A reader copying the example onto the very classes it names gets a TypeError 500. The check: for each property the example passes onward, diff the example's control flow against the modeled controller's — any dropped conditional that changes reachability of a shown line is a fidelity bug, not an elision.
Evidence: shoptet/cms4#46374 re-review (MIN-70, 2026-10-15) — controllers.md:155 at head 75e682fed5 vs admin/controllers/MultiShop/WizardValidateDomainAndNameController.php:50-55, ValidateDomainAndNameRequest.php:12, GetRegistrarForDomainQuery.php:19, DomainDataValidator.php:28-30, frontend/.../MarketAddWizard/steps/NameDecision.tsx:27-31.
