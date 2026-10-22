---
status: active
dimension: testing
date: 2026-10-21
---

# PHPat's ShouldNotDepend tracks usage edges, not bare `use` imports — an import-only probe proves nothing

Why: ShouldNotDepend tracks constant use (incl. `::class`), params, returns, new, instanceof, static calls, catch, properties, attributes, parents, traits, interfaces and docblock tags (ignore_doc_comments: false), but NOT a bare unused `use` statement. A negative-control probe that adds only an import stays green and proves nothing; the probe must add a real usage edge. Complements the existing learning `phpat-docblock-throws-dependencies-are-guarded`.
Evidence: shoptet/cms4 PR #46759 commit 0f2a8845dd review (task MIN-104, 2026-10-21) — import-only probe green, `::class` usage probe fired `phpat.testApplicationCommandHandlersDoNotDependOnQueryHandlers`.
