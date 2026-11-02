---
status: active
dimension: architecture
date: 2026-11-02
---

# A bus-dispatch→Domain-port swap's "no NEON change needed" claim is proven by exactly one implementer plus a factory that passes only its explicit arguments — grep `implements` before repeating it

Why: when a consumer swaps a bus dispatch for a Domain port, autowiring resolves the port by type, so the claim "no DI registration change is needed" holds only while exactly one implementer exists and the consumer's DI factory passes only its explicit arguments (nothing that would make the container choose between two candidates). Before repeating the claim in a review, grep `implements <Interface>` repo-wide (one hit = proof; two = the NEON really does change) and read the consumer's factory line in the NEON. A second implementer or an optional/variadic factory argument turns the "unchanged" into a silent resolution error or a wrong binding — the kind CI catches only if the suite instantiates the consumer.
Evidence: shoptet/cms4#47339 (task MIN-150, review 2026-11-02) — MarketsCountChecker swaps GetMarketsQuery dispatch for FindMarketRepositoryInterface::count(); MarketReadRepository is the sole implementer (repo-wide grep, one hit), the checker's factory passes only `logger:` (multishop-services.neon:508), NEON unchanged.
