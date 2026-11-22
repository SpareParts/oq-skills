---
status: active
dimension: testing
date: 2026-11-22
---

# A hardcoded-msgid assertion in a cms4 test is locale-dependent — only expectations built through `_()` are stable, and the CI integration devenv resolves Czech

Why: `_()` output follows the runtime locale, not the test bootstrap. `tests/phpunit/bootstrap.php` does `putenv('LANGUAGE=')`, yet the Cms4 Integration Tests workflow's devenv resolves the Czech catalog, so an assertion comparing `_()` output to a hardcoded English literal fails there ('Doména byla změněna z … na …' vs 'Domain name was changed from … to …'). The locale-stable form is the established pattern (see `underscore-assertions-in-cms4-unit-tests-are-locale-stable`): build the expected value through the same translation call the producer used, e.g. `sprintf(_('Domain name was changed from %s to %s'), …)`, which passes in every locale. When verifying such an assertion statically, check that a cited precedent really is the same pattern: a test that builds its expectation with `sprintf(_(...))` is not evidence that a hardcoded literal is stable, and a bootstrap env-var read does not establish what the CI devenv resolves — say the claim needs CI confirmation instead of marking it statically verified.

Evidence: MIN-233 review round, shoptet/cms4#48487 — the review marked the new hardcoded expectations statically verified citing `tests/phpunit/bootstrap.php:167` and `SentReceiptToEmailCommandHandlerTest.php:66` (which wraps its expectation in `sprintf(_(...))`); CI run 44767229567 on head c7836a7ee9 failed both remark assertions; fixed in commit ffa16404d2 by asserting through the translator.
