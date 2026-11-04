---
status: active
dimension: general
date: 2026-11-04
---

# A PR body describing a read-then-write race must open the table's CREATE TABLE before claiming which constraint is missing — the claimed missing key may be the primary key

Why: in the evidence PR the body's "Not covered" section claimed two concurrent commands "can still both pass exists() and double-insert. That wants a unique key on `codebook_countries.countryId`" — but that table already had `PRIMARY KEY (countryId)` (`database/schema/st_pattern.sql:1177`), so the double-insert consequence was impossible. The real race outcome is the loser getting a duplicate-key exception on the provisioning path, and the right fix (`INSERT IGNORE`, already used by `admin/controllers/CountriesListingAddController.php:67`, or catch-and-treat-as-success) never got named. Before accepting or writing a "needs a unique key/index" follow-up, read the table's `CREATE TABLE` in the schema dump (not the migration history) and state the *actual* failure mode of the race, not the one the missing-constraint story implies.

This is the sibling rule of `pr-body-inventory-counts-need-diff-verification`: a prose claim about *database state* needs the same mechanical check as a prose claim about the diff, and both fail the same way — the code is correct, only the record lies. Recount counts mechanically; open the schema mechanically.

Evidence: shoptet/cms4#47508 review (task MIN-162, 2026-11-04) — `database/schema/st_pattern.sql:1177` (`PRIMARY KEY (countryId)`) vs the PR's "Not covered" section; the body's follow-up claim was void, the code was correct.
