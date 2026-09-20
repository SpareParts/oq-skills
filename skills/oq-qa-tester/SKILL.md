---
name: oq-qa-tester
description: "Manually QA-test one GitHub PR end-to-end: loads the linked Jira ticket, derives test scenarios, closes information gaps from code and recorded learnings (asks the human only as last resort), drives the running dev shop in Chrome, and publishes a result artifact with per-scenario verdicts and screenshots. Use when asked to QA, manually test, or click-test a PR."
argument-hint: "[PR URL or number] [optional project ID or shop URL — defaults to 10000 (fenix)]"
user-invocable: true
disable-model-invocation: true
compatibility: "requires the already-running CMS4 docker dev stack (*.test domains), a seeded dev shop, and the Claude-in-Chrome browser extension"
---

# PR QA Tester

QA one PR from the user's chair: what the ticket promises is the contract, what the
browser shows is the evidence. Deliverable: a published result artifact with a verdict,
per-scenario results, and screenshots — plus a short session summary. Never fix product
code; report findings only.

## CRITICAL

- **Claude-in-Chrome only** — never Playwright, headless browsers, or ad-hoc harnesses.
- **Reuse the running stack.** Docker on `*.test` is up. Don't start, restart, or
  rebuild services beyond what a step names. Shop not responding → stop and tell the
  user; a login screen is not a blocker — log in yourself (Step 5).
- **Credentials only on `.test` hosts.** The dev password may be typed only when the
  page host ends in `.test`. Any other host → stop and ask the user.
- **Information-gap order is fixed:** code → learnings → local DB → human. Ask the
  human once, in one batch, and only for what the first three cannot answer.
- **Mutate freely to verify** (submit, toggle, delete, seed a row, activate a module) —
  but never `make setup-project` (global reset). Keep a mutation ledger and restore the
  pre-test value when cheap (one write). An empty DB table is never "nothing to test" —
  seed a couple of identifiable marker rows, then delete exactly those.
- **Native dialogs block CDP.** A tool timeout right after a click means a pending
  `confirm()`, not a crash — don't retry: screenshot the wording, click Cancel/OK,
  continue.
- **Silence is not success** — every scenario you could not exercise is reported
  NOT-RUN with the reason.

## Step 0 — Load learnings

Read every file in this skill's `learnings/` directory before anything else. They
encode environment quirks and per-domain scenario patterns from past runs; apply them
without re-deriving.

## Step 1 — Load the PR

1. Parse `$ARGUMENTS` for the PR. Load it read-only:

   ```bash
   gh pr view {N} --json number,title,body,headRefName,headRefOid,baseRefName,isDraft,labels,url,files
   gh pr diff {N}
   ```

2. Classify the change (feature / bugfix / refactor / config) and list the user-facing
   surfaces it touches: admin pages (Smarty or React), storefront, API, emails, cron.
   A PR with no user-facing surface → say so and stop; this skill has nothing to drive.
3. Preflight the dev stack:
   `./docker/dev compose ps --status running --format '{{.Service}}'` — the core
   services (www, database, console, proxy) must be listed. Anything down → stop and
   ask; starting the stack is the user's call (see CRITICAL).
4. The PR must be running locally. Compare `git rev-parse HEAD` with `headRefOid`; if
   they differ, ask before `gh pr checkout {N}` (dirty tree →
   `git stash push -m "oq-qa-tester"`, tell the user, pop after restoring the starting
   ref at the end). Record the starting ref.
5. Rebuild only what the diff (plus the checkout delta, when you switched branches)
   demands:
   - `admin/react/**` → `make fe-build-admin`;
   - storefront JS/CSS → `make fe-build-core`;
   - `composer.lock` → `make composer-install`;
   - `*.neon` / DI config → clear the container DI cache (it does NOT rebuild on NEON
     changes):

     ```bash
     ./docker/dev ai console sh -c 'rm -rf /var/tmp/release/cms4-*/cache/nette.configurator'
     ```

   - `migrations/**` → list the files and ask before applying (`/st-apply-migration`).
     Migrations mutate the local DB and don't auto-revert on branch switch — say so
     when asking.

## Step 2 — Load the Jira ticket

1. Derive the Jira key from `headRefName` or the PR title (`[A-Z][A-Z0-9]+-\d+`).
2. Load the `oq-jira-context` skill with the key. From its brief, extract: product intent,
   acceptance criteria, explicit non-goals, and decisions from comments.
3. No key or no ticket access → note it in the report and derive scenarios from the PR
   description and diff alone.

## Step 3 — Design test scenarios

Build the scenario table before touching the browser. Sources in priority order:
acceptance criteria, the diff, learnings. Coverage rules:

- one happy-path scenario per acceptance criterion;
- validation and error paths for every new/changed input or write action;
- both data states (empty, populated) for lists and detail views;
- module gates and permission boundaries when the touched code checks them;
- a regression scenario around adjacent behavior when the diff touches shared code;
- the storefront side when the change is visible there, not just admin.

Each scenario: `ID (S1…) · Goal · Preconditions · Steps · Expected · Source (AC-n /
diff / learning / human)`. Keep scenarios small — one assertion focus each; a scenario
whose steps exceed ~8 actions should be split.

## Step 4 — Close information gaps

For every scenario field you cannot fill, resolve in this order and stop at the first
source that answers:

1. **Code** — routes and controllers, module/permission gates, feature flags,
   validation rules, translations, seed data expectations.
2. **Learnings** — re-check Step 0 notes for the affected domain.
3. **Local DB** — read-only lookups for real data to test with:

   ```bash
   ./docker/dev ai console sh -c 'echo "SELECT …" | st-mysql st_<projectId>'
   ```

4. **Human** — one batched `AskUserQuestion` covering everything left (expected
   business behavior the ticket doesn't state, unusual data/shop needs). Never ask
   what the code already answers.

Print the final scenario table in the session before driving, then proceed — do not
wait for approval unless open questions block a scenario.

## Step 5 — Prepare the shop

1. Shop base URL from the second argument: a URL → as given; `10000` or absent →
   `https://fenix.myshoptet.com.test`; other project ID →
   `https://<subdomain>.myshoptet.com.test`:

   ```bash
   ./docker/dev ai console sh -c 'echo "SELECT subdomain FROM projects WHERE id = <projectId>" | st-mysql st_cms'
   ```

2. Open the relevant admin page. Logged-in admin → proceed; login screen → log in
   (host must end in `.test`). Anonymization sets the password `admintestpw` for every
   `*@shoptet.cz` admin user. Try `info@shoptet.cz` / `admintestpw` first; if that user
   doesn't exist, look up the shop's owner and retry with the same password:

   ```bash
   ./docker/dev ai console sh -c 'echo "SELECT email FROM admin_users WHERE email LIKE \"%@shoptet.cz\" AND authorized = 1 AND twoFactorAuthSecret IS NULL ORDER BY role = \"owner\" DESC, id ASC LIMIT 1" | st-mysql st_<projectId>'
   ```

   Both attempts fail → stop and report which emails you tried and how each failed.
3. Fix the Chrome window at 1440×1080 and keep it for the whole run. Dismiss the Tracy
   bar when present (`document.querySelector('a[data-tracy-action="close"]')?.click()`).

## Step 6 — Execute scenarios

Drive scenarios in table order. Per scenario:

1. Establish preconditions (seed marker rows, activate modules) and log each mutation
   in the ledger.
2. Execute the steps; screenshot every assertion point and the final state.
3. Record observed vs expected → **PASS** / **FAIL** / **BLOCKED** (env) / **NOT-RUN**
   (+ reason). A write action passes only when the write is executed and its effect
   observed (reloaded page, notifier, DB row) — a form that merely renders is not a
   pass.
4. On FAIL: reproduce once to confirm when cheap; capture the failure evidence —
   screenshot plus `read_network_requests` / `read_console_messages` output for the
   failing action.

Never leave a scenario half-driven without marking it NOT-RUN.

## Step 7 — Result artifact

1. Recover screenshots — the `computer` tool's `save_to_disk` flag is a silent no-op
   (anthropics/claude-code#40141); every capture is persisted in the session
   transcript:

   ```bash
    scripts/extract_screenshots.py list
    scripts/extract_screenshots.py extract <idx…> --out <scratchpad>/shots
   ```

2. Build the report as an HTML file in the scratchpad. In Claude Code, load the
   `artifact-design` skill first, then publish with the Artifact tool (title:
   `<JIRA-KEY> QA Run`; keep the favicon stable across redeploys). In other harnesses,
   leave the HTML file and print its path. Embed screenshots as JPEG data URIs; the
   rendered page must stay under 16 MB — downscale with `sips -Z 1200` when needed.
3. Report structure:
   - header: PR link/title, Jira key, branch + head sha, shop URL, date;
   - verdict: **PASS** | **FAIL** (n failed) | **INCOMPLETE** (n NOT-RUN) |
     **BLOCKED** (env) — PASS requires every scenario driven; any NOT-RUN caps the
     verdict at INCOMPLETE; FAIL beats INCOMPLETE when both apply;
   - scenario summary table (ID, goal, status);
   - one section per scenario: steps, expected, observed, screenshots, failure
     evidence;
   - mutation ledger (what changed, what was restored);
   - information gaps: what was asked of the human, what stayed open.
4. Session summary: verdict, pass/fail/not-run counts, findings in one line each,
   artifact link. Post nothing to the PR or Jira unless the user explicitly asks.

## Step 8 — Harvest learnings

After the report, write new generalizable learnings to
this skill's `learnings/` directory — one file per learning,
`<kebab-slug>.md` with a `**Trigger:**` line (when it applies) and a `**Rule:**` line
(what to do). Capture environment quirks, login/selector/timing traps, and per-domain
scenario patterns — not run-specific facts. Dedupe against existing files; update or
delete a learning a run proves wrong.

## Constraints

- Exactly one PR per run.
- Read-only toward GitHub and Jira: never comment, review, approve, edit, or
  transition anything unless the user explicitly asks.
- Never modify product code; a bug is a finding, not a fix.
- Always restore the starting ref, pop the stash if you made one, and leave the
  working tree as you found it.
- Findings name the scenario, the observed behavior, and the evidence — not guesses
  about the cause; code-level diagnosis is a follow-up, not part of the verdict.

## Additional resources

- `scripts/extract_screenshots.py` — recover
  captured screenshots from the session transcript (Step 7)
- `oq-jira-context` — Jira intake used in Step 2
- `learnings/` — this skill's accumulated QA learnings (Steps 0 and 8)
