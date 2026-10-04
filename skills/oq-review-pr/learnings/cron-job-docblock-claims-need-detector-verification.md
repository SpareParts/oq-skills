---
status: active
dimension: domain-integrity
date: 2026-10-04
---

# Verify a job docblock's "when" claim against the detector, not the job's own code

Why: a cron job's catch types and dispatch calls describe its failure handling, not its
domain trigger. Docblock headlines written from the job's perspective drift into plausible-
sounding but false trigger conditions: PR #45687's docblock said the job fixes the default
language option "when it no longer matches the sales channel languages", but the detector
(`LanguageOptionMismatchResolver::detectTargetLanguageCode()`) reads only two project
options, and the sales channel languages are an output of the fix — in the canonical
broken state the two agree (`LanguageSynchronizer` assigns `[DEFAULT_LANGUAGE_CODE]` when
the add-on is off). The codebase already carried the truthful pairing in three places
(command docblock, resolver docblock, LanguageMismatchChecker log).

Evidence: PR shoptet/cms4#45687, scripts/cron/LanguageOptionMismatchJob.php:15-16 vs
cms/packages/Localization/LanguageOptionMismatch/LanguageOptionMismatchResolver.php:49-67
and cms/packages/Multishop/Application/Synchronization/PartialSynchronizers/LanguageSynchronizer.php:38-45.
