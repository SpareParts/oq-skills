---
status: active
dimension: testing
date: 2026-09-29
---

# expectExceptionMessage(_(msgid)) in cms4 unit tests is locale-stable, not brittle — the producer calls _() with the same msgid at the same time

Why: when a validator/middleware builds a message via `_($msgid)` at runtime and the test asserts via `expectExceptionMessage(_($msgid))`, both calls resolve under the same locale in the same process, so translated and untranslated environments agree; symfony's ValidationFailedException message is `(string) $violations` and expectExceptionMessage is a contains-check, so the assertion holds. Do not flag this pattern as environment-dependent — it is the established style (cf. UpdateLanguageCommandValidatorTest asserting `_('_MULTISHOP_ERROR_MARKET_NOT_FOUND')`).
Evidence: shoptet/cms4#45441, tests/unit/.../UpdateLanguageCommandHandlerTest.php:88; tests/unit/cms/packages/Localization/Language/Validator/UpdateLanguageCommandValidatorTest.php:108.
