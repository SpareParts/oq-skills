---
status: active
dimension: general
date: 2026-09-29
---

# Pin the trailing-dot row when mirroring BE domain validation — accept/reject aligns but step attribution legitimately diverges

Why: PHP FILTER_VALIDATE_DOMAIN (and therefore Symfony's Assert\Hostname step) accepts a trailing dot (`www.example.com.` — the TLD slice after `strrpos` is `''`, not reserved), so the BE rejects such input only at a LATER chain step with that step's message ("too short, perhaps missing www?"). An anchored FE label regex cannot reproduce this — it rejects at the syntax step with "not valid.". Both sides reject, so the mirror invariant (no round-trip, no false rejection) still holds; message parity does not, and chasing it is wrong. Add the trailing-dot row to the truth-table test with a comment accepting the divergence so nobody "fixes" either side.
Evidence: shoptet/cms4#45366 increment 0ad13cd0c2..5368847d6c; frontend/apps/admin-web/src/MultiShop/common/utils/domainValidation.ts:5 vs vendor/symfony/validator/Constraints/HostnameValidator.php hasValidTld().
