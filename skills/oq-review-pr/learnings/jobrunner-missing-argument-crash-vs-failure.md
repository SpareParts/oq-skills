---
status: active
dimension: domain-integrity
date: 2026-10-26
---

# A cron-job PR that turns a required `getInputArgument` into an optional one plus a controlled `FAILURE` changes the operator-visible contract — the body must name the exit-code and log difference, not only the new validation

Why: `Shoptet\Scheduler\Job::getInputArgument(string $name, bool $isRequired = true): ?string` (cms/packages/Scheduler/Job.php:77-88) throws `RuntimeException` when a required argument is missing. Uncaught, that throw reaches `JobRunner`'s `catch (\Throwable)` (cms/packages/Scheduler/JobRunner.php:186-197), which logs `Scheduler job failed` at critical and returns `SchedulerException::JOB_ANOTHER_EXCEPTION_CODE` (100, cms/packages/Scheduler/SchedulerException.php:13). Reading the argument with `false` and returning `Job::FAILURE` (1) with the job's own error line is a quieter path: an ordinary 1-coded red run whose error text is the job's, no critical log, and alerting keyed on exit code 100 never fires. The queue is not part of the difference — `JobRunner` dequeues the job before `run()` (JobRunner.php:132) on both paths. Both are legitimate, but a body that only describes "now validates the argument" hides a behavior change operators and alert rules depend on.
Evidence: review of shoptet/cms4#46958 (task MIN-124), which made exactly this switch for `marketId` in `UpdateMarketDomainJob`; the review verified both paths against the code cited above.
