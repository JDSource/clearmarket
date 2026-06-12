#!/usr/bin/env bash
# ClearMarket 24h analytics digest — Worker health (GraphQL) + human-vs-bot call_log (D1 via OAuth).
# One-time prereq: `cd /tmp && npx wrangler login` (OAuth persists in ~/.wrangler; no token needed after).
# Usage: ./scripts/cf-analytics.sh   [HOURS]   (default 24)
set -uo pipefail
export PATH="/usr/local/opt/node@22/bin:$PATH"   # wrangler needs node 22
cd "$(dirname "$0")/.."
HOURS="${1:-24}"

# Grab the analytics token for the Worker GraphQL call BEFORE we hide .env (D1 needs OAuth, not the token).
set -a; . ./.env; set +a
ACCT="$CLOUDFLARE_ACCOUNT_ID"; ATOK="$CLOUDFLARE_ANALYTICS_TOKEN"
SINCE=$(python3 -c "import datetime;print((datetime.datetime.utcnow()-datetime.timedelta(hours=$HOURS)).strftime('%Y-%m-%dT%H:%M:%SZ'))")
UNTIL=$(python3 -c "import datetime;print(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))")

echo "=== ClearMarket — last ${HOURS}h ($SINCE → $UNTIL UTC) ==="
echo "--- Worker (clearmarket-api): requests + error outcomes ---"
curl -s -X POST https://api.cloudflare.com/client/v4/graphql \
  -H "Authorization: Bearer $ATOK" -H "Content-Type: application/json" \
  --data "{\"query\":\"query(\$a:String!,\$s:Time!,\$u:Time!){viewer{accounts(filter:{accountTag:\$a}){workersInvocationsAdaptive(limit:1000,filter:{datetime_geq:\$s,datetime_leq:\$u,scriptName:\\\"clearmarket-api\\\"}){sum{requests errors}dimensions{status}}}}}\",\"variables\":{\"a\":\"$ACCT\",\"s\":\"$SINCE\",\"u\":\"$UNTIL\"}}" \
  | python3 -c "import sys,json,collections;d=json.load(sys.stdin);g=d['data']['viewer']['accounts'][0]['workersInvocationsAdaptive'];c=collections.Counter();[c.update({r['dimensions']['status']:r['sum']['requests']}) for r in g];t=sum(c.values());print(f'  total requests: {t}');[print(f'    {k:22} {v}') for k,v in c.most_common()]"

# D1 call_log needs OAuth; wrangler auto-loads .env (under-scoped token) and would override it. Hide .env, always restore.
trap 'mv -f .env.__cf_hidden .env 2>/dev/null || true' EXIT
mv -f .env .env.__cf_hidden
unset CLOUDFLARE_API_TOKEN CLOUDFLARE_ANALYTICS_TOKEN   # else wrangler uses the under-scoped token instead of OAuth
q(){ npx -y wrangler@latest d1 execute clearmarket --remote --json --command "$1" 2>/dev/null \
     | python3 -c "import sys,json
raw=sys.stdin.read()
try:
    d=json.loads(raw[raw.index('['):raw.rindex(']')+1] if '[' in raw else raw)
except Exception:
    print('    (parse error)'); sys.exit(0)
rows=(d[0] if isinstance(d,list) else d).get('results',[])
[print('    '+' | '.join(f'{k}={v}' for k,v in r.items())) for r in rows] or print('    (none)')"; }
W="ts>=datetime('now','-${HOURS} hours')"

echo "--- call_log: REST+MCP data calls (the human-vs-bot source) ---"
echo "  by surface:";  q "SELECT surface,COUNT(*) n FROM call_log WHERE $W GROUP BY surface ORDER BY n DESC;"
echo "  by client class:"; q "SELECT CASE
     WHEN user_agent LIKE '%Googlebot%' OR user_agent LIKE '%GoogleOther%' OR user_agent LIKE '%Google-%' OR user_agent LIKE '%bingbot%' OR user_agent LIKE '%externalagent%' OR user_agent LIKE '%GPTBot%' OR user_agent LIKE '%OAI-SearchBot%' OR user_agent LIKE '%ClaudeBot%' OR user_agent LIKE '%PerplexityBot%' OR user_agent LIKE '%bot%' OR user_agent LIKE '%crawl%' OR user_agent LIKE '%spider%' THEN '1-crawler'
     WHEN user_agent LIKE 'claude-code%' OR surface='mcp' THEN '2-ai-agent'
     WHEN user_agent LIKE 'curl%' OR user_agent LIKE '%python%' OR user_agent LIKE 'wget%' OR user_agent LIKE 'Go-http%' OR user_agent LIKE '%node-fetch%' THEN '3-script'
     WHEN user_agent LIKE 'Mozilla%' THEN '4-browser(maybe-human)'
     ELSE '5-other' END klass, COUNT(*) n, COUNT(DISTINCT requester) ips
   FROM call_log WHERE $W GROUP BY klass ORDER BY klass;"
echo "  keyed vs anon:"; q "SELECT CASE WHEN requester LIKE 'key:%' THEN 'keyed-firm' ELSE 'anon-ip' END t, COUNT(DISTINCT requester) uniq, COUNT(*) calls FROM call_log WHERE $W GROUP BY t;"
echo "  top user agents:"; q "SELECT substr(COALESCE(user_agent,'(null)'),1,50) ua, COUNT(*) n FROM call_log WHERE $W GROUP BY ua ORDER BY n DESC LIMIT 12;"
echo "  by country:"; q "SELECT COALESCE(country,'?') c, COUNT(*) n FROM call_log WHERE $W GROUP BY c ORDER BY n DESC LIMIT 10;"
echo "  top actions:"; q "SELECT action,COUNT(*) n FROM call_log WHERE $W GROUP BY action ORDER BY n DESC LIMIT 12;"
echo "=== done ==="
