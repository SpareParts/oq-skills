---
status: active
dimension: general
date: 2026-09-25
---

# Never pass a possibly-empty string to `_()` — `gettext('')` returns the PO catalog header

Why: `_()` is PHP's built-in gettext alias (cms4 defines no override); `gettext('')` returns the whole PO header ("Project-Id-Version: …") by design, which then renders to users. Every `_($x->getMessage())` needs an empty-string guard; `HttpException::fromStatusCode()` defaults its message to `''`, so message-less throws are the main source.
Evidence: PR shoptet/cms4#45383, cms/packages/System/Middleware/HttpExceptionToResponseMiddleware.php:120-126 (guard), remaining unguarded sites: scripts/controllers/ShoptetValidateXMLController.php:53, admin/controllers/Marketplaces/MarketplaceOfferListingActionController.php:101, cms/packages/Marketplaces/Application/Offer/MarketplaceOfferService.php:349, cms/controllers/SocialController.php:123.
