---
status: active
dimension: general
date: 2026-11-07
---

# cms4's lib-common libraries are analysed by their own phpstan configurations (e.g. `libraries/lib-common/phpstan-ci.neon`, run by `.github/workflows/test-lib-common.yaml`), never by the main repo's phpstan/phpstan-l10 — do not run or require the main config against lib-common files

Why: `libraries/lib-common` carries its own `phpstan.neon` (with `forbidStaticMethodRule: false`) and the CI workflow includes `libraries/lib-common/phpstan-ci.neon`, so lib-common code is gated in a context where the main repo's rules are not loaded at all. Pointing the main `phpstan-l10.neon` at a lib-common file makes rules such as `shoptet.forbidStaticMethod` fire on code CI never applies them to, and the resulting "phpstan-l10 fails on this lib-common change" claim is an artifact of the wrong config, not a defect the author must fix: the same change gates cleanly under `Lib-Common Checks`. When a PR touches `libraries/lib-common`, verify with lib-common's own config (or rely on the Lib-Common Checks workflow) and say which config you ran; do not ask the author to satisfy a main-repo rule that never runs there.
Evidence: task MIN-177 (CZ3INF1-486, shoptet/cms4#47676, 2026-11-06) — the requester corrected the agent's verification: "lib-common libraries do not use phpstan-l10 from main phpstan. Lib-common have their own phpstan configurations." The agent then confirmed `libraries/lib-common/phpstan-ci.neon` (including its own `phpstan.neon` with `forbidStaticMethodRule: false`) is what the Lib-Common Checks workflow runs, and that the change passes it with `[OK] No errors`. Distinct from the merged `tmp-phpstan-extraction-must-preserve-cms4-tests-path.md` (a path-segment exemption inside one config) — this is about which config owns the file.
