#!/usr/bin/env bash
# Snapshot ONE UTC day of the zone AI-crawler/agent layer into a durable CSV — because Cloudflare
# only retains ~30 days of zone analytics (sampled), so the crawler history is otherwise lost.
# Companion to cf-crawlers.sh (same GraphQL query + family buckets); that one is an ad-hoc digest,
# this one persists a per-day, per-family series we own. Reporter: cf-crawlers-trend.sh.
#
# Usage: ./scripts/cf-crawlers-snapshot.sh [YYYY-MM-DD] [--force]
#   no date -> yesterday (UTC, the most recent COMPLETE day). --force overwrites an existing day.
# Auth: wrangler OAuth token (zone:read), pulled from wrangler config — same as cf-crawlers.sh.
# Output CSV (default ~/jeremy-os/outputs/clearmarket/crawler-history.csv; override CRAWLER_HISTORY_CSV):
#   date,family,kind,site,api,total   — plus one _ALL_TRAFFIC_ row/day (all UAs) for the % denominator.
set -uo pipefail
cd "$(dirname "$0")/.."
ZID="efb7e18526239ba3a463220737469db7"   # clearmarket.fyi zone
OUT="${CRAWLER_HISTORY_CSV:-$HOME/jeremy-os/outputs/clearmarket/crawler-history.csv}"

DATE="${1:-$(python3 -c "import datetime;print((datetime.datetime.utcnow()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'))")}"
FORCE=""; [ "${2:-}" = "--force" ] && FORCE=1

CFG="$HOME/Library/Preferences/.wrangler/config/default.toml"
[ -f "$CFG" ] || CFG="$HOME/.wrangler/config/default.toml"
OAUTH="${CLOUDFLARE_ZONE_TOKEN:-$(grep -E '^oauth_token' "$CFG" 2>/dev/null | sed 's/.*= *"//; s/".*//')}"
if [ -z "$OAUTH" ]; then echo "No OAuth token found. Run: npx wrangler whoami"; exit 1; fi

mkdir -p "$(dirname "$OUT")"
[ -f "$OUT" ] || echo "date,family,kind,site,api,total" > "$OUT"
if grep -q "^${DATE}," "$OUT"; then
  if [ -z "$FORCE" ]; then echo "skip ${DATE} (already recorded; --force to overwrite)"; exit 0; fi
  grep -v "^${DATE}," "$OUT" > "$OUT.tmp" && mv "$OUT.tmp" "$OUT"
fi

SINCE="${DATE}T00:00:00Z"
UNTIL="$(python3 -c "import datetime;d=datetime.datetime.strptime('$DATE','%Y-%m-%d')+datetime.timedelta(days=1);print(d.strftime('%Y-%m-%dT00:00:00Z'))")"

Q=$(python3 -c "import json;print(json.dumps({'query':'query(\$z:String!,\$s:Time!,\$u:Time!){viewer{zones(filter:{zoneTag:\$z}){httpRequestsAdaptiveGroups(limit:1000,filter:{datetime_geq:\$s,datetime_leq:\$u},orderBy:[count_DESC]){count dimensions{userAgent clientRequestHTTPHost}}}}}','variables':{'z':'$ZID','s':'$SINCE','u':'$UNTIL'}}))")

# CF GraphQL rate-limits bursts (code 10429) — the daily driver fires 14 queries back-to-back, so a
# 429 (or an HTML/empty body) used to surface as a JSONDecodeError and a bogus "aged out / auth
# stale" failure. Retry with backoff; only give up after 4 tries.
BODY=""
for try in 1 2 3 4; do
  RESP=$(curl -s -w $'\n%{http_code}' -X POST https://api.cloudflare.com/client/v4/graphql \
    -H "Authorization: Bearer $OAUTH" -H "Content-Type: application/json" --data "$Q")
  CODE="${RESP##*$'\n'}"; BODY="${RESP%$'\n'*}"
  if [ "$CODE" = "200" ] && printf '%s' "$BODY" | python3 -c "
import sys,json
try: d=json.load(sys.stdin)
except Exception: sys.exit(1)
sys.exit(1 if any(e.get('extensions',{}).get('code')==10429 or 'Rate limited' in e.get('message','') for e in (d.get('errors') or [])) else 0)  # CF sends errors:null on success
" 2>/dev/null; then break; fi
  echo "  retry ${try}/4 for ${DATE} (http ${CODE}, rate-limited or non-JSON) — sleeping $((15*try))s" >&2
  sleep $((15*try))
done

ROWS=$(printf '%s' "$BODY" | DATE="$DATE" python3 -c "
import sys,os,json,collections
DATE=os.environ['DATE']
raw=sys.stdin.read()
try:
    d=json.loads(raw)
except Exception:
    sys.stderr.write('  non-JSON response '+DATE+': '+raw[:160].replace(chr(10),' ')+'\n'); sys.exit(4)
if d.get('errors'):
    sys.stderr.write('  GraphQL error '+DATE+': '+json.dumps(d['errors'][:1])+'\n'); sys.exit(3)
z=d.get('data',{}).get('viewer',{}).get('zones') or []
grp=z[0]['httpRequestsAdaptiveGroups'] if z else []
FAMS=[('GPTBot','train'),('OAI-SearchBot','search'),('ChatGPT-User','agent'),
 ('ClaudeBot','train'),('Claude-User','agent'),('anthropic-ai','train'),
 ('PerplexityBot','search'),('Perplexity-User','agent'),
 ('Google-Extended','train'),('Bytespider','train'),('CCBot','train'),
 ('meta-externalagent','train'),('Amazonbot','train'),('Applebot-Extended','train'),
 ('cohere-ai','train'),('Diffbot','train'),('Omgilibot','train'),('Timpibot','train'),
 ('ImagesiftBot','train'),('YouBot','search'),('DuckAssistBot','agent'),
 ('agent-tools','agent'),('Agenstry','agent'),('cloud-crawler','agent'),
 ('ShapBot','search'),   # Parallel.ai AI-search crawler — 43K-request ingest on 2026-10-01
 ('-mcp','agent'),('mcp-','agent')]
total_all=0
fam=collections.Counter(); site=collections.Counter(); api=collections.Counter(); kind={}
for r in grp:
    c=r['count']; total_all+=c
    ua=(r['dimensions'].get('userAgent') or '').lower()
    host=r['dimensions'].get('clientRequestHTTPHost') or ''
    for name,k in FAMS:
        if name.lower() in ua:
            fam[name]+=c; kind[name]=k
            (api if host.startswith('api.') else site)[name]+=c
            break
out=[]
for name,n in fam.most_common():
    out.append('%s,%s,%s,%d,%d,%d'%(DATE,name,kind[name],site[name],api[name],n))
out.append('%s,_ALL_TRAFFIC_,all,0,0,%d'%(DATE,total_all))
print('\n'.join(out))
")
rc=$?
if [ $rc -ne 0 ]; then echo "FAILED ${DATE} (rc=$rc — 3=GraphQL error, 4=non-JSON after retries; see stderr above. Auth: verify the plist token; retention ≈ 8d)"; exit $rc; fi
printf '%s\n' "$ROWS" >> "$OUT"
NAMED=$(printf '%s\n' "$ROWS" | grep -v '_ALL_TRAFFIC_' | awk -F, '{s+=$6} END{print s+0}')
ALL=$(printf '%s\n' "$ROWS" | awk -F, '$2=="_ALL_TRAFFIC_"{print $6}')
echo "recorded ${DATE}: ${NAMED} named AI/agent / ${ALL:-0} total requests"
