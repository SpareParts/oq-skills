## Your assigned dimension: Architecture & design

- Are new classes/files in the correct directories and layers? (4-layer DDD architecture)
- Does the change follow existing architectural patterns in the codebase?
- Are responsibilities properly separated?
- Are dependencies injected rather than hardcoded?
- Is unnecessary coupling introduced?
- Are internal package classes "escaping" the package boundary? Especially check
  exceptions and domain objects/DTOs.

Ground each finding in the pattern the surrounding code actually uses, not an abstract
ideal — check a sibling class/file in the same package before flagging a deviation.
