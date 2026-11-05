---
status: active
dimension: domain-integrity
date: 2026-11-05
---

# Reading request input through an API that throws on non-scalar values turns hostile array-valued input into an uncaught 500 instead of the intended 4xx — prefer a non-throwing read and pin one test row per hostile shape

Why: `Symfony\Component\HttpFoundation\InputBag::get()` throws `BadRequestException` when the value is an array, so a request field the code only wants as a string becomes an attacker-triggered exception rather than a validation failure. In the evidence PR a `__csrf__` form/JSON value of `["a"]` or `{"a":1}` escaped the gate as an uncaught `BadRequestException` — a 500 and the wrong error contract, where the gate intended a fail-closed 403; the legacy getter it replaced tolerated arrays and returned null, so this was a regression in the error path rather than a new hole. Read through the non-throwing API (`InputBag::all()[field] ?? null`) plus a type check, or catch the exception and map it to the intended status, and pin one test row per hostile shape: form array, JSON array, JSON object.
Evidence: shoptet/cms4#46656 review and re-review (task MIN-94, 2026-11-04/05), finding M1; `CsrfTokenExtractor.php:15`/`:45` before vs `:16`/`:50-57` after.
