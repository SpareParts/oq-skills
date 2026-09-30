---
status: active
dimension: domain-integrity
date: 2026-09-29
---

# MultiShop DNS controllers throw MarketNotFoundException for a missing sales channel — pre-existing house style, flag softly, never block

Why: `DomainTransferController` (and `DnsSettingsOrchestrator`) throw `MarketNotFoundException` with a truthful "Sales channel with ID %d not found." message when `GetSalesChannelByIdQuery` returns null, then catch it locally → 404 with the cause chained. Five of seven review dimensions independently flagged the type/message mismatch on MIN-15 before establishing it is a verbatim mirror of the sibling controller — new code copying it is consistency, not a defect. The right long-term fix (a Contracts-level sales-channel-not-found exception) spans all siblings; do not ask a small label-fix PR to carry it.
Evidence: shoptet/cms4#45486, admin/controllers/MultiShop/DomainTransferController.php:61 vs MultishopDomainRedirectionsController.php:51 (new mirror); cms/packages/Multishop/Application/Dns/Service/DnsSettingsOrchestrator.php:49.
