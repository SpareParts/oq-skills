---
status: active
dimension: domain-integrity
date: 2026-10-22
---

# Lab system hosts are a two-shape family: `<id>.labshoptet.com` parses via UrlHelper, `<id>-N.labshoptet.com` needs rewriteLabSystemDomain-style normalization

Why: reviews touching host resolution on lab must check both shapes, because only the first is
regex-covered. `UrlHelper::getProjectIdFromNumericDomain` matches `^(\d+)\.(my|lab)shoptet\.com(\.test)?`
(project-style lab host, e.g. `63003.labshoptet.com`), while the market variant `63003-2.labshoptet.com`
is rejected there (`\d+` cannot span the hyphen) and also escapes `ShoptetDomainParser`, which accepts
`myshoptet.com` registrables only — so on lab, market-style hosts resolve to null and the repo's
own `rewriteLabSystemDomain()` (StorefrontApiBridge) shows the missing normalization is a known
shape. When a review verifies host-resolution changes on lab, probe both shapes and say which
one stays null, rather than testing only the project-style row the diff added.
Evidence: shoptet/cms4#46823 review (MIN-111) — `UrlHelper.php:349-354` alternation `(my|lab)`
parses `63003.labshoptet.com`; `ShoptetDomainParser` (`NormalizedDomain::isMyShoptetComDomain`,
`MY_SHOPTET_COM_DOMAIN = 'myshoptet.com'`) leaves `63003-2.labshoptet.com` null (pre-existing,
flagged as follow-up); `ResolveProjectContextByHostQueryHandler.php:106` shows the
`<id>-N.labshoptet.com` normalization precedent.
