---
status: active
dimension: testing
date: 2026-09-29
---

# cms4's test archetype mandates #[DisableReturnValueGenerationForTestDoubles] on every new test class, but the suite does not follow it yet — flag softly, never block

Why: .agents/skills/st-archetype-test/references/unit-tests.md and mocking-and-doubles.md say "use on every test class", but only ~161/1969 unit test classes carry the attribute and none of the CommandHandler/Validator neighbour tests do. New tests matching their neighbours will lack it; it looks like a violation of the archetype but is house practice — report as low-severity polish (the tests typically pass with the attribute since exercised methods are explicitly configured), not a blocking finding.
Evidence: shoptet/cms4#45441 (three new test classes without it, all three neighbour reference tests without it).
