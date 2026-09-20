---
name: oq-jira-context
description: "Use when reading Jira context before analysis or implementation: issue details, comments, parent/Epic, siblings, linked issues, current sprint, or board state. Read-only; do NOT use for creating or editing Jira work items."
user-invocable: true
disable-model-invocation: false
argument-hint: "[Jira key like CZ3MUL1-123 | Jira URL | board/sprint context request]"
---

# Jira Context Intake

Load and summarize Jira context before planning, analysis, or implementation. This skill is read-only: it gathers facts from Jira and reports what is known, what is implied, and what still needs clarification.

- `$ARGUMENTS` — a Jira key, Jira URL, sprint/board request, JQL fragment, or short description of the Jira context to load.

## Step 1 — Read local Jira defaults

At the start of every invocation, read `./AGENTS.local.md` and find the `## pm-jira-analyze` section. Reuse its settings as the shared Jira defaults for this skill.

Recognized keys:

- `default-project` — primary Jira project key, for example `CZ3MUL1`.
- `default-parent` — optional Epic/parent key when a context request omits one.
- `required-labels` — labels that may help with related-ticket search.
- `default-issue-type` and `default-assignee` — informational only; do not use them to create or edit anything.

If `default-project` is missing, infer the project from the Jira key in `$ARGUMENTS`. If neither exists, ask one precise question for the project key before running project-wide or sprint-wide searches.

## Step 2 — Identify the requested context shape

Classify `$ARGUMENTS` into one of these modes:

1. **Issue context** — a Jira key or URL is present.
2. **Parent/Epic context** — the user asks for children, siblings, Epic, parent, initiative, or a parent key.
3. **Sprint/board context** — the user asks for current sprint, board, active work, sprint scope, or sprint risks.
4. **Search context** — the user provides keywords, labels, components, teams, or a JQL-like request.

When multiple modes apply, run them in this order: issue → parent/Epic → linked issues → siblings → sprint/board → broad search.

## Step 3 — Resolve Jira access path

Prefer Atlassian MCP tools when available because they return structured data without shell parsing. Use `ToolSearch` or the environment's MCP discovery mechanism to find read-only Jira tools before calling them.

Useful Atlassian MCP tools:

- `getAccessibleAtlassianResources` — resolve cloud id and Jira site.
- `getVisibleJiraProjects` — list visible projects if the project key is unknown.
- `getJiraIssue` — read an issue by key. Request markdown for human-readable descriptions/comments when supported.

If MCP tools are unavailable, use the read-only `acli` commands below. Always request JSON when the result will be parsed.

```bash
acli jira workitem view <KEY> --json
acli jira workitem search --jql "<JQL>" --limit <N>
acli jira project view --key <PROJECT> --json
acli jira project list
```

Do not use create, edit, transition, delete, or status-changing Jira tools in this skill.

## Step 4 — Load issue-level context

For each primary Jira issue key:

1. Fetch the issue with description, status, type, priority, labels, assignee, reporter, parent, links, comments, created/updated dates, fix versions, sprint field, component field, and relevant custom fields when available.
2. Summarize the description in plain language. Preserve product intent, acceptance criteria, constraints, and explicit non-goals.
3. Summarize comments chronologically by decision or new information, not by every message. Include author/date only when it matters for accountability or recency.
4. Extract links to Jira, GitHub, Confluence, Slack, Figma, documents, or PRs. Load linked resources only when they are directly relevant and available through safe read-only tools.

Important fields to inspect in JSON responses when present:

- `key`, `summary`, `description`, `status`, `issuetype`, `priority`
- `labels`, `components`, `fixVersions`, `assignee`, `reporter`
- `parent`, `issuelinks` or `issueLinks`, `subtasks`
- `comment.comments`
- `created`, `updated`, `resolution`, `sprint`

## Step 5 — Load parent, siblings, and linked issues

If the issue has a parent/Epic, fetch it and summarize:

- parent goal and business context,
- parent status and timeline clues,
- how the requested issue fits the parent,
- conflicts between parent scope and child scope.

Then search for siblings under the same parent:

```bash
acli jira workitem search --jql "parent = <PARENT-KEY> ORDER BY rank ASC" --limit 100
```

For linked issues, inspect the issue's link fields first. Fetch linked issues when their relationship affects interpretation, sequencing, blockers, duplicates, or dependencies.

Optional JQL fallback, if supported by the Jira instance:

```bash
acli jira workitem search --jql "issueFunction in linkedIssuesOf('<KEY>')" --limit 50
```

If `issueFunction` is unavailable, do not fail the workflow. Use links returned on the issue itself and state that reverse-link search was unavailable.

## Step 6 — Load current sprint and board context

When the user asks about current sprint, board, active work, or sprint planning, use the configured `default-project` unless the user provided another project.

Start with project-scoped open sprint work:

```bash
acli jira workitem search --jql "project = <PROJECT> AND sprint in openSprints() ORDER BY rank ASC" --limit 100
```

If the user asks for a board specifically and board APIs are available, list boards for the project and inspect the active sprint for the relevant board. If board APIs are not available, say so and use the JQL `openSprints()` fallback.

Useful sprint summary dimensions:

- issues by status,
- blockers and blocked issues,
- unassigned or stale issues,
- work grouped by parent/Epic,
- tickets without clear acceptance criteria,
- recently updated issues,
- risks or scope mismatches visible from issue summaries/comments.

## Step 7 — Search related context when needed

Use targeted JQL searches instead of broad browsing. Base searches on concrete terms from the issue summary, parent, labels, components, or comments.

Examples:

```bash
acli jira workitem search --jql "project = <PROJECT> AND text ~ '<term>' ORDER BY updated DESC" --limit 20
acli jira workitem search --jql "project = <PROJECT> AND labels = '<label>' ORDER BY updated DESC" --limit 30
acli jira workitem search --jql "project = <PROJECT> AND comment ~ '<term>' ORDER BY updated DESC" --limit 20
acli jira workitem search --jql "assignee = currentUser() AND resolution = Unresolved ORDER BY updated DESC" --limit 50
```

Keep related searches narrow. Do not read dozens of unrelated issues just because they match a generic word.

## Step 8 — Produce the context brief

Return a structured, concise brief with these sections when relevant:

1. **Source** — issue key/URL, project, parent/Epic, sprint/board source.
2. **Ticket summary** — what the ticket asks for and why.
3. **Current state** — status, assignee, labels, sprint, blockers, recency.
4. **Parent/Epic context** — parent goal and sibling landscape.
5. **Sibling and linked issues** — dependencies, duplicates, blockers, related work.
6. **Comment decisions** — decisions, clarifications, disagreements, or unanswered questions from comments.
7. **Sprint/board view** — current sprint scope and visible delivery risks.
8. **Engineering implications** — likely impacted area, constraints, hidden risks, and what to verify in code.
9. **Open questions** — only questions that remain after loading available context.

Be explicit about confidence. Separate facts read from Jira from inferences made from those facts.

## Constraints

- Read-only only: never create, edit, transition, assign, label, comment on, or delete Jira work items.
- Do not run `acli jira workitem create`, `acli jira workitem edit`, `transitionJiraIssue`, `editJiraIssue`, or any write-capable operation.
- Do not expose private personal data beyond what is necessary to understand ownership or decisions. Prefer display names over emails.
- Do not fabricate parent, sprint, board, or relationship data. If a field is missing or inaccessible, say that it was not available.
- Do not assume `issueFunction` JQL extensions exist. Treat them as optional and fall back gracefully.
- Do not use `default-project` from any source other than `AGENTS.local.md` `## pm-jira-analyze`, unless the Jira key or user explicitly overrides it.
- Keep the final brief actionable; avoid dumping raw JSON unless the user asks for it.
