---
status: active
dimension: security
date: 2026-10-19
---

# A body-token gate that reads JSON only when `getContentTypeFormat() === 'json'` must match the content-type tolerance of the payload resolver that makes existing traffic work

Why: clients that send `JSON.stringify(payload)` through `fetch()` without setting a Content-Type header arrive as `text/plain;charset=UTF-8`, yet Symfony's `MapRequestPayload` resolver (`RequestPayloadValueResolver`) still `json_decode`s `getContent()` regardless of content type — so the same request binds fine today and gets 403'd by a new gate that branches on the content-type format. Before shipping any body-token extractor, diff its content-type tolerance against the payload resolver the controller actually uses, and add a test that reproduces the REAL client wire format (string body, no content type), not a `CONTENT_TYPE: application/json` fixture that no client sends.
Evidence: shoptet/cms4#46656 review (task MIN-94, 2026-10-19, artifact 0aec49b4) — CsrfTokenExtractor's `getContentTypeFormat() === 'json'` check vs RequestPayloadValueResolver's unconditional decode.
