---
status: active
dimension: domain-integrity
date: 2026-10-19
---

# Making an exception checked ripples only through ports that declare @throws — an untyped parallel port silently swallows the checked-exception contract, and PHPStan stays green

Why: when a PR promotes an exception to a `CheckedException` and adds `@throws` to the concrete class but not to the Domain port it implements, every caller typed by the interface sees no throw: `missingType.checkedException` never fires, the failure is invisible to static analysis exactly where it still escapes, and a "the @throws cascade is complete" body claim is true only for the paths the PR touched. Two ports for the same underlying operation must agree on their throw contracts. Check the implementer's interface, not just the implementer, before accepting a "cascade complete" claim. Related but different from `checked-exception-throws-ripple-to-every-transitively-throwing-caller`, which is about the production callers' `@throws` ripple in the same PR — here the interface itself never declares the throw, so the ripple never starts.
Evidence: shoptet/cms4#46567 review (MIN-89, 2026-10-19) — `BasicSettingsRepository::save` (Infrastructure/Market/BasicSettingsRepository.php:22, @throws added) vs `BasicSettingsRepositoryInterface::save` (Domain/Market/Repository/BasicSettingsRepositoryInterface.php:9, no @throws); settings-path escape verified to the controller.
