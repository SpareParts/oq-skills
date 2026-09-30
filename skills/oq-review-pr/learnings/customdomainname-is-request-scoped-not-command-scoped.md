---
status: active
dimension: domain-integrity
date: 2026-09-29
---

# #[CustomDomainName] on Multishop request DTOs is request-scoped, not command-scoped — alternate dispatchers of ConnectCustomDomainCommand bypass it

Why: UpdateMarketDomainCommandHandler (fed only by the ops manual @never job updateMarketDomain, scripts/cron/Multishop/UpdateMarketDomainJob.php) validates via DomainDataValidator/DomainNormalizer before dispatching Connect/ChangeCustomDomainCommand — DomainNormalizer::isValid requires just ≥2 labels with no reserved-TLD or 3-level check — so domain states every request path forbids are writable from that path regardless of FE/BE mirror fidelity. Domain-integrity reviews in this area must not treat request-DTO validation as closure; check command dispatchers, not only requests.
Evidence: shoptet/cms4#45366; cms/packages/Multishop/Application/Market/CommandHandler/UpdateMarketDomainCommandHandler.php:53-58; cms/packages/Multishop/Domain/Dns/Service/DomainNormalizer.php isValid().
