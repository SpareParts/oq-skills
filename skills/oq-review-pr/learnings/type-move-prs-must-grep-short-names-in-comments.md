---
status: active
dimension: general
date: 2026-10-09
---

# A type-move PR must also grep the type's SHORT name in comments and prose, not only the FQN

Why: a move's "zero residual references" grep (full FQN) passes while prose references to the old home survive — e.g. `// Literal on purpose: the AdminApi layer must not depend on Multishop\Domain (Market\Status);` (OnlineStoreView.php:29) cites the old namespace via the short form `Market\Status` and goes stale the moment the enum moves to Contracts. Value-based usage means zero behavior impact, but the comment's justification now names a dependency that no longer exists at that location, and a future reader either "fixes" the literal pointlessly or trusts a stale boundary reason. When reviewing or writing a type move, sweep `git grep '<ShortName>'` over comments/docblocks and .md, and note (don't necessarily patch) out-of-scope files whose comments the move orphans.
Evidence: shoptet/cms4#46018 review (MIN-45); cms/packages/AdminApi/Application/OnlineStore/Response/OnlineStoreView.php:29 vs cms/packages/Contracts/Multishop/Market/Enum/Status.php.
