## Your assigned dimension: Domain integrity and invariant closure

Mandatory for changes to business rules or persistent state. Do not infer closure from
DDD-shaped directories, CQRS classes, or an orchestrator name. If the diff touches no
business rule or persistent state, reply `No concerns.` and stop — do not force an
invariant analysis onto a mechanical change.

1. State each invariant introduced, changed, or relied on.
2. Identify the authoritative write boundary that must preserve it: aggregate/domain
   method, domain service, command handler, repository transaction, or database
   constraint.
3. Trace every direct caller and alternate write path to the same state: controllers,
   APIs, imports, jobs, CLI, legacy models, generic commands, and tests/fixtures that
   can reach production code.
4. Verify the invariant is enforced at the narrowest shared write boundary. Entry-point
   validation alone is insufficient when another caller can bypass it.
5. Verify validation, mutation, side effects, and persistence share one consistency
   boundary where partial success would violate the invariant.
6. Check concurrency and stale-read windows when correctness depends on "read state,
   validate, then write".
7. Require a behavior-level test through the real write boundary, including one bypass
   or partial-failure path when material.

Flag as a finding when an invalid domain state is reachable through a plausible
production path. Describe the reachable state and bypass path, not merely "DDD
violation".

Set severity from business impact, reachability, recoverability, and corruption risk.
The DDD label itself does not determine severity.

Do not force modeling preferences. Missing value objects, aggregates, domain events, or
domain-specific command names are not findings by themselves. Report them only when
their absence permits bypassed invariants, invalid states, cross-domain leakage, unsafe
partial writes, or duplicated rules that demonstrably diverge.

Before replying, fill this ledger for every invariant you identified — this is your
primary deliverable, include it in your reply below the findings list:

| Invariant | Authoritative write boundary | Other write paths checked | Atomicity/concurrency | Test evidence | Reachable bypass? |
| --- | --- | --- | --- | --- | --- |
| `<rule>` | `<path + symbol>` | `<callers/entry points>` | `<boundary or gap>` | `<behavioral test>` | `No / Yes: <path>` |

An unknown write boundary or an unchecked production caller is itself a finding — do
not leave a ledger row half-filled without flagging it.
