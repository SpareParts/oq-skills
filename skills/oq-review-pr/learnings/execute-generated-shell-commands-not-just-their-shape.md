---
status: active
dimension: general
date: 2026-11-11
---

# A diff that changes generated shell must be verified by executing the command, not just its shape

Why: unit tests over a command *generator* assert the generated string's shape (substrings,
exact text), and shape pins text, not behaviour — a set -e bootstrap that aborts on the health
check, a recovery branch that never fires, or quoting that breaks only under a real shell all
pass shape assertions. The behavioural check is cheap: import the generator from the reviewed
branch, render the command for a tiny fixture, and execute it under `bash -e` against local
fixtures (healthy → short-circuits; damaged → recovers; failing → aborts with the right exit
code). Minutes of work, no repository writes; do it in /tmp. When the review cannot execute
(execution needs credentials or minutes-scale setup), say so and fall back to shape — but name
the gap rather than treating shape as proof.

Evidence: shoptet/multishop-software-factory#156 (task MIN-198 review round, 2026-11-11) — the
cloneCommand health-check change; four shape tests pinned the string while direct execution of
the rendered command under `set -e` against fixtures verified the six behaviours that mattered
(fail-closed detection, recovery, healthy short-circuit, untracked-leftover tolerance, and the
set -e exemption for the check vs fatality of the re-clone).
