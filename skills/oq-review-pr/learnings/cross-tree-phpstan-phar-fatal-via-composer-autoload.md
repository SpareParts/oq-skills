---
status: active
dimension: general
date: 2026-11-07
---

# Running one tree's `vendor/phpstan/phpstan/phpstan` with the working directory inside a different tree fatals on a redeclared ComposerAutoloaderInit class — each extracted tree must run its own `./vendor/...` binary from its own root

Why: the phar's bootstrap `require_once`s `vendor/autoload.php` resolved against the invoking cwd, so tree A's phar run with cwd inside tree B redeclares tree B's `ComposerAutoloaderInit…` class and dies with a PHP fatal before analysis starts. This bites the /tmp PR-extraction flow when two extractions sit side by side and the second run keeps the first tree's cwd (or an absolute path to the other tree's phar). The fatal names the analysed tree's file paths, so it reads like a defect in the PR under review rather than the tooling mistake it is — the reviewer's first instinct is to report a broken head. Invoke each tree's own `./vendor/phpstan/phpstan/phpstan` from that tree's root (an absolute path to `treeA/vendor/...` with cwd `treeB` is exactly the failing shape) and the run proceeds.
Evidence: shoptet/cms4#47732 / #47731 review (task MIN-178, 2026-11-07) — the review round hit it while running PHPat/PHPStan on /tmp-extracted trees; the reviewer's Proposed learnings block records it.
