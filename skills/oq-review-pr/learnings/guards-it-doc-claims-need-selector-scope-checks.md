---
status: active
dimension: testing
date: 2026-10-13
---

# A doc note claiming "test X guards the rule" must be checked against the guard's selector scope, both directions — the named classes are covered AND the rule's other members aren't silently uncovered

Why: MultishopCqrsShapeTest guards Multishop Application Query/Command messages + handlers and Contracts *queries* only; Contracts *commands* (e.g. Shoptet\Contracts\Multishop\Market\Command\ChangeStatusCommand) have naming-only rules in MultishopApplicationContractsTest and no final/readonly assertion, so a regression there would not fail `make tests-architecture` even though the doc's Command Requirements state the same final-readonly rule. A doc note scoped to the named classes is still true — but reviews of "guards it" claims should pin the selector regexes to the rule's full member set and flag the uncovered residue as a follow-up guard extension, not a doc defect.
Evidence: shoptet/cms4#46216 review (MIN-64, 2026-10-13) — MultishopCqrsShapeTest.php:20-22,60-74 vs MultishopApplicationContractsTest.php:79-82; all 9 Contracts commands compliant at HEAD. (The Contracts-command gap itself was closed on master by #46880, commit 07fa761658, which added test_contracts_multishop_commands_are_final/readonly; the selector-scope check is the reusable part.)
