---
status: active
dimension: general
date: 2026-10-02
---

# Multishop coding docs' "final readonly" CQRS requirement is normative — doc examples must teach the rule and note where deployed code lags, never mirror lagging classes or weaken the rule

Why: the deployed Multishop query-side contract classes (GetMarketsQuery, GetMarketsQueryHandler — readonly WITHOUT final) predate the docs' final-readonly rule, while the command side already complies. A docs PR that byte-mirrored the deployed classes into the tutorial examples therefore looked like it "removed final" and drew a team correction: "Why did you remove "final" from Query and Handler definition? It makes sense in my eyes." (Ondrej Hatala, task MIN-22, 2026-10-02). The fix teaches final readonly in the examples plus an explicit note that the deployed query-side classes still lack final. Reviews of Multishop doc changes must distinguish descriptive claims (versions, class names, signatures — these must match the code) from normative requirements (these state the team's direction — flag the lag, don't erase the rule). Note: this file amends the opposite proposal from that PR's review report ("doc examples mirroring the real code are correct") — the human correction reverses it.
Evidence: PR shoptet/cms4#45627, heads 53a534c14a → c828c528eb — cms/packages/Multishop/docs/coding/queries-and-commands.md:47 vs cms/packages/Contracts/Multishop/Market/Query/GetMarketsQuery.php:15.
