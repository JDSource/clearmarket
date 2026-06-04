// Real enriched-universe data source for the /events/ pages.
// Same interface as ./specimens.ts so route swaps are a one-line import change.
// Two adaptations vs the specimen format:
//   1. IDs are now strings (CM-EVT-…, CM-MKT-…) after the 2026-05-27 prefix lock.
//   2. The enrich run produced no marks (marks come from the hourly cron), so we
//      synthesize a current mark per market from its last_price/volume snapshot.
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// -linked is the current bundle: post cross-venue link, with catalyst_types, per-market strike
// fields, and the build-time ladder patch (event_type / ladder_distribution). The old -full bundle
// was pre-link + had none of that, so event pages showed stale data + broken ladders.
const BUNDLE_PATH = resolve(process.cwd(), 'data/universe-enriched-linked.json');

export type Mark = {
  mark_id: string;
  market_id: string;
  snapshot_date: string | null;
  snapshot_at: string;
  source_updated_at: string | null;
  yes_last_price: number | null;
  implied_probability: number | null;
  volume_24h_usd: number | null;
  volume_total_usd: number | null;
  mark_method: string;
  stale_flag: boolean;
  [k: string]: unknown;
};

export type Market = {
  market_id: string;
  platform: 'kalshi' | 'polymarket';
  platform_market_id: string | null;
  event_id: string | null;
  question_raw: string | null;
  description_raw: string | null;
  contract_type: string;
  settlement_currency: string;
  underlying_reference: string | null;
  close_at: string | null;
  resolve_at: string | null;
  status: string;
  resolution_rules_raw: string | null;
  arbitration_model: string | null;
  resolution_proposer: string | null;
  resolution_source: string | null;
  source_citation: string | null;
  source_type: string | null; // mapped from resolution_source_type
  resolution_source_quality: string | null;
  resolution_clarity_grade: string | null;
  rcg_score: number | null;
  rcg_caps: string[];
  rcg_applied_factors: number | null;
  last_price: number | null;
  volume_24h_usd: number | null;
  volume_total_usd: number | null;
  [k: string]: unknown;
};

export type Event = {
  event_id: string;
  slug: string;
  question: string;
  category: string;
  tags: string[];
  primary_market_id: string | null;
  catalyst_dates: { date: string; event: string }[];
  published: boolean;
  editorial_notes: string | null;
  created_at: string;
  updated_at: string;
  venues_covered: ('kalshi' | 'polymarket')[];
  current_primary_mark: Mark | null;
  field_provenance?: Record<string, unknown>;
  rcg_factors?: Record<string, unknown>;
  [k: string]: unknown;
};

type Bundle = { _meta: Record<string, unknown>; events: any[]; markets: any[] };
const bundle = JSON.parse(readFileSync(BUNDLE_PATH, 'utf-8')) as Bundle;
const generatedAt = (bundle._meta?.generated_at as string) ?? new Date().toISOString();

function synthMark(m: any): Mark {
  return {
    mark_id: `synth-${m.market_id}`,
    market_id: m.market_id,
    snapshot_date: null,
    snapshot_at: generatedAt,
    source_updated_at: null,
    yes_last_price: m.last_price ?? null,
    implied_probability: m.last_price ?? null,
    volume_24h_usd: m.volume_24h_usd ?? null,
    volume_total_usd: m.volume_total_usd ?? null,
    mark_method: 'enrich_snapshot',
    stale_flag: false,
  };
}

const allMarkets: Market[] = bundle.markets.map((m) => ({
  ...m,
  source_type: m.resolution_source_type ?? null,
  rcg_caps: m.rcg_caps ?? [],
})) as Market[];

const marketsByEvent = new Map<string, Market[]>();
for (const m of allMarkets) {
  if (!m.event_id) continue;
  const list = marketsByEvent.get(m.event_id);
  if (list) list.push(m);
  else marketsByEvent.set(m.event_id, [m]);
}
const synthMarkByMarketId = new Map<string, Mark>(allMarkets.map((m) => [m.market_id, synthMark(m)]));

const allEvents: Event[] = bundle.events
  .filter((e) => e.published !== false)
  .map((e) => {
    const mkts = marketsByEvent.get(e.event_id) ?? [];
    const venues = Array.from(new Set(mkts.map((m) => m.platform))) as ('kalshi' | 'polymarket')[];
    const primary = e.primary_market_id ? synthMarkByMarketId.get(e.primary_market_id) ?? null : null;
    return {
      ...e,
      tags: e.tags ?? [],
      catalyst_dates: e.catalyst_dates ?? [],
      venues_covered: venues,
      current_primary_mark: primary,
    } as Event;
  });

const eventsBySlug = new Map(allEvents.map((e) => [e.slug, e]));
const eventsById = new Map(allEvents.map((e) => [e.event_id, e]));

// Cross-venue link index: markets sharing a claim_sig are the same claim across venues.
const marketById = new Map<string, Market>(allMarkets.map((m) => [m.market_id, m]));
const marketsBySig = new Map<string, Market[]>();
for (const m of allMarkets) {
  const sig = (m as any).claim_sig as string | null;
  if (!sig) continue;
  const list = marketsBySig.get(sig);
  if (list) list.push(m);
  else marketsBySig.set(sig, [m]);
}

export type CrossVenueLink = {
  market_id: string;
  platform: 'kalshi' | 'polymarket';
  event_slug: string | null;
  question: string | null;
  last_price: number | null;
  grade: string | null;
};

// Twin markets on the OTHER venue that price the same claim as this market.
export function getCrossVenueLinks(market_id: string): CrossVenueLink[] {
  const m = marketById.get(market_id);
  const sig = m ? ((m as any).claim_sig as string | null) : null;
  if (!m || !sig) return [];
  return (marketsBySig.get(sig) ?? [])
    .filter((p) => p.market_id !== market_id && p.platform !== m.platform)
    .map((p) => ({
      market_id: p.market_id,
      platform: p.platform,
      event_slug: eventsById.get(p.event_id ?? '')?.slug ?? null,
      question: p.question_raw ?? null,
      last_price: p.last_price ?? null,
      grade: (p as any).resolution_clarity_grade ?? null,
    }));
}

// Markets sharing a claim_sig = the same canonical claim across venues.
export function getMarketsBySig(sig: string): Market[] {
  return marketsBySig.get(sig) ?? [];
}

// Canonical cross-venue pairs (built by merge_canon.py) — the data-driven /compare set.
export type CanonPair = {
  slug: string; title: string; claim: string; sector: string;
  horizon: string; claim_sig: string; markets: number; clean: boolean; confidence: string;
};
let canonPairs: CanonPair[] = [];
try {
  canonPairs = JSON.parse(readFileSync(resolve(process.cwd(), 'data/canon-pairs.json'), 'utf-8'));
} catch { canonPairs = []; }
export function getCanonPairs(): CanonPair[] {
  return canonPairs;
}

// Resolution log: append-only `resolved` events (built by build_resolution_log.py from the
// price+date snapshot — outcome YES/NO when the final price is extreme, PENDING when the snapshot
// predates settlement). The resolved-history surface for a reference product. Loaded like canon-pairs;
// gracefully empty if the file is absent (e.g. a build before the file is fetched from R2).
export type ResolutionLogEntry = {
  market_id: string;
  event_id: string;
  platform: 'kalshi' | 'polymarket' | string;
  event_type: string;            // 'resolved'
  occurred_at: string;           // when it settled
  recorded_at: string;           // pull date that observed it
  to_value: 'YES' | 'NO' | 'PENDING' | string;
  final_price: number | null;
  source: string;
  source_ref: string;
  actor: string;
};
let resolutionLog: ResolutionLogEntry[] = [];
try {
  resolutionLog = JSON.parse(readFileSync(resolve(process.cwd(), 'data/resolution-log.json'), 'utf-8'));
} catch { resolutionLog = []; }
const resolutionLogByEvent = new Map<string, ResolutionLogEntry[]>();
for (const r of resolutionLog) {
  if (!r.event_id) continue;
  const list = resolutionLogByEvent.get(r.event_id);
  if (list) list.push(r);
  else resolutionLogByEvent.set(r.event_id, [r]);
}

export function getMarkByMarketId(id: string): Mark | undefined {
  return synthMarkByMarketId.get(id);
}

export function getAllEvents(): Event[] {
  return allEvents;
}
export function getEventBySlug(slug: string): Event | undefined {
  return eventsBySlug.get(slug);
}
export function getEventById(id: string): Event | undefined {
  return eventsById.get(id);
}
export function getMarketsForEvent(event_id: string): Market[] {
  return marketsByEvent.get(event_id) ?? [];
}
export function getMarksForEvent(event_id: string): Mark[] {
  return getMarketsForEvent(event_id)
    .map((m) => synthMarkByMarketId.get(m.market_id))
    .filter((x): x is Mark => Boolean(x));
}
// Resolved-market history for an event, newest settlement first.
export function getResolutionLogForEvent(event_id: string): ResolutionLogEntry[] {
  return (resolutionLogByEvent.get(event_id) ?? [])
    .slice()
    .sort((a, b) => (b.occurred_at ?? '').localeCompare(a.occurred_at ?? ''));
}

// Build-date "today" — the static site rebuilds daily (CM Signal cron), so this re-filters daily.
const TODAY_ISO = new Date().toISOString().slice(0, 10);
// An event is LIVE if at least one of its markets still resolves today or later. Multi-date series
// (e.g. "Bitcoin ATH by Mar / Jun / Sep / Dec") stay live until the final leg resolves; a fully-
// resolved event drops out of the active index + search (still reachable by URL as a record).
export function isEventLive(event: Event): boolean {
  const mk = getMarketsForEvent(event.event_id);
  if (!mk.length) return false;
  return mk.some((m) => {
    const d = (m.resolve_at ?? (m as any).close_at ?? '').slice(0, 10);
    return !d || d >= TODAY_ISO; // missing date → keep (never hide on absent data)
  });
}
export function getActiveEvents(): Event[] {
  return allEvents.filter(isEventLive);
}

export const SPECIMEN_GENERATED_AT = generatedAt;
export const SCHEMA_VERSION = (bundle._meta?.schema as string) ?? 'v0.2.0';
