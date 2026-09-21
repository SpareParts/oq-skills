## Your assigned dimension: Code quality

- Is the code readable and self-documenting?
- Are types used properly? Avoid `mixed` when possible; never accept `@ts-ignore`,
  `as any`, or equivalent suppression as a solution.
- Are error cases handled with meaningful exceptions or control flow?
- Is immutability respected where appropriate, e.g. `final readonly class` for DTOs and
  `DateTimeImmutable` over `DateTime`?
- Are magic strings/numbers better represented as constants, enums, or existing domain
  values?
