---
status: active
dimension: naming
date: 2026-09-25
---

# cms4 msgids come in two accepted shapes: `_UPPERCASE_KEY` for shared keys, English sentence + period for one-offs

Why: a new one-off msgid like `_('The redirection was not found.')` is house style (cf. 'Export type was not found.', 'Shipper was not found.'); shared/reusable keys use `_MULTISHOP_ERROR_*`-style uppercase. No `.po` update is needed in the PR — extraction/translation runs via tools/st-translations + Weblate, gated by the Check Untranslated Translations CI which tolerates new msgids.
Evidence: PR shoptet/cms4#45383, admin/controllers/MultiShop/MultishopDomainRedirection{Create,Detail,Delete,Update}Controller.php, .github/workflows/reusable-check-untranslated.yaml.
