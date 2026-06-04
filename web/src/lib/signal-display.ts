// Title / telemetry display layer for CM Signal wire items.
//
// The wire title splits into two fields (refactor 2026-06-04):
//   semantic_title — LLM-authored, durable, directional, symbol-free narrative anchor.
//                    Drives <title>, <h1>, JSON-LD name/claimReviewed (the indexed surfaces).
//   telemetry      — Python-composed (never LLM) terse as-of read, rendered as a muted track.
//
// These helpers provide the FALLBACK for the pre-refactor wires that carry only the old flat
// `headline`. New + backfilled wires set both fields directly; the fallback then never fires.
// composeTelemetry() mirrors compose_telemetry() in gen_news_cycle.py so old + new render alike.

type PrimaryMarket = {
  platform?: string;
  current_price?: number;
  volume_24h_usd?: number;
  volume_cumulative_usd?: number;
};

type SignalData = {
  semantic_title?: string;
  telemetry?: string;
  headline?: string;
  event_question?: string;
  detection_path?: string;
  primary_market?: PrimaryMarket;
  related_markets?: Array<{ platform?: string; current_price?: number }>;
  atomic_claims?: any[];
};

const pct = (p: number | undefined | null): string =>
  p == null ? '—' : `${Math.round(p * 100)}%`;

const venueLabel = (v: string | undefined): string =>
  v === 'polymarket' ? 'Polymarket' : v === 'kalshi' ? 'Kalshi' : (v ?? '');

const compactUsd = (n: number | undefined | null): string => {
  if (n == null) return '';
  if (n >= 1e9) return `$${(n / 1e9).toFixed(1).replace(/\.0$/, '')}B`;
  if (n >= 1e6) return `$${(n / 1e6).toFixed(1).replace(/\.0$/, '')}M`;
  if (n >= 1e3) return `$${Math.round(n / 1e3)}K`;
  return `$${Math.round(n)}`;
};

// Best-effort deterministic cleanup of an event_question into a fallback title. No model.
// Intentionally conservative: it does NOT try to rewrite a question into a noun phrase
// (that needs the LLM-authored semantic_title) — stripping "Will" produced broken grammar
// ("There be ..."). It only normalizes whitespace and casing, keeping the question intact and
// readable. The backfill / fresh generation replaces this with a real directional title.
export function cleanEventQuestion(q: string | undefined): string {
  if (!q) return '';
  const s = q.replace(/\s+/g, ' ').trim();
  return s.length ? s.charAt(0).toUpperCase() + s.slice(1) : '';
}

// The durable, indexed title. Prefers the authored semantic_title; falls back to a cleaned
// event_question, then to the legacy flat headline as a last resort.
export function displayTitle(data: SignalData): string {
  if (data.semantic_title && data.semantic_title.trim()) return data.semantic_title.trim();
  const cleaned = cleanEventQuestion(data.event_question);
  if (cleaned) return cleaned;
  return data.headline ?? '';
}

// Feed-level dedupe. The generators emit a fresh dated wire for the same persistent market
// (CPI, Fed) every day, so the active feed would accumulate duplicates. Collapse to the NEWEST
// wire per (detection_path + market). The older dated wires still resolve at their own URLs —
// this only affects which wires the active index/homepage/RSS surface (the archive is intact).
// Apply ONLY to feed surfaces, never to the per-wire pages or the for-event discovery list.
type WireEntry = {
  id?: string;
  data: {
    detection_path?: string;
    published_at?: string;
    signal_id?: string;
    primary_market?: { platform_market_id?: string };
  };
};

export function dedupeActiveWires<T extends WireEntry>(entries: T[]): T[] {
  const newest = new Map<string, T>();
  for (const e of entries) {
    // unique market identity → market id; fall back to the wire's own id so nothing falsely collapses
    const mid = e.data.primary_market?.platform_market_id ?? e.data.signal_id ?? e.id ?? '';
    const key = `${e.data.detection_path ?? ''}|${mid}`;
    const cur = newest.get(key);
    if (!cur || (e.data.published_at ?? '') > (cur.data.published_at ?? '')) newest.set(key, e);
  }
  return [...newest.values()];
}

// The muted as-of telemetry track. Prefers the authored telemetry; otherwise composes a
// conservative read from structured primary_market fields. The benchmark anchor (whose unit
// varies — rate level vs probability) is omitted in the fallback to avoid a unit error; the
// Python composer and the backfill set the full string with the correct anchor.
export function composeTelemetry(data: SignalData): string {
  if (data.telemetry && data.telemetry.trim()) return data.telemetry.trim();
  const pm = data.primary_market ?? {};
  switch (data.detection_path) {
    case 'cross_venue_divergence': {
      const rel = (data.related_markets ?? [])[0] ?? {};
      const a = `${venueLabel(pm.platform)} ${pct(pm.current_price)}`;
      const b = rel.platform ? `${venueLabel(rel.platform)} ${pct(rel.current_price)}` : '';
      return b ? `${a} vs ${b}` : a;
    }
    case 'volume_spike': {
      const vol = compactUsd(pm.volume_24h_usd);
      return vol ? `${pct(pm.current_price)} · ${vol} 24h` : pct(pm.current_price);
    }
    case 'news_cycle':
    case 'benchmark_drift':
    default:
      return `${venueLabel(pm.platform)} ${pct(pm.current_price)}`.trim();
  }
}
