---
status: active
dimension: general
date: 2026-10-12
---

# A `.catch(() => false)` around a boolean query conflates "unreachable" with "verified no"

Why: when a data function's `false` is a *verified negative* (a query executed and matched zero rows), wrapping its rejection into the same `false` silently turns every transient failure into the negative answer, and the caller then acts on a fact it never checked. Read every `X.catch(() => false)` / `.catch(() => null)` on a boolean/optional result by asking what the catch-path value *means* to the caller: if the legitimate negative triggers an irreversible action (abandon, delete, fail-loud), the error path needs its own branch — log, stay inconclusive, retry — even when the happy path is one boolean.

Evidence: shoptet/multishop-software-factory#69 (task MIN-55): `Worker.renewLease` wrapped `heartbeatJob` (false = 0-row guarded UPDATE = lease genuinely lost) in `.catch(() => false)`, so a deploy that recreated PostgreSQL severed the pool and the worker abandoned a healthy run as "lease lost"; one specialist run was wasted (incident 2026-10-11T23:46:38, task MIN-54). The fix branches the catch into "inconclusive: warn and retry next interval". Distinct from `checked-exception-throws-ripple-to-every-transitively-throwing-caller` (that one is about *declared* throw contracts rippling to callers; this one is about the caller *erasing* the throw contract) and from `dibi-guard-passes-but-runtime-leak-remains` (a guard not covering the failure mode, not a swallowed error flattening into a negative).
