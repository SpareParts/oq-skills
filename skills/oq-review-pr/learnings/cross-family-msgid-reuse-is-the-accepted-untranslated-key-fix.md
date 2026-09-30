---
status: active
dimension: naming
date: 2026-09-29
---

# Reusing another feature's msgid family is the accepted cms4 fix for untranslated keys — the msgid's context segment stops describing all usage sites; review the coupling as a documented trade-off, not a naming violation

Why: when a msgid has empty msgstr and an already-translated key with identical meaning exists, house practice is to reuse it even across feature families (an `ADD-MODAL_*` label on a DETAIL page, a `NAME-SERVERS_*` state key in a redirection-records table). The key name then under-describes its usage scope and a Weblate reword of the canonical site silently changes every reuse site — but hard-coded literals keep all sites greppable and the alternative (new msgids) leaves raw keys rendered until Weblate translates them. Do not flag the cross-family reuse itself; at most note the coupling and check the PR description documents the old→new mapping.
Evidence: PR shoptet/cms4#45485 — RedirectionDetailForm.tsx:125/131 reuse AddRedirectionModal.tsx:67/74 labels, table.tsx:27 completes the NAME-SERVERS family its sibling switch arms already used; task MIN-14 explicitly prescribed the reuse route.
