# OQ Skills

Personal agent skills for Jira context gathering, pull request review, and manual QA.

## Included skills

| Skill | Purpose |
| --- | --- |
| `oq-jira-context` | Load read-only Jira issue, parent, sibling, linked issue, sprint, and board context. |
| `oq-review-pr` | Review one GitHub pull request deeply, with emphasis on invariants and reachable write paths. |
| `oq-qa-tester` | Derive browser test scenarios from a PR and Jira ticket, drive a running CMS4 shop, and publish an evidence-backed QA report. |

`oq-qa-tester` uses `oq-jira-context`, so all three skills are distributed together.

## Claude Code

Add this repository as a marketplace, then install the plugin:

```text
/plugin marketplace add SpareParts/oq-skills
/plugin install oq-skills@spareparts-skills
```

Restart Claude Code or run `/reload-plugins` when prompted. Installed skills are namespaced by the plugin:

```text
/oq-skills:oq-jira-context
/oq-skills:oq-review-pr
/oq-skills:oq-qa-tester
```

## OpenCode

Clone the repository and add its `skills` directory to your global OpenCode configuration:

```bash
git clone https://github.com/SpareParts/oq-skills.git ~/.config/opencode/oq-skills
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": {
    "paths": ["~/.config/opencode/oq-skills/skills"]
  }
}
```

Merge the `skills.paths` entry into `~/.config/opencode/opencode.json` or `opencode.jsonc` if that file already exists, then restart OpenCode. Load the skills by their unscoped names, such as `oq-review-pr`.

## Requirements

- `oq-jira-context` needs either Atlassian MCP access or the read-only `acli` Jira CLI. Project-wide Jira searches also expect Jira defaults in `AGENTS.local.md` under `## pm-jira-analyze`.
- `oq-review-pr` needs an authenticated GitHub CLI (`gh`).
- `oq-qa-tester` is specific to a running CMS4 development environment and Claude-in-Chrome. Its full prerequisites are declared in the skill metadata.

The skills are read-only toward Jira and GitHub unless the user explicitly requests a write action.
