import { defineCollection, z } from 'astro:content';

const signals = defineCollection({
  type: 'content',
  schema: z.object({
    signal_id: z.string(),
    signal_slug: z.string(),
    // Legacy flat title — KEPT for backward compat (RSS/.json consumers, the 54 pre-refactor
    // wires). No longer the source for <title>/<h1>/JSON-LD. Title now splits into two fields:
    headline: z.string(),
    // semantic_title (LLM-authored) — durable, directional, symbol-free narrative anchor.
    // Maps to <title>, <h1>, JSON-LD name/claimReviewed. Optional so pre-refactor wires build;
    // renderers fall back to a cleaned event_question via displayTitle() (lib/signal-display.ts).
    semantic_title: z.string().max(90).optional(),
    // telemetry (Python-composed, NEVER LLM) — terse as-of read (e.g. "Kalshi 76% vs Polymarket 70%").
    // Rendered as a muted track after the title. Optional; falls back to composeTelemetry() over
    // primary_market fields for pre-refactor wires.
    telemetry: z.string().optional(),
    category_tag: z.enum([
      'MOMENTUM_REPRICING',
      'CROSS_VENUE_DIVERGENCE',
      'COVERAGE_GAP',
      'PRE_EVENT_PRICING',
      'VS_BENCHMARK_DRIFT',
      'RESOLUTION_DISPUTED',
      'VOLUME_SPIKE',
      'NEW_LISTING',
    ]),
    secondary_tags: z.array(z.string()).optional(),
    detection_path: z.enum([
      'news_cycle',
      'benchmark_drift',
      'cross_venue_divergence',
      'volume_spike',
    ]),
    pre_news_classification: z.enum(['pre_news', 'concurrent', 'lagging']),
    published_at: z.string(),
    // Accepts the real prefixed ids (CM-EVT-XXXXXXXX, locked 2026-05-27) and the older
    // compact demo ids (CMI3R4N4P5C1). Was /^CM[0-9A-Z]{10}$/ which rejected real ids.
    event_id: z.string().regex(/^CM[-0-9A-Z]+$/),
    event_slug: z.string(),
    event_question: z.string(),
    linked_event_ids: z.array(z.string()).optional(),
    primary_market: z.object({
      platform: z.enum(['kalshi', 'polymarket']),
      platform_market_id: z.string(),
      question_raw: z.string(),
      current_price: z.number(),
      price_24h_ago: z.number().optional(),
      volume_24h_usd: z.number().optional(),
      volume_7d_usd: z.number().optional(),
      volume_cumulative_usd: z.number().optional(),
      arbitration_model: z.string().nullable().optional(),
      resolution_source: z.string().nullable().optional(),
      resolves_at: z.string().optional(),
    }),
    related_markets: z.array(z.object({
      platform: z.enum(['kalshi', 'polymarket']),
      platform_market_id: z.string(),
      question_raw: z.string(),
      current_price: z.number().optional(),
    })).optional(),
    bullets: z.array(z.string()).min(3).max(5),
    atomic_claims: z.array(z.object({
      type: z.enum([
        // Cross-venue divergence wire — cross_venue_divergence detection path
        'cross_venue_spread',
        'divergence_context',
        // Benchmark-drift wire — benchmark_drift detection path
        'benchmark_divergence',
        'benchmark_context',
        // News-cycle wire — news_cycle detection path
        'news_event',
        'pm_response',
        // Volume-spike wire — volume_spike detection path
        'volume_anomaly',
        'volume_context',
      ]),
      provenance: z.string().optional(),
      // Per-field provenance map (locked 2026-05-23). Each field name in this object
      // points at a structured provenance entry. The legacy single-string `provenance`
      // field above is kept optional for backward compat with older specimens.
      field_provenance: z.record(z.object({
        tier: z.enum(['direct', 'mediated', 'derived', 'editorial']),
        method: z.string(),
        source: z.string().optional(),
        source_url: z.string().url().optional(),
        retrieved_at: z.string().optional(),
        note: z.string().optional(),
        // For derived values: the list of upstream field names this value depends on.
        // Lets AI agents trace dependencies mechanically without NLP-parsing the note.
        // Example: pm_consensus_24h_vw has inputs=['poly_price', 'kalshi_price'].
        inputs: z.array(z.string()).optional(),
      })).optional(),
      // Liquidity context — exposed on claims that assert price-related metrics so
      // consumers can judge "is this a real signal or noise?" A 16pp price move on
      // $5K of volume is noise; the same move on $5M is a signal. Without this block,
      // the price-move claim is unverifiable without scrolling to the wire envelope.
      liquidity_context: z.object({
        poly_vol_24h_usd: z.number().optional(),
        kalshi_vol_24h_usd: z.number().optional(),
        poly_vol_7d_usd: z.number().optional(),
        kalshi_vol_7d_usd: z.number().optional(),
        poly_open_interest_usd: z.number().optional(),
        kalshi_open_interest_usd: z.number().optional(),
        depth_to_100bp_usd: z.number().optional(),
      }).optional(),
      // Uniform significance block — tells the machine "why this wire crossed the bar."
      // Populated on MAIN claims (cross_venue_spread, benchmark_divergence, news_event,
      // volume_anomaly) but NOT on context claims (which are explanatory, not triggers).
      // Required field is `reason` — even when there's no numerical threshold (news_event
      // doesn't have one; the threshold is "made the daily top-N stories").
      significance: z.object({
        threshold: z.number().optional(),
        threshold_unit: z.string().optional(),   // 'pp', 'x', 'rank', 'ratio', 'count', 'pct'
        current: z.number().optional(),          // observed value being compared to threshold
        passed: z.boolean().optional(),          // current crossed threshold yes/no
        percentile_30d: z.number().optional(),   // rank within trailing 30-day distribution
        reason: z.string(),                      // 1-line plain-English explanation
      }).optional(),
      // Bucket A: cross_venue_spread
      spread_pp: z.number().optional(),
      threshold_pp: z.number().optional(),
      percentile_30d: z.number().optional(),
      prior_max_pp: z.number().optional(),
      prior_max_date: z.string().optional(),
      days_above_threshold_30d: z.number().optional(),
      // Bucket A: divergence_context
      poly_vol_24h_usd: z.number().optional(),
      kalshi_vol_24h_usd: z.number().optional(),
      volume_ratio: z.number().optional(),
      next_catalyst: z.object({
        type: z.string(),
        date: z.string(),
        days_out: z.number(),
      }).passthrough().optional(),
      fomc_date: z.string().optional(),
      fomc_days_out: z.number().optional(),
      audience_note: z.string().optional(),
      // Benchmark-drift wire: benchmark_divergence (renamed from benchmark_wedge 2026-05-23)
      poly_price: z.number().optional(),
      kalshi_price: z.number().optional(),
      pm_consensus_24h_vw: z.number().optional(),
      benchmark_source: z.string().optional(),
      benchmark_source_url: z.string().url().optional(),
      benchmark_value: z.number().optional(),
      benchmark_retrieved_at: z.string().optional(),
      divergence_pp: z.number().optional(),
      // Benchmark-drift wire: benchmark_context (renamed from wedge_context 2026-05-23)
      corr_30d_poly: z.number().optional(),
      corr_30d_kalshi: z.number().optional(),
      corr_breakpoint_date: z.string().optional(),
      poly_offset_pp: z.number().optional(),
      kalshi_offset_pp: z.number().optional(),
      interp: z.string().optional(),
      // Bucket C: news_event
      story: z.string().optional(),
      publisher: z.string().optional(),
      published_at: z.string().optional(),
      source_url: z.string().optional(),
      // Bucket C: pm_response
      poly_price_change_pp: z.number().optional(),
      kalshi_price_change_pp: z.number().optional(),
      lead_lag_minutes_poly: z.number().optional(),
      lead_lag_minutes_kalshi: z.number().optional(),
      notes: z.string().optional(),
      // Volume-spike: volume_anomaly
      current_vol_24h_usd: z.number().optional(),
      baseline_vol_7d_avg_usd: z.number().optional(),
      volume_ratio_vs_baseline: z.number().optional(),
      prior_max_ratio_30d: z.number().optional(),
      prior_max_ratio_date: z.string().optional(),
      // Volume-spike: volume_context
      venue: z.enum(['polymarket', 'kalshi', 'both']).optional(),
      price_change_during_spike_pp: z.number().optional(),
      associated_catalyst: z.string().optional(),
    })).optional(),
    judge_confidence: z.number().min(0).max(1).optional(),
    prompt_template: z.string().optional(),
    // REQUIRED, min 1 (locked 2026-05-26 per Jeremy). Every wire item cites at least
    // one source — provenance is the defensible layer, so a sourceless wire is not
    // publishable. For pure-mechanical wires (cross_venue_divergence, volume_spike) the
    // source is the venue market URL(s); for news/benchmark wires it is the underlying
    // article / benchmark deep link. Deep-link enforced 2026-07-14 (was a follow-up refine):
    // a domain root is provenance theater — an agent following it cannot verify the claim.
    sources: z.array(z.object({
      label: z.string(),
      url: z.string().url().refine((u) => {
        try { const p = new URL(u); return (p.pathname !== '' && p.pathname !== '/') || p.search.length > 0; }
        catch { return false; }
      }, 'source url must be a deep link (path or query), not a domain root'),
      // Article's own publish date (e.g. Exa `publishedDate`). Distinct from retrieved_at:
      // published_at = when the source was published; retrieved_at = when CM fetched it.
      // Added 2026-05-25 — enabled by retrieval-first stack returning per-result publish dates.
      published_at: z.string().optional(),
      retrieved_at: z.string().optional(),
    })).min(1, 'every wire item must cite at least one source'),
    field_provenance: z.object({
      pm_data: z.string().default('platform_api'),
      // Name the actual retriever in specimens: 'exa_search' / 'claude_web_search' /
      // 'negative_scan'. Default generalized off 'perplexity_grounded' 2026-05-25.
      news_context: z.string().default('retrieval_grounded'),
      editorial_judgment: z.string().default('cm_signal_llm_judge'),
    }).optional(),
    // Negative-scan provenance (added 2026-05-25). For pre-news / coverage-gap signals
    // whose FINDING is the absence of news, the provenance is the scan itself — there is
    // no source_url or published_at to cite because there is no article. This block makes
    // the negative machine-readable and reproducible (query + sources + window + null result),
    // and flows into JSON-LD + the parallel .json so a crawler reads the same negative a human does.
    scan_record: z.object({
      engine: z.string(),                            // retriever used, e.g. 'exa_search', 'claude_web_search'
      query: z.string(),                             // exact query run
      sources_checked: z.array(z.string()).min(1),   // outlets / feeds scanned
      window_start: z.string(),                      // ISO date — start of scanned window
      window_end: z.string(),                        // ISO date — end of scanned window
      scanned_at: z.string(),                        // ISO timestamp of the scan
      result: z.enum(['no_match', 'match']),         // outcome; 'no_match' = confirmed negative
      match_count: z.number().int().min(0),          // 0 for a true negative
    }).optional(),
  }),
});

export const collections = {
  signals,
};
