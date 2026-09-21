---
name: oq-review-pr
description: "Review a single GitHub PR deeply. Use when the user asks to review, analyze, or quality-check a PR link/number. Fans the review out to one subagent per dimension (architecture, domain integrity, code quality, naming, testing, security, readability), synthesizes their findings into a senior review report, and harvests generalizable learnings for next time."
argument-hint: "[GitHub PR URL or repo + PR number]"
user-invocable: true
---

# GitHub PR Analyst

Analyze one GitHub pull request as an experienced senior engineer and produce a
thoughtful, opinionated quality report. You are the orchestrator: you load the PR once,
dispatch one focused subagent per review dimension, then synthesize their findings —
you do not re-derive their checklists yourself.

- `$ARGUMENTS` — PR URL, PR number, repository, or accompanying PR metadata/message.

## Communication style

- Lead with a compact 2-line header: PR title + stats.
- Follow with your verdict in at most 2 sentences.
- Put detailed analysis after the verdict.
- Use emoji sparingly: ⚠️ for warnings, 🔴 for critical issues, ✅ for positive signals.
- Be concise and actionable; if there is nothing meaningful to flag, say so and stop.

## Step 0 — Load learnings

Read every file in this skill's `learnings/` directory before anything else (skip
`status: retired` ones). They encode false-positive patterns, repo conventions that
look like violations but aren't, and environment/`gh` quirks from past runs — apply
them without re-deriving. Group them by their `dimension:` field; you'll hand each
group to the matching subagent in Step 3.

## Step 1 — Load PR context

Use read-only GitHub CLI commands to load exactly one PR:

```bash
gh pr view {N} --repo {repo} --json number,title,body,author,additions,deletions,changedFiles,reviewDecision,reviewRequests,latestReviews,isDraft,labels,headRefOid,url
gh pr diff {N} --repo {repo} --name-only
```

This is enough for the header and to classify the change — the deep read of the actual
diff happens once per dimension, inside each subagent, in Step 3.

## Step 2 — Understand intent before judging

- Read the PR title and description.
- Identify whether this is a feature, bugfix, refactor, config change, dependency
  update, or test-only change.
- Summarize what behavior the PR claims to change.
- Note this intent in one or two sentences — you'll compare it against the diff
  yourself when forming the verdict in Step 5; subagents don't need it.
- A PR with no reviewable diff (pure metadata, already merged, empty) → say so and stop.

## Step 3 — Dispatch one subagent per dimension

Seven dimensions live as standalone files in this skill's `prompts/` directory, each
scoped to exactly one concern so a subagent can go deep without the others' noise:

| File | Dimension |
| --- | --- |
| `architecture-design.md` | Architecture & design |
| `domain-integrity.md` | Domain integrity and invariant closure |
| `code-quality.md` | Code quality |
| `naming-consistency.md` | Naming consistency and intent |
| `testing.md` | Testing |
| `security-safety.md` | Security & safety (also owns the high-attention-files check) |
| `readability-maintainability.md` | Readability & maintainability |

For each one, build its subagent prompt by taking `prompts/_shared.md`, substituting
`<REPO>` / `<PR_NUMBER>` / `<LEARNINGS_BLOCK>` (the learnings from Step 0 tagged for
that dimension, plus every `dimension: general` one; empty is fine), and appending the
dimension file's content.

Dispatch all seven in a single batch so they run in parallel:

- **Claude Code**: the Agent tool, `subagent_type: "general-purpose"`, one call per
  dimension, all seven Agent calls in the same message.
- **Other harnesses**: whatever the host's equivalent sub-task/subagent mechanism is;
  if none exists, run the seven prompts sequentially yourself instead of skipping them.

Each subagent independently runs its own `gh pr view` / `gh pr diff` (per
`prompts/_shared.md`) — do not paste the diff into their prompts yourself; it's
wasteful and every subagent needs the full diff anyway, not a pre-filtered slice.

## Step 4 — Evaluate high-attention files

The security-safety subagent owns this check (its prompt file says so explicitly), but
sanity-check its answer yourself against the paths below before trusting a "no
concerns" for a PR that clearly touches one of them:

- `**/migrations/**` — database migrations and deploy-order compatibility.
- `.github/**` — CI/CD configuration.
- `Dockerfile*`, `docker-compose*`, `docker/**` — container and local environment behavior.
- `.env*`, `**/config/**` — runtime configuration.
- `composer.json`, `composer.lock`, `package.json`, lockfiles — dependency changes.
- Authentication, authorization, payment, checkout, order, customer, multishop, and cross-tenant code paths.

## Step 5 — Synthesize and form a real review opinion

Collect all seven subagent replies. Answer these before writing the report:

- Does the PR do what it claims (compare against your Step 2 intent note)?
- Does it make the codebase better or worse?
- Is there a simpler or safer approach?
- Are there subtle bugs, logic errors, naming traps, or missing tests the subagents
  surfaced?
- Would you approve this in a real review?

For every business-rule or state-changing PR, the domain-integrity subagent's ledger
is your primary evidence — do not issue a `Clean PR` or approving verdict while it
contains an unknown write boundary or an unchecked production caller; send it back (or
investigate the gap yourself) before deciding.

Scale depth to PR complexity. A trivial dependency bump may need only a header and
one-line verdict even though all seven subagents ran. A multi-file feature needs a
deeper report.

If two subagents disagree about the same file/line (e.g. naming calls something a
"resolver" that domain-integrity says is really a policy decision), don't silently pick
one — surface both readings in the finding, they're usually pointing at the same real
issue from different angles.

## Report format

Use this structure, omitting empty sections:

```markdown
<PR title> — <changed files/additions/deletions>
<short scope summary>

Verdict: <1–2 sentences>

### Findings
- 🔴 <critical issue with concrete file/path and why it matters>
- ⚠️ <actionable concern with concrete evidence>

### Positive signals
- ✅ <specific good pattern, coverage, or safety property>

### Notes
- <low-severity observation or product/semantics question>
```

Do not force findings. If there are no real concerns, say `Clean PR, no concerns.`

## Step 6 — Harvest learnings

After the report, write new generalizable learnings to this skill's `learnings/`
directory — one file per learning, `<kebab-slug>.md`, format and lifecycle rules in
`learnings/README.md`. Write one when this run:

- overturned a subagent finding as a false positive once you checked the surrounding
  code (record the pattern that looks like a violation but isn't, tagged to that
  dimension);
- hit a `gh`/environment quirk worth remembering (`dimension: general`);
- surfaced a repo convention a subagent couldn't have known without this PR (naming,
  layering, invariant boundary) that will recur on future PRs in the same area.

Dedupe against existing files; update or retire (never silently delete) a learning this
run proves wrong.

## Constraints

- Analyze exactly one PR per run.
- The orchestrator reads PR metadata directly (Step 1); the actual diff is read once
  per dimension, inside each subagent — never skip a subagent's own `gh pr diff` call
  to save time.
- For business-rule or state-changing PRs, the domain-integrity subagent's ledger must
  be complete before a clean or approving verdict.
- Never treat controller/orchestrator validation as domain closure without checking the
  shared write boundary and alternate writers.
- Keep the work read-only unless the user explicitly asks you to post comments or
  modify something.
- Never run `gh pr review`, `gh pr comment` (unless the user explicitly asks for a
  PR-level comment), `gh pr merge`, `gh pr close`, or `gh pr edit`.
- Never approve, request changes, merge, close, or edit PR metadata.
- Never scan repositories for multiple PRs.
- Never modify source files as part of the review.
- Do not pad the report with filler.

## Additional resources

- `prompts/_shared.md` — preamble prepended to every dimension subagent's prompt
  (Step 3)
- `prompts/*.md` — the seven standalone dimension prompts
- `learnings/` — this skill's accumulated review learnings (Steps 0 and 6)
