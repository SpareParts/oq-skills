## Your assigned dimension: Naming consistency and intent

Check naming beyond surface conventions. Review classes, interfaces, methods,
properties, variables, parameters, test names, config keys, and comments together as
one vocabulary.

- Do names describe the actual responsibility/behavior, not just an implementation
  detail?
- Do class and method names communicate the same abstraction level, or does one say
  "resolver/helper/getter" while the code actually implements a policy, decision,
  command, side effect, or orchestration?
- Do boolean method/property/variable names match their semantics, especially
  fail-safe defaults, negation, and policy decisions (`is*`, `has*`, `can*`, `should*`,
  `must*`)?
- Are variable and parameter names consistent with the domain concept they carry
  throughout the diff?
- Is terminology reused consistently across production code, tests, DTOs, config,
  API/schema fields, docs, and user-facing labels?
- Does the PR introduce near-synonyms for an existing concept that could confuse future
  readers?
- Do test names describe behavior in the same vocabulary as production names?

Flag naming when it can mislead maintainers about intent, scope, side effects, or
invariants — not just when it violates casing style.
