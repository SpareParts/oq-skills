---
status: active
dimension: domain-integrity
date: 2026-10-08
---

# "An escaping exception aborts all later X" claims need registration-order and flag-cooccurrence checks, not just loop mechanics

Why: a runner loop that iterates registered items and calls them unguarded makes any per-item crash mechanically "abort all later items", but the claim must be tested against the wiring: if the failing item is registered LAST (config/app/multishop-services.neon:186) and the only context enabling it carries no other item's flag (Synchronizers/ShippingMethodsSynchronizer.php:34-38, single-badge builder), the blast radius is latent — the accurate impact is the raw escape itself. PR bodies stating the maximal consequence as current fact make maintainers over-weight the path's coupling; a footnote hedge ("today the crash surface is…") does not cure an overstated headline. Check the DI registration order + which flags co-occur in every real context builder before repeating the loop's mechanics as a current consequence.
Evidence: shoptet/cms4#45938 review (MIN-41, 2026-10-08) — body "aborts all later partials" vs shipping registered last + single-badge context; runner loop cms/packages/Multishop/Application/Synchronization/Runner/SynchronizationRunner.php:37-46.
