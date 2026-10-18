---
status: active
dimension: testing
date: 2026-10-18
---

# In cms4, a Domain service that fan-out tests double with `createMock` must be `readonly`, not `final readonly`

Why: making such a service `final` fails PHPUnit's `ClassIsFinalException` in tests the PR does not own — `dg/bypass-finals` is deliberately not enabled in `tests/unit`, so any fan-out test that doubles the service with `createMock` breaks. `readonly` without `final` matches the sibling Domain services (e.g. `BasicSettingsService`) and stays mockable. Before claiming the team's "final readonly" convention is violated, probe the head with a final variant to see whether the unit tree actually tolerates it; the convention is real but the test tree constrains it.

Evidence: shoptet/cms4#46565 (task MIN-85) — the reviewer reproduced the `ClassIsFinalException` empirically in three fan-out tests (`SetMarketContactInformationCommandHandlerTest`, `CreateMarketSubmitOrchestratorTest`, `FullSynchronizerTest`) and confirmed no `BypassFinals::enable` anywhere in the unit tree.
