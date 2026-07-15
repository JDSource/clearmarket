#!/usr/bin/env bash
# Who is actually USING the API — recurring consumers and their trends, from call_log (D1).
# Companion to cf-analytics.sh (point-in-time digest); this one answers "which developers/
# agents keep showing up, since when, and what do they do" — pull it monthly to see the trend.
# Usage: ./scripts/consumer-trends.sh [DAYS]   (default 30)
set -uo pipefail
export PATH="/usr/local/opt/node@22/bin:$PATH"
cd "$(dirname "$0")/.."
DAYS="${1:-30}"

# D1 needs the wrangler OAuth session; the under-scoped .env token would override it.
trap 'mv -f .env.__cf_hidden .env 2>/dev/null || true' EXIT
mv -f .env .env.__cf_hidden 2>/dev/null || true
unset CLOUDFLARE_API_TOKEN CLOUDFLARE_ANALYTICS_TOKEN
q(){ npx -y wrangler@latest d1 execute clearmarket --remote --json --command "$1" 2>/dev/null \
     | python3 -c "import sys,json
raw=sys.stdin.read()
try:
    d=json.loads(raw[raw.index('['):raw.rindex(']')+1] if '[' in raw else raw)
except Exception:
    print('    (parse error)'); sys.exit(0)
rows=(d[0] if isinstance(d,list) else d).get('results',[])
[print('    '+' | '.join(f'{k}={v}' for k,v in r.items())) for r in rows] or print('    (none)')"; }

CRAWLER="COALESCE(user_agent,'') NOT LIKE '%bot%' AND COALESCE(user_agent,'') NOT LIKE '%Bot%' AND COALESCE(user_agent,'') NOT LIKE '%crawl%' AND COALESCE(user_agent,'') NOT LIKE '%spider%'"

echo "=== ClearMarket consumer trends — last ${DAYS} days ==="
echo "--- recurring consumers (>=4 distinct days, crawlers excluded): who keeps coming back ---"
q "SELECT country c, substr(COALESCE(user_agent,'(null)'),1,42) ua, action, COUNT(DISTINCT date(ts)) days, COUNT(*) n, MIN(date(ts)) first, MAX(date(ts)) last FROM call_log WHERE ts>=datetime('now','-${DAYS} days') AND $CRAWLER GROUP BY c, ua, action HAVING days>=4 ORDER BY days DESC, n DESC LIMIT 20;"
echo "--- known consumer #1: the daily movers cron (streak check) ---"
q "SELECT COUNT(DISTINCT date(ts)) days_active, MIN(date(ts)) first, MAX(date(ts)) last FROM call_log WHERE action='list_movers' AND user_agent LIKE 'python-requests%';"
echo "--- agent surfaces by week (a2a + real MCP; excludes card/manifest polling) ---"
q "SELECT strftime('%Y-%W',ts) wk, surface, COUNT(*) n, COUNT(DISTINCT requester) uniq FROM call_log WHERE surface IN ('a2a','mcp') AND action NOT IN ('agent_card') GROUP BY wk, surface ORDER BY wk;"
echo "--- discovery-doc pickup (who reads the agent card / x402 / api-catalog) ---"
q "SELECT substr(COALESCE(user_agent,'(null)'),1,42) ua, action, COUNT(*) n, COUNT(DISTINCT date(ts)) days, MAX(date(ts)) last FROM call_log WHERE action IN ('agent_card','x402_manifest','api_catalog') GROUP BY ua, action ORDER BY n DESC LIMIT 12;"
echo "--- new first-time non-crawler UAs this period (watch list candidates) ---"
q "SELECT substr(COALESCE(user_agent,'(null)'),1,42) ua, MIN(date(ts)) first_seen, COUNT(*) n FROM call_log WHERE $CRAWLER GROUP BY ua HAVING first_seen>=date('now','-${DAYS} days') ORDER BY first_seen DESC LIMIT 15;"
echo "--- keyed users (conversion check) ---"
q "SELECT requester, COUNT(*) n, MIN(date(ts)) first, MAX(date(ts)) last FROM call_log WHERE requester LIKE 'key:%' GROUP BY requester ORDER BY last DESC LIMIT 10;"
echo "=== done ==="
