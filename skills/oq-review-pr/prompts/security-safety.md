## Your assigned dimension: Security & safety

- Check for hardcoded secrets, tokens, or credentials.
- Check file operations for path validation.
- Check user input validation/sanitization.
- Check SQL injection, XSS, authorization, data leak, and multi-tenant isolation risks.
- Scrutinize sensitive config changes such as `.env*`, `**/config/**`, CI, Docker, and
  dependency files.

This dimension owns the "high-attention files" list from the shared instructions above
— if the diff touches any of those paths, say so explicitly even when you find nothing
wrong, so the orchestrator knows the area was checked.
