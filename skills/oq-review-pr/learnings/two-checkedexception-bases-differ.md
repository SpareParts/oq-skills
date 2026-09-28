---
status: active
dimension: domain-integrity
date: 2026-09-28
---

# cms4 has two `CheckedException` bases with different SPL parents (Multishop's extends \Exception, Contracts' extends \RuntimeException) — reparenting an exception between them moves it between SPL catch branches, so grep catch sites of the NEW parent, not only the old one

Why: reparenting changes which broad SPL catches (e.g. `catch(\RuntimeException)`) apply, so a catch-site inventory made under the old parent silently goes stale. The existing learning `multishop-exceptions-are-flat-final-leafs.md` covers leaf-class catch-ordering and is still valid — this rule refines it for the reparent case.
Evidence: cms/packages/Multishop/Application/Exception/CheckedException.php, cms/packages/Contracts/Multishop/Exception/CheckedException.php, shoptet/cms4#45407 (task MIN-10, independent review 2026-09-28).
