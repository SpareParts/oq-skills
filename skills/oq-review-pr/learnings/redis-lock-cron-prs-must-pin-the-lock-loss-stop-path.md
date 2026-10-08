---
status: active
dimension: testing
date: 2026-10-07
---

# A PR that adds a RedisLock to a cron job must test the extendLock-false → stop path (exit code included) — acquire/skip/release staying green proves nothing

Why: the stop path is the contract that keeps the original incident fixed: when `extendLock()` returns false another worker holds the lock, and the job must stop mid-run with the documented exit code rather than plough on and double-process. The gap survives review unnoticed because acquire/skip/release tests all stay green without it — green coverage of the happy concurrency paths reads as "the locking is tested". In review, name the lock-loss branch explicitly and check a test pins it, exit code and all; an untested stop path in a lock-introducing PR is a blocking finding, not polish.
Evidence: shoptet/cms4#45914 (task MIN-40, review 2026-10-07) — MIN-40 made the missing extendLock-false → stop test the blocking finding; the precedent jobs ship the same path untested: LogisticsReportCheckJob.php:42, ShoptetPayPaymentsCheckJob.php:50, PaymentProcessorJob.php:42.
