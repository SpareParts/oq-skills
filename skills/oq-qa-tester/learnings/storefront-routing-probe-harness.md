**Trigger:** QA that has to check many storefront hosts (routing, alias→canonical hops, redirects) on the dev stack, where every check must start from a cold `env:` cache.

**Rule:** Write one probe script and reuse it for the whole run instead of ad-hoc curls — it removes the single biggest source of false results (a stale `env:<host>` blob) and gives comparable evidence lines:
```bash
#!/bin/bash   # probe.sh <host-without-.test> [path]
H="$1"; P="${2:-/}"
./docker/dev compose exec -T keydb sh -c "redis-cli DEL 'env:$H' 'env:www.$H' > /dev/null"
OUT=$(curl -sk -o /tmp/qa_body.html -w '%{http_code} %{redirect_url}' "https://$H.test$P")
echo "REQ  https://$H.test$P"; echo "RESP $OUT"
grep -oE '<html[^>]*>|<title>[^<]*</title>|<link rel="canonical"[^>]*>' /tmp/qa_body.html | head -8
```
`%{redirect_url}` gives the Location without a second request, `<html lang>` plus the `<title>XX</title>` language-flag rows identify which sales channel answered (see missing-routing-row-serves-unscoped-storefront), and `curl -sk` sidesteps both the `*.myshoptet.com.test`-only dev cert and the Chrome extension allowlist that refuses most non-fenix hosts. Take a full baseline sweep of every host BEFORE the first mutation and repeat it verbatim at the end — that final sweep is the restore proof, alongside a `diff` of a `SELECT *` snapshot of the tables you touched.
