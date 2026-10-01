---
status: active
dimension: domain-integrity
date: 2026-10-01
---

# "roundForDocument rounds to documentPriceDecimalPlaces" is mode-dependent — scope docblock parity claims to MATHEMATICAL/UP/DOWN

Why: `PriceHelper::roundForDocumentWithMode` returns `$price` completely unrounded in the default
branch (cms/packages/Products/Helper/PriceHelper.php:367-368), and `currency.rounding` defaults to
`ROUNDING_NONE` (= 0) in both schemas (st_pattern.sql, st_crm.sql) with AbstractCurrency defaulting
unset values to it (AbstractCurrency.php:65). The three cash modes round to whole units (scale 0),
not to `documentPriceDecimalPlaces`. Only ROUNDING_MATHEMATICAL/UP/DOWN round at
`documentPriceDecimalPlaces`. A wrapper that claims "the scale roundForDocument rounded to" (or
"zero behavior change vs the float contract") without scoping it to those three modes is wrong for
the DEFAULT configuration; a Money wrapper additionally introduces its own half-up rounding in
NONE mode (number_format in Money::fromFloat) that the float contract never performs.
Evidence: PR cms4#45569 — handler docblock at
cms/packages/SalesChannel/Localization/Currency/QueryHandler/Contract/GetConvertedMoneyByCurrenciesQueryHandler.php:22-23.
