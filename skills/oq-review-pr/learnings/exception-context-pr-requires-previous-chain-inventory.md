---
status: active
dimension: domain-integrity
date: 2026-09-29
---

# An exception-message PR only reaches logs where the catch site chains $e as previous — inventory the previous-argument of every catch, not just the catch's existence

Why: a PR that enriches an exception's message claims a logs/Sentry benefit, but a controller that rethrows `HttpException::fromStatusCode(code, msg)` without the third `$e` argument silently discards the enriched exception on that path — the benefit materialises only on paths that chain previous. Reviewing "all throw sites are caught" is not enough; grep each catch's arguments.
Evidence: shoptet/cms4#45441, admin/controllers/Localization/MultishopLanguageDetailController.php:37 (2-arg rethrow, message swallowed) vs MultishopUpdateLanguageController.php:41 / MultishopRemoveLanguageController.php:36 (both chain $e).
