---
status: active
dimension: general
date: 2026-10-26
---

# Project::getUrl()/getDomain() is runtime-context-dependent: primary/current-market canonical in admin/admin-api/storefront, the ProjectConstants-resolved URL in cron/messenger/Core API

Why: `MarketDetectionMiddleware` (runtimes admin/admin-api/storefront only, config/app/system.neon) rewrites `$project->url` to the primary-market canonical (admin) or current-market canonical (storefront) on every request; cron/messenger-isolated/Core API contexts never run it, so there the URL is whatever `ProjectConstants::resolveFreshEnvironment` produced from `--server-name` (numeric domain → the `projects.url` row value; market domain → the normalized request domain). A PR that moves readers between `projects.url` and the runtime URL must state which context it means, and reviewers must not assume "the runtime URL" has one value: two capture paths for the same shop (admin request vs worker) can disagree whenever the best-effort `SyncProjectUrlOnDomainRoutingChangeSubscriber` (#46756, "interim fix", catch-and-log) fails to sync — the exact drift surface PR #46939 exists to remove.
Evidence: shoptet/cms4#46938 review (MIN-129, 2026-10-26) — cms/packages/System/Middleware/MarketDetectionMiddleware.php:39,48-58; cms/packages/Config/ProjectConstants.php:451-456,498-499; config/app/system.neon:30-31.
