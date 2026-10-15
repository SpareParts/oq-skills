---
status: active
dimension: general
date: 2026-10-14
---

# A docs example pairing two REAL class names from different flows is falser than a fictional example — verify the Request↔Command COMBINATION, not each identifier's existence

Why: a docs PR's verification section passed every existence check (`CommandBus` exists, `CreateMarketCommand` exists, `CreateMarketRequest` exists) while the taught pairing was fiction: the request feeds the legacy-orchestrator flow, the command has zero production dispatch sites, no validation constraints (so the illustrated `catch (ValidationFailedException)` is unreachable — its handler throws a different exception), and a constructor incompatible with the request's shape. For doc examples referencing real classes, grep the *combination* — the dispatch site (`new <Command>(`), and which Request/Command/Orchestrator actually feed each other in production — and check the command's `Assert` attributes plus the handler's real throws before writing a catch. Two real names spliced from two flows read as MORE authoritative than one fictional name, which is exactly why the check must cover the pairing.
Evidence: shoptet/cms4#46374 review (MIN-70, 2026-10-14) — cms/packages/Multishop/docs/coding/controllers.md:62-68 vs admin/controllers/MultiShop/CreateMarketWizardSubmitController.php:38-47 and cms/packages/Multishop/Application/Market/CommandHandler/CreateMarketCommandHandler.php.
