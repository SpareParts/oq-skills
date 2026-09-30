---
status: active
dimension: domain-integrity
date: 2026-09-30
---

# cms4's Query bus is structurally synchronous — deleting Query/handler classes strands no queued messages; prove it via the SenderStamp('sync') chain, not just messenger.neon routing

Why: `config/ext/messenger.neon` routes only Commands (no Query entries), but the stronger proof is structural: `QueryBus::handle()` always dispatches with `SenderStamp('sync')` (cms/packages/Framework/MessageBus/QueryBus.php:32) and the custom `MessengerExtension` wires `StampAwareSendersLocator`, which yields no senders for `'sync'` (StampAwareSendersLocator.php:31-33), neutralizing the `*: commands` routing fallback (messenger.neon:313). No Query message is ever serialized to a transport, so a deletion PR for read-side classes cannot strand queued messages and needs no queue-drain analysis — check the stamp chain once, cite it, move on.
Evidence: shoptet/cms4#45504 (MIN-17 review, 2026-09-30); cms/packages/Framework/MessageBus/{QueryBus,MessengerExtension}.php, config/ext/messenger.neon:313.
