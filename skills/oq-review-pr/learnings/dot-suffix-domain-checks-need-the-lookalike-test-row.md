---
status: active
dimension: testing
date: 2026-10-09
---

# When rewriting or testing a '.'-prefixed domain-suffix check, add the look-alike row (badexample.com under example.com) to the DIRECT test — sibling end-to-end pins don't catch a dotless "simplification"

Why: `'.' . $parent` suffix logic answers `badexample.com` → false where naive `str_ends_with($value, $parent->value)` answers true, yet all three natural contract cases (subdomain→true, unrelated→false, equal→false) pass under BOTH implementations — so a direct test without the near-miss row would stay green through a regression that inverts it. The pin often exists only indirectly (DnsPresetMatcherTest's look-alike zone row, ZoneRecordNameTest's evilexample.com), which catches it end-to-end but leaves the unit test unable to localize. One extra assertion in the direct test makes the arithmetic locally un-simplifiable.
Evidence: shoptet/cms4#46019 review (2026-10-09, task MIN-45); tests/unit/cms/packages/Multishop/Domain/Dns/Model/Domain/NormalizedDomainTest.php:76-131; cms/packages/Multishop/Domain/Dns/Service/DnsPresetMatcher.php:179.
