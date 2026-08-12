// CSV twin of the CIRO 26-0076 eligibility screen — the analyst-in-Excel
// surface. One row per screened contract, all three statuses (free flag tier:
// status + reason; the evidence file is the paid artifact). Same data the
// HTML page and .json render.
import { getAllEvents, getMarketsForEvent } from '../../lib/universe';
import { getScreenSummary, getEligibility } from '../../lib/eligibility';

const esc = (v: string) => (/[",\n\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v);

export async function GET() {
  const summary = getScreenSummary();
  const rows: string[][] = [[
    'cm_market_id', 'venue', 'venue_id', 'question', 'status', 'reasons', 'review_cluster',
    'permitted_category', 'resolves', 'resolution_source', 'rcg_grade', 'regime', 'screen_version', 'screened_at',
  ]];
  const seen = new Set<string>();
  // Eligible-first, A-grade-first ordering: the analyst's eye lands on row 1, so the top of
  // the file should be the cleanest slice of the screen, not bundle order.
  const statusRank: Record<string, number> = { eligible: 0, review: 1, not_eligible: 2 };
  const body_rows: string[][] = [];
  for (const ev of getAllEvents()) {
    for (const m of getMarketsForEvent(ev.event_id)) {
      const rec = getEligibility(m.market_id);
      if (!rec || seen.has(m.market_id)) continue;
      seen.add(m.market_id);
      body_rows.push([
        m.market_id,
        (m as any).platform ?? '',
        (m as any).platform_market_id ?? '',
        ev.question,
        rec.status,
        (rec.reasons ?? []).join(';'),
        rec.cluster ?? '',
        rec.permitted_category ?? '',
        (m.resolve_at ?? m.close_at ?? '').slice(0, 10),
        m.resolution_source ?? '',
        rec.rcg_grade ?? '',
        rec.regime,
        summary?.screen_version ?? '',
        rec.screened_at,
      ]);
    }
  }
  // status (eligible→review→not_eligible), then grade (A→C, blanks last), then id for determinism
  body_rows.sort((a, b) =>
    (statusRank[a[4]] ?? 9) - (statusRank[b[4]] ?? 9) ||
    (a[10] || 'Z').localeCompare(b[10] || 'Z') ||
    a[0].localeCompare(b[0])
  );
  rows.push(...body_rows);
  // UTF-8 BOM: Excel's double-click open sniffs the BOM, not HTTP headers —
  // and the static build strips the charset header anyway. ~190 rows carry
  // non-ASCII question text that would otherwise mojibake.
  const body = '\ufeff' + rows.map((r) => r.map((v) => esc(String(v))).join(',')).join('\n') + '\n';
  return new Response(body, {
    headers: { 'Content-Type': 'text/csv; charset=utf-8' },
  });
}
