---
status: active
dimension: general
date: 2026-10-12
---

# In codeception suite YAML, unquoted header values become ints on the wire (psr7 deprecates per request) and CURLOPT_* in `curl:` deprecates per request in guzzle ≥7.11 — quote header values, use native keys

Why: YAML parses `Disable-Tracy-Panel: 1` as int; PhpBrowser passes default headers into every `GuzzleHttp\Psr7\Request`, which (psr7 ≥2.11) fires a deprecation per request for non-string header values — 3017 requests = 3017 notices. The receiving side compares `=== '1'`, so quoting the value is behavior-identical. Likewise `curl: {CURLOPT_TIMEOUT: 300}` maps into the Guzzle client's `curl` option, which guzzle ≥7.11 deprecates per request; the native PhpBrowser key `timeout` (in `guzzleConfigFields`, applied via `array_intersect_key` as a client default) is the replacement and preserves the value. Removing a `curl:` block entirely is safe (`'curl' => []` is the module default). When a CI log shows per-request deprecation multiplication, check the suite YAML's scalar types and curl block first.
Evidence: shoptet/cms4#46126 (MIN-57, 2026-10-12) — tests/functional.suite.dist.yml:34-36 (fix), vendor/codeception/module-phpbrowser/src/Codeception/Module/PhpBrowser.php:90,104-115,225, cms/packages/Debugging/Helper/DebuggerConfigurator.php:208; baseline CI run 38225375871/job 114731529697.
