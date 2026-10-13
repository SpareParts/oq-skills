---
status: active
dimension: general
date: 2026-10-12
---

# products_lng.indexName is a bare slug, not a product URL — DiscussionHelper::buildTree feeds it to a helper expecting a full URL; a URL-shaped test fixture masks the mismatch

Why: `products_lng.indexName` values are `[a-z0-9-]` slugs (`IndexName::encode` strips everything else; seed data shows `unisex-hodinky-nature`-shaped values), but `DiscussionHelper::buildTree()` passes the DTO's `indexName` into `FrontEndHelper::getProductDiscussionPostUrl($productUrl, ...)`, whose parameter expects a full product URL — the sibling caller `Product::getProductDiscussionUrl()` passes `Product::$url` (`kategorie/my-product/`-shaped). With a bare slug, `StandardHelper::beforeLastChar(slug, '/')` returns `''` (strrpos false → substr length false→0 in the non-strict file), so production URLs are `':diskuze/?postId=N'` for every product since #5699 (b7510f2849) — whose only renderer is the 2G Reply link (productDetail.tpl:904). A regression test using a URL-shaped fixture (`'kategorie/my-product/'`) makes the "url built correctly" assertion pass while production data would fail it. When reviewing or writing tests in this area, use the production data shape or explicitly note the contract-under-test; when a fixture only passes with input production never produces, that is the smell.
Evidence: shoptet/cms4#46126 review (MIN-57, 2026-10-12) — cms/packages/Content/Discussion/DiscussionHelper.php:58, cms/packages/Url/Helper/FrontEndHelper.php:667-690, cms/packages/Products/Model/Product.php:1639-1642, database/migration-zero/st_pattern.sql:11478, cms/packages/Strings/Encoder/IndexName.php.
