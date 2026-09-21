# oq-review-pr learnings

One file per learning, `<kebab-slug>.md`, slug states the rule not the PR it came from:

```markdown
---
status: active | retired
dimension: architecture | domain-integrity | code-quality | naming | testing | security | readability | general
date: YYYY-MM-DD
---

# One-line rule as the H1

Why: the mechanism — what breaks, what it looked like, how to catch it.
Evidence: PR # / file paths.
```

`dimension: general` applies to every subagent (report-format quirks, recurring
false-positive patterns, `gh` gotchas). Any other value scopes the learning to that one
dimension's subagent prompt.

## Lifecycle

- Never delete a rule — mark it `status: retired` with a one-line note why, in the body.
- Add one file per generalizable gotcha a run turns up: a false positive the team pushed
  back on, a repo convention that looks like a violation but isn't, a `gh`/environment
  trap. Not PR-specific facts — those belong in the PR report, not here.
- Dedupe against existing files before writing a new one.

## Reading

All active learnings:

```bash
grep -L "status: retired" skills/oq-review-pr/learnings/*.md | grep -v README | xargs cat
```

Written by the orchestrator's harvest step; read in full before dispatching subagents,
then split by `dimension:` when building each subagent's prompt.
