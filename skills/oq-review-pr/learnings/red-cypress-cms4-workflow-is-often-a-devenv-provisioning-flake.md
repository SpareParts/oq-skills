---
status: active
dimension: general
date: 2026-10-02
---

# A red "Cypress Cms4" workflow is often a devenv-provisioning flake — read the archived failure log and name the failed step before treating it as a code failure

Why: two heads of a backend-only PR went red in "Cypress Cms4"; in both archived failure logs the run died at the "Setup project … on devenv" step before any spec executed — infrastructure provisioning, not code — and Cypress was green on the substantive first head. Red Cypress alone must not block a report or trigger a code fix: name the failing step and ask for a rerun instead. The signature of the flake is the failing step name (a setup/provisioning step, before any spec runs), not the workflow's red color.
Evidence: task MIN-20, PR shoptet/cms4#45569 — heads 942c07b4a6 and bbf9e4dd91 both died at the devenv setup step (verified in the archived failure logs); first head 7ec6486c38 fully green.
