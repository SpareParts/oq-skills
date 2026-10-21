---
status: active
dimension: general
date: 2026-10-20
---

# When a refactor moves a guard from implementations into their caller, check whether the guard's failure mode crossed a try/catch boundary — the old catch may have silently converted an assert/exception into reset-and-continue, and the new location may propagate it

Why: a guard like `assert($x instanceof T); if ($x !== T::A) return null;` living inside a callee that the caller wraps in `try/catch (Throwable)` has its dev-time `AssertionError` (and any other throw) silently converted to the caller's recovery path. Moving the guard to the caller — the "cleaner" placement — puts the same assert OUTSIDE the catch, so the identical failure now escapes as a 500. In the evidence PR this was benign (both kernel entry points always set the attribute, and an earlier middleware in the stack asserts the same attribute first), but the equivalence only holds because of three external facts, none of which the diff shows. Check: (1) who can reach the moved guard without the precondition, (2) whether an earlier component already fails loudly on the same precondition, (3) what the stripped-assert production path degrades to (`null !== enum` is usually the fail-safe default — verify it). Distinct from `catch-to-false-conflates-unreachable-with-answered-no` (a caller erasing a boolean contract) and from `dibi-guard-passes-but-runtime-leak-remains` (a guard not covering the failure mode): here the guard is intact and the question is which stack frame owns its throw.
Evidence: shoptet/cms4#46742 review (MIN-100, 2026-10-20) — master's resolvers asserted inside the middleware's `try/catch (Throwable)`; head's `ActiveSalesChannelMiddleware.php:35` asserts outside it. Sibling pattern: `EnvironmentSetupMiddleware`/`ProjectSetupMiddleware`/`UrlRewriterMiddleware` assert the same attribute outside any try.
