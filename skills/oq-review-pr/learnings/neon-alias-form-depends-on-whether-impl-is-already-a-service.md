---
status: active
dimension: general
date: 2026-10-16
---

# A NEON port alias to an implementation that is already its own service must use `factory: @<service>`, not `create: <FQCN>`

Why: in cms4 NEON, `type:` + `create: <FQCN>` registers a NEW service under the port type. That is fine when the implementation has no other registration, but when the class already appears earlier in the same file's service list it produces a second instance and makes autowire-by-type ambiguous (two services of the implementation's type). `type:` + `factory: @<existing service>` reuses the existing instance instead. Before copying a sibling alias, check whether the implementation class is already registered in the same file and pick the form accordingly.
Evidence: shoptet/cms4#46450 review (task MIN-76, artifact f5ec6389) — `config/app/localization-services.neon:79` (repository registered as its own service) vs `:93-96` (port aliased via `factory: @ref`); sibling `config/app/catalog-services.neon:421-429`.
