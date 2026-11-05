---
status: active
dimension: security
date: 2026-11-05
---

# A server-side gate that reads a request body must be at least as tolerant as the framework's payload resolver that already makes the existing traffic work — diff their content-type handling before shipping, and test the real client wire format, not the `Content-Type: application/json` fixture

Why: a gate can be correct about the token and still be a production-breaking regression, because its body reader decides whether it ever sees the traffic at all. In the evidence PR the new CSRF gate read the JSON body only when `getContentTypeFormat() === 'json'`, while the admin-web mutation endpoints send `JSON.stringify` payloads through raw `fetch()` with no `Content-Type` header — the browser labels those `text/plain;charset=UTF-8`, so the gate saw "not JSON" and refused. The framework's own `MapRequestPayload` resolver, which binds those same requests today, json-decodes the raw content regardless of content type; the gate was stricter than the resolver and would have 403'd requests that work before the module was even switched on. Catch it by diffing the gate's content-type branch against the resolver's, and by exercising the wire format the client actually sends (`text/plain`, no header) instead of the `application/json` test fixture. The fix dropped the content-type check and decoded `getContent()` with non-array-root and non-string-value normalization — the resolver's tolerance, mirrored.
Evidence: shoptet/cms4#46656 review (task MIN-94, 2026-11-04), blocker B1; `CsrfTokenExtractor.php:33-46` vs `RequestPayloadValueResolver.php:201-220`.
