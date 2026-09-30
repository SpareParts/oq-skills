---
status: active
dimension: general
date: 2026-09-29
---

# Registered-but-empty msgstr keys pass the untranslated-check CI — the gate verifies registration, not msgstr content, so raw-key rendering is invisible to automated gates

Why: a page can render raw msgids while every CI workflow is green: the Check Untranslated Translations workflow only checks that msgids are registered/extractable, not that the gitignored Weblate-built catalogs carry non-empty msgstr. A PR that swaps to already-translated keys is the only in-code fix; keys left on untranslated msgids keep rendering raw after merge until Weblate is filled, and no gate will catch it. Treat that CI's green as "registered", never as "translated"; verify the swap targets are msgids already rendered translated in shipped UI.
Evidence: PR shoptet/cms4#45485 — run 36586855602 (Check Untranslated Translations) green on head 37f71cc74c while the PR itself documents 3 still-untranslated `_…_DETAIL_*` keys; fix validated by byte-exact reuse of `ADD-MODAL_*`/`NAME-SERVERS_*` keys from AddRedirectionModal.tsx / StateCell.tsx.
