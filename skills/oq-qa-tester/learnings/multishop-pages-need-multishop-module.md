**Trigger:** `/admin/online-obchody/` (MarketOverview) or Market Settings pages render "Stránka nenalezena" on a dev shop even though markets exist in DB.

**Rule:** Those admin sections are gated on the `multishop` module (`cms2_admin_section_map` rows 1785/1791, `hideInactiveModule=1`), which fenix (project 10000) does not have by default. Insert `multishop` into `st_<projectId>.modules`, invalidate the modules Redis cache, and the pages appear. Remove the row again at cleanup.
