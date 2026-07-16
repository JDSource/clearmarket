#!/usr/bin/env python3
"""
sweep_past_due.py — daily bundle-side status reconciliation (the freshness cadence fix).

Targets markets in the SERVED bundle (web/data/universe-enriched-linked.json) that read
status='open' but are past their resolve/close date, asks each market's venue for the truth
(settle_status_sweep's query functions, verbatim), and writes the corrected bundle in place.
Zero LLM calls — venue status GETs only. Complements, not replaces:
  - the Worker's daily reconcileStatus cron (heals D1 only; static pages render from the bundle)
  - the monthly deep sweep in reconcile-bundle.sh (carried-market pass at re-enrich time)
First run 2026-07-06 cleared a 3.5-week backlog of 3,980; the daily increment is ~50-150.

Run AFTER fetching the live bundle from R2, BEFORE build_resolution_log.py + the R2 re-upload
(see .github/workflows/freshness-daily.yml). Exits 0 always; prints the swept count.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import settle_status_sweep as S  # noqa: E402  (reuses _get/sweep_kalshi/sweep_poly + BUNDLE path)

bundle = json.loads(S.BUNDLE.read_text())
now = datetime.now(timezone.utc)

# Markets referenced by published signal wires. Wires serve a build-time status field, and an
# EARLY-resolved market (settled before its resolve_at — SCOTUS/SpaceX class) never trips the
# past-due filter, so its wires would read 'live' until the deadline. Venue-check every open
# wire-referenced market regardless of deadline. Regex over frontmatter (CI has no YAML dep);
# catches primary + related ids — the extra GETs are bounded by the wire universe.
SIGNALS_DIR = Path(__file__).resolve().parent.parent / "web" / "src" / "content" / "signals"
wire_ids: set[str] = set()
for f in SIGNALS_DIR.glob("*.md"):
    wire_ids.update(re.findall(r'platform_market_id:\s*"?([^\s"]+)"?', f.read_text()))


def past_due(m):
    if m.get("status") != "open":
        return False
    t = m.get("resolve_at") or m.get("close_at")
    if not t:
        return False
    try:
        dt = datetime.fromisoformat(str(t).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt < now
    except ValueError:
        return str(t)[:10] < now.date().isoformat()


def wire_referenced(m):
    # 'closed' included: closed = trading stopped, settlement unconfirmed — without a
    # re-check a wire market that closes then settles would stick at 'closed' forever.
    return m.get("status") in ("open", "closed") and m.get("platform_market_id") in wire_ids


target = [m for m in bundle["markets"] if past_due(m) or wire_referenced(m)]
kal = [m for m in target if m.get("platform") == "kalshi"]
pol = [m for m in target if m.get("platform") == "polymarket"]
n_wire = sum(1 for m in target if not past_due(m))
print(f"sweep targets: {len(target)} (kalshi {len(kal)} / polymarket {len(pol)}; wire-referenced pre-deadline {n_wire})", flush=True)

if not target:
    print("nothing to sweep — bundle untouched")
    sys.exit(0)

stats = {"resolved": 0, "closed": 0, "still_active": 0,
         "gone_closed": 0, "gone_left": 0, "errors": 0}
S.sweep_kalshi(kal, stats)
print(f"  kalshi done: {stats}", flush=True)
S.sweep_poly(pol, stats)
print(f"  total: {stats}", flush=True)

S.BUNDLE.write_text(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {S.BUNDLE}")
