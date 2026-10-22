---
status: active
dimension: general
date: 2026-10-22
---

# Every cms4 phpstan config includes the gitignored build/phpstan.local.neon — touch it before any run in a fresh checkout

Why: phpstan.neon, phpstan-l10.neon and phpstan-architecture.neon all `include: build/phpstan.local.neon`, which is gitignored and absent from a fresh clone/archive; the run aborts on the missing include before analysing anything. `touch build/phpstan.local.neon` (empty file is fine) unblocks phpstan, phpstan-l10 and the PHPat architecture runner; composer scripts do the same. A PR body's "this clone lacks build/phpstan.local.neon so PHPStan aborts" is an environment note, not a verification result — reviewers can and should just touch it and run.
Evidence: shoptet/cms4#46806 review (task MIN-107, 2026-10-22); phpstan.neon:9, phpstan-l10.neon:9, phpstan-architecture.neon (includes block).
