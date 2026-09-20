**Trigger:** Need the response (or request) BODY of an admin AJAX call — `read_network_requests` returns only URL/method/status.

**Rule:** Install a capture hook in the page before acting, then read it back:
```js
window.__qaCaptured=[]; const of=window.fetch;
window.fetch=async(...a)=>{const r=await of(...a);const u=typeof a[0]==='string'?a[0]:a[0].url;
  if(u.includes('/submit')){window.__qaCaptured.push({u,status:r.status,body:await r.clone().text()});} return r;};
// + mirror on XMLHttpRequest.prototype.open/send for jQuery-era calls
```
Hooks die on every navigation — re-install per page instance. For idempotent GET/validate endpoints, a direct same-origin `fetch` from the logged-in tab is simpler (no CSRF header needed on Symfony-routed admin JSON controllers).
