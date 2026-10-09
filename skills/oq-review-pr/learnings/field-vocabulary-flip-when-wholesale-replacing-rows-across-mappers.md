---
status: active
dimension: domain-integrity
date: 2026-10-08
---

# When the FE replaces rows wholesale from one backend mapper with rows from another, diff the two mappers' field-NAME vocabularies, not just the matching key

Why: cms4's `DnsPresetRecordMapper` (TXT → `content`) and `DnsValidationEntryDtoMapper` (SPF → `value`) name the same concept differently, so a key-matched wholesale replacement silently changes the rendered field label ("Content" → "Value") once a verdict attaches; a fixture that hand-copies one vocabulary masks the flip.
Evidence: PR shoptet/cms4#46009 review (task MIN-44, 2026-10-08); `recordsTable.tsx:87`, `DnsPresetRecordMapper.php:87`, `DnsValidationEntryFactory.php:264`, `msw/.../responses.ts:85-89`.
