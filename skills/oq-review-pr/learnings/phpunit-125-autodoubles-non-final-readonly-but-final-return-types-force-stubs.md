---
status: active
dimension: testing
date: 2026-10-20
---

# PHPUnit 12.5 can double a non-`final` `readonly` class, so adding `final` to a DTO breaks every `createMock` whose method returns it — at runtime, not at mock creation

Why: the mock generator emits `readonly class` test doubles, so a `readonly` DTO without `final` keeps auto-generated mock returns working. The moment `final` is added per the final-readonly convention, every `createMock` of a collaborator whose mocked method returns that type throws `ClassIsFinalException` when the doubled method is first invoked — invisible to static analysis and to a diff-only reading. A PR that adds `final` to a DTO must grep the test tree for mocks of its returning collaborators in the same PR; the fix (`->willReturn(new <DTO>(...))` with minimal constructor args) is behaviour-preserving when the test never read the return. Related, not duplicated: the open PR #19 learning `readonly-not-final-when-tests-double-a-domain-service` covers the production-side counterpart (do not `final` a service that tests double); this one covers the DTO whose type a double returns.
Evidence: shoptet/cms4#46668 review (task MIN-95, 2026-10-20, artifact 245bc0b3) — SalesChannelModuleActivationSubscriberTest.
