---
status: active
dimension: domain-integrity
date: 2026-10-19
---

# Moving a private method into a command handler turns its implicit caller-side preconditions into callable-by-anyone properties — pin them with a dispatch-inside-transaction assertion and keep the one-line invariant comment

Why: a private method inherited its preconditions from its only caller (the caller's transaction, the caller's module state). A command handler is dispatchable from anywhere, so those preconditions stop being facts about the code and become conventions nobody enforces. The evidence PR moved a resolver's method into a command + handler and dropped the master docblock's blocked-row-reuse / hidden-already-copied invariants — exactly the "one line for something the code cannot say" kind the sparse-comments rule allows. Keep that line, and pin the coupling behaviourally: the resolver test's `$transactionActive` assertion (dispatch happens inside a transaction) is the surviving pin; the handler's re-copy condition is the line a simplifier would break.
Evidence: shoptet/cms4#46450 (task MIN-76, 2026-10-19, artifact b5b65dcd).
