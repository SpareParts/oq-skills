---
status: active
dimension: domain-integrity
date: 2026-10-25
---

# A render-degradation fix for unparsable stored rows must re-check the delete/update paths before the PR body calls the row "deletable"

Why: the normalizer or matcher that threw on the read path usually also sits on the ownership-check path of the delete/update services, so the fix that makes a corrupt row render often leaves it visible but immutable. Walk each write path (`Delete*Service`, `Update*Service`) for the same row class before writing the claim, or scope the claim to the row class it actually holds. Reading "visible" and "deletable" as one property is the trap: only the read path was changed.
Evidence: shoptet/cms4#46951 review (task MIN-121, 2026-10-25) — the body's "What" claimed the unparsable rows are "visible and deletable", while its own Decisions/follow-ups admitted the null-channel row still cannot be deleted: `DeleteRedirectionService.php:63` → `matchesBySourceOrTargetPattern()` → 400.
