---
status: active
dimension: general
date: 2026-11-01
---

# When a PR replaces a simple status guard with a richer predicate shared by several call sites, review must walk the predicate's entire input domain — every status value × every call site — and diff old vs new per cell

Why: a plain status guard asserts one uniform rule over the whole domain, so there is nothing to overlook; a predicate encodes per-status exceptions, and the change set becomes a matrix whose cells the PR author usually tests only where the reported bug lived. The reported status gets a pin and a sentence in the body, while an adjacent status keeps compiling, keeps its old test (which now asserts the new behaviour by accident or is simply silent), and flips meaning unremarked. Enumerate every status the entity can hold, every call site that shares the predicate, and write the old and new outcome in each cell before judging the diff; any cell that changes without a test pinning it and a line in the body is a finding, even when the new behaviour is defensible.
Evidence: shoptet/multishop-software-factory#131 (task MIN-148, review 2026-11-01), `packages/task-engine/src/runs.ts` `runConsumedInbox()` + `lastInboxConsumingRun()`: the consume guard `status !== "cancelled" && status !== "interrupted"` became "failed runs consume only when they reached a model turn", shared by the `finalizeRun()` consume and the inbox-fence lookup; the tested status was `failed`, and the adjacent `interrupted`-after-a-model-turn cell silently changed from "consumes" to "consumes nothing" — an inbox redelivered to a session that resumes the same context — with no test and no mention in the PR body. Distinct from `checked-exception-throws-ripple-to-every-transitively-throwing-caller` (a caller inventory of a new throw, not a predicate's status domain) and `dibi-guard-passes-but-runtime-leak-remains` (a guard that misses the failure mode entirely, not a per-status exception matrix).
