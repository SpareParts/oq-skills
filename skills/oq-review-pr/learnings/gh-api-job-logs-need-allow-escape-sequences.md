---
status: active
dimension: general
date: 2026-11-09
---

# `gh api` on an Actions job-logs URL needs `--allow-escape-sequences`, or the "log" is a one-line refusal

Why: `gh api repos/<owner>/<repo>/actions/jobs/<id>/logs` returns the raw log with ANSI terminal
escape sequences; gh refuses to print them and emits only "the response contains terminal escape
sequences; pass --allow-escape-sequences to output it anyway" — so a grep over the piped output
finds nothing and the CI failure looks unverifiable. Pass the flag and strip the codes
(`sed 's/\x1b\[[0-9;]*m//g'`) before grepping.
Evidence: MIN-188 review of SpareParts/oq-skills#39 — verifying cms4#47750's run 42543075670
(job 128922133655) needed the flag + strip before the `cast.int` line at the Cest's line 21
grepped clean.
