---
status: active
dimension: general
date: 2026-10-09
---

# When a PR moves a type AND deletes a dead file that imports it, delete the dead importer in the same commit (or first)

Why: commit 1 of a 2-commit move PR deleted the enum while the dead duplicate command — deleted only in commit 2 — still `use`d the old FQN, so the intermediate tree references a nonexistent class inside phpstan's analyzed paths: any bisect or checkout landing on commit 1 fails analysis with unknown-class, and the "clean PR" story only holds at head. Dead-file deletions are free to reorder (nothing references them — that's why they're dead), so hoist them into the move commit and keep every commit self-consistent. Flag as bisect-hygiene, not a head defect, when head CI is green.
Evidence: shoptet/cms4#46018 (MIN-45 review) — commit 2ef6be5f33 leaves Application/Market/Command/ChangeStatusCommand.php:5 importing the enum deleted by the same commit; head 92cd19b2d7 clean, CI green.
