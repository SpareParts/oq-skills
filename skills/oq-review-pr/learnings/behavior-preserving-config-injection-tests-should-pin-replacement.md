---
status: active
dimension: testing
date: 2026-10-11
---

# A config-following test must pin replacement, not inclusion

Why: when a PR moves hardcoded values behind an injected config, the natural test — a non-default value is honored — passes even if the code UNIONs the old hardcoded list with the injected one, because the non-default value is included either way. The decommission/drift semantics the PR exists for then stay unproven. Add the companion assertion: under the non-default config, a value from the OLD list must now fail the check; otherwise a future regression back to union-semantics keeps the suite green. Look for the negative control, not just the positive one.
Evidence: shoptet/cms4#46102 (MIN-51, review 2026-10-11) — `testCloudIpsComeFromInjectedPresetConfig` asserted only that aRecordIps `['203.0.113.10']` classifies `direct_records_ok`; no test asserted `185.184.254.10` classifies `not_pointing` under that config. The implementer's follow-up commit added the replacement assertion with a proven negative control.
