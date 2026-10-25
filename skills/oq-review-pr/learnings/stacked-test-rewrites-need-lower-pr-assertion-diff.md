---
status: active
dimension: testing
date: 2026-10-25
---

# When an upper stacked PR wholesale-rewrites a test file the lower PR just extended, diff the lower PR's new assertions across the rewrite

Why: the upper PR's diff against master shows the rewrite as one blob, so nothing in it says whether the lower PR's new tests kept their assertions; a rewrite that softened one assertion (e.g. dropped a "good row still filtered out" negative control) stays green. Mechanical check: list the test names the lower PR added, then read each at the upper head and compare assertion-by-assertion — a same-named test with different fixture wiring can silently shed the guarantee. This extends `reshaped-tests-can-unpin-previous-contracts.md` from maintainer reshapes to agent-authored stacks, where the upper PR is a fresh rewrite rather than a reshape of the same diff.
Evidence: shoptet/cms4#46951 → #46952 review (task MIN-121, 2026-10-25) — `DomainRedirectionsServiceTest.php` rewritten wholesale in #46952; the four lower-PR tests (`testRendersUnparsableSourceHostWithoutDnsDiagnostics`, `testKeepsNullChannelRedirectionWithUnparsableSourceHostInTheList`, `testRendersDiagnosticsForParsableRedirectionNextToUnparsableOne`, `testLogsWarningWhenSourceHostCannotBeParsed`) verified intact at head `1512d75464`.
