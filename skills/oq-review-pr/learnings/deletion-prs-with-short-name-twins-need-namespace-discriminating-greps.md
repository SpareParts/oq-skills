---
status: active
dimension: general
date: 2026-09-30
---

# When a PR deletes classes whose short names survive on live twins, prove the dead-path claim with namespace-discriminating greps plus positive controls — and test "the only mentions were…" claims with a repo-wide short-name grep

Why: cms4's Contracts pattern means a deleted package-local class (e.g. `Shoptet\SalesChannel\SalesChannel\Query\GetSalesChannelByIdQuery`) routinely shares its short name with a live Contracts twin (`Shoptet\Contracts\SalesChannel\Query\GetSalesChannelByIdQuery`), so a bare short-name grep proves nothing. Calibrate the FQCN grep on master first (it must match exactly the deleted files' own `use` lines) so that zero matches on the head is a real result, then run a repo-wide short-name grep anyway to catch inert docblock fossils in other namespaces (a dangling `@see GetSalesChannelByIdQueryHandler` in a Warehouse contract survived a PR body claiming "the only mentions were the two handlers' own `use` lines"). Also verify historical narrative claims ("predates the Contracts one") with `git log --diff-filter=A` before repeating them — in #45504 the deleted surface was added two months AFTER its Contracts twin, i.e. duplicate-from-birth, which strengthened the deletion while making the PR body's story wrong.
Evidence: shoptet/cms4#45504 (MIN-17 review, 2026-09-30); cms/packages/Contracts/Warehouse/Query/Warehouse/GetAllWarehousesQuery.php:10.
