import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const SAMPLES_DIR = resolve(here, '../../../samples');
const SPECIMEN_NAMES = ['fed-apr-2026', 'fed-apr-2026-settled', 'iran', 'netanyahu', 'sp500-2026'] as const;

export type Mark = {
  mark_id: number;
  market_id: number;
  snapshot_date: string;
  snapshot_at: string;
  source_updated_at: string;
  yes_bid: number | null;
  yes_ask: number | null;
  no_bid: number | null;
  no_ask: number | null;
  yes_bid_size_usd: number | null;
  yes_ask_size_usd: number | null;
  no_bid_size_usd: number | null;
  no_ask_size_usd: number | null;
  yes_last_price: number | null;
  implied_probability: number | null;
  volume_24h_usd: number | null;
  volume_total_usd: number | null;
  open_interest_usd: number | null;
  mark_method: string;
  stale_flag: boolean;
  source_count: number;
  spread: number | null;
  mid: number | null;
  divergence_from_primary: number | null;
  hours_since_source_update: number | null;
  field_provenance?: Record<string, unknown>;
};

export type Market = {
  market_id: number;
  platform: 'kalshi' | 'polymarket';
  platform_market_id: string;
  event_id: string | null;
  platform_event_id: string | null;
  question_raw: string | null;
  description_raw: string | null;
  category_raw: string | null;
  contract_type: 'binary' | 'scalar';
  settlement_currency: 'USD' | 'USDC';
  tick_size: number | null;
  contract_multiplier: number | null;
  underlying_reference: string | null;
  close_at: string | null;
  last_trading_date: string | null;
  resolve_at: string | null;
  status: 'open' | 'closed' | 'resolved' | 'amended';
  resolution_rules_raw: string | null;
  resolution_triggers: unknown;
  arbitration_model: string | null;
  resolution_proposer: string | null;
  resolution_source: string | null;
  source_citation: string | null;
  source_type: string | null;
  regulatory_class: 'DCM' | 'DeFi' | 'Other' | null;
  analyst_notes: string | null;
  contract_terms_url: string | null;
  resolution_outcome: string | null;
  resolution_value: number | null;
  resolved_at: string | null;
  first_seen_at: string;
  last_updated_at: string;
  cross_platform_link?: { kalshi: { market_count: number }; polymarket: { market_count: number } } | null;
  field_provenance?: Record<string, unknown>;
};

export type ResolutionLogEntry = {
  log_id: number;
  market_id: number;
  event_type: string;
  occurred_at: string;
  recorded_at: string;
  from_value: string | null;
  to_value: string | null;
  diff: unknown;
  source: string;
  source_ref: string | null;
  actor: string | null;
};

export type Event = {
  event_id: string;
  slug: string;
  question: string;
  category: 'macro' | 'geopolitics' | 'politics' | 'crypto' | 'sports';
  tags: string[];
  primary_market_id: number | null;
  primary_market_locked: boolean;
  catalyst_dates: { date: string; event: string; type?: string | null; source_url?: string | null; verified_at?: string | null }[];
  published: boolean;
  editorial_notes: string | null;
  resolution_headline?: string | null;
  created_at: string;
  updated_at: string;
  venues_covered: ('kalshi' | 'polymarket')[];
  current_primary_mark: Mark | null;
  field_provenance?: Record<string, unknown>;
};

type Specimen = {
  _meta: Record<string, unknown>;
  events: Event[];
  markets: Market[];
  marks: Mark[];
  resolution_log: ResolutionLogEntry[];
};

function loadSpecimen(name: string): Specimen {
  const path = resolve(SAMPLES_DIR, name, 'specimen.json');
  return JSON.parse(readFileSync(path, 'utf-8')) as Specimen;
}

const specimens: Specimen[] = SPECIMEN_NAMES.map(loadSpecimen);

const allEvents: Event[] = specimens.flatMap((s) => s.events).filter((e) => e.published);
const allMarkets: Market[] = specimens.flatMap((s) => s.markets);
const allMarks: Mark[] = specimens.flatMap((s) => s.marks);
const allResolutionLog: ResolutionLogEntry[] = specimens.flatMap((s) => s.resolution_log);

const eventsBySlug = new Map(allEvents.map((e) => [e.slug, e]));
const eventsById = new Map(allEvents.map((e) => [e.event_id, e]));

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
  return allMarkets.filter((m) => m.event_id === event_id);
}

export function getMarksForEvent(event_id: string): Mark[] {
  const marketIds = new Set(getMarketsForEvent(event_id).map((m) => m.market_id));
  return allMarks.filter((m) => marketIds.has(m.market_id));
}

export function getResolutionLogForEvent(event_id: string): ResolutionLogEntry[] {
  const marketIds = new Set(getMarketsForEvent(event_id).map((m) => m.market_id));
  return allResolutionLog.filter((r) => marketIds.has(r.market_id));
}

export const SPECIMEN_GENERATED_AT = (specimens[0]._meta?.generated_at as string) ?? null;
export const SCHEMA_VERSION = (specimens[0]._meta?.schema_version as string) ?? 'v0.1.0';
