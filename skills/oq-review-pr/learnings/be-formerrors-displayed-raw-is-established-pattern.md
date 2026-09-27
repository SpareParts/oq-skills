---
status: active
dimension: general
date: 2026-09-26
---

# BE 422 formErrors messages are displayed raw on the FE — established pattern, not a bug

Why: `translateErrors` (frontend/apps/admin-web/src/Core/utils/forms.ts) returns `error.message` as-is, and wizard `onError` handlers do `setError(field, { message })` without `t()`. BE validation messages (English literals like 'Domain name is not valid.' or msgids like `_MULTISHOP_ERROR_...`) therefore reach the screen untranslated whenever the FE schema is bypassed. This looks like a regression in every PR touching the flow, but it is the long-standing contract across the MultiShop wizards (DomainDecision.tsx, DnsSetupMethodSelector.tsx, MarketSettings/page.tsx). Flag it only if a PR *introduces* a new BE message that merchants will hit in the normal (non-bypass) flow.
Evidence: PR shoptet/cms4#45366 investigation; cms/packages/System/Middleware/HttpExceptionToResponseMiddleware.php (does not `_()`-translate ValidationFailedException messages).
