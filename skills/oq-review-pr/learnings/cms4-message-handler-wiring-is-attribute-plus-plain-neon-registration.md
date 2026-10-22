---
status: active
dimension: architecture
date: 2026-10-22
---

# cms4 message handlers need only #[AsMessageHandler] plus a plain NEON service line — prove bus routing via the compiled container's handlers-locator map

Why: fmasa/messenger's MessengerExtension discovers handlers by reflecting ALL container service definitions for #[AsMessageHandler] (vendor/fmasa/messenger/src/Messenger/DI/MessengerExtension.php, getHandlerDefinitionsForService) — no messenger bus-section entry and no tag are required, and an attribute without a `bus` argument registers on every bus's locator (harmless; queries are always dispatched synchronously via QueryBus + SenderStamp('sync')). To PROVE a new query routes, compile the container (APP_ENV=dev php build/compile-container.php) and grep the generated Container_*.php for the message FQCN inside createServiceMessenger__queryBus__handlersLocator — the map must show the handler service and __invoke. Scoped file-only phpstan runs cannot see wiring; CI boots prove it only indirectly.
Evidence: shoptet/cms4#46806 review (task MIN-107, 2026-10-22) — GetCountryMarketsViewQuery mapped to service 01781 in the compiled container; config/app/multishop-services.neon:265.
