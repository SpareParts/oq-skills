**Trigger:** QA on the project-wide vs sales-channel-scoped `default_language_code_frontend` option (Multishop language decoupling, epic CZ3MUL1-882).

**Rule:** Which action writes which scope (verified 2026-09-17 on PR #44496):
- Market Settings → Languages and currencies → Save: writes the **channel-scoped** row every time (even with nothing changed), and when that market is primary also the **project-wide** row via `SalesChannelPrimaryLanguageChangedEvent`.
- Market Settings → Settings → Save: writes the **project-wide** row only (from the channel's *assigned* primary language), via `MarketBasicInformationChangedEvent`. Leaves the scoped row alone — so it repairs a corrupted project-wide value but never a corrupted scoped one.
- Ticking *Default store* (set-as-primary): writes the project-wide row from the promoted channel's **assignment**, deliberately ignoring that channel's scoped option — which therefore stays stale after the switch.
- Market synchronization (`SynchronizeMarketWithLegacyDataCommand`, cron job 5547 — skipped whenever the `multishop` module is active, so only runnable on non-multishop projects): writes both scopes.

**The storefront serves the CHANNEL-SCOPED value**, not the project-wide one: with project-wide `en` and channel `cs`, `https://<shop>.test/` returned `<html lang="cs">`. So a stale scoped option is the user-visible defect and a stale project-wide one is not. Each save reaches the storefront on the next request with no cache flush. Cheapest storefront probe: `curl -sk` and grep `<html[^>]*>` plus `<title>`.
