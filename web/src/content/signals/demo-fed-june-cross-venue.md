---
signal_id: "CMSIGDEMO00002"
signal_slug: "demo-fed-june-cross-venue"
headline: "Polymarket and Kalshi diverge sharply on Fed June rate cut"
category_tag: "CROSS_VENUE_DIVERGENCE"
secondary_tags: ["VS_BENCHMARK_DRIFT"]
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-05-22T09:30:00-04:00"
event_id: "CMFEDJUN25C1"
event_slug: "fed-june-2026-25bp-cut"
event_question: "Will the Fed cut rates by 25bp at the June 2026 FOMC meeting?"
linked_event_ids: ["CMCYQ4MMGJN4"]
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfedjun2026"
  question_raw: "Fed cuts 25bp at June 2026 meeting"
  current_price: 0.41
  price_24h_ago: 0.38
  volume_24h_usd: 2400000
  volume_7d_usd: 11200000
  volume_cumulative_usd: 18600000
  arbitration_model: "uma_oracle"
  resolution_source: "Federal Reserve Board press release"
  resolves_at: "2026-06-17T18:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXFED-26JUN-CUT25"
    question_raw: "Fed cuts 25bp at June 2026 FOMC"
    current_price: 0.32
bullets:
  - "Polymarket and Kalshi are pricing the June Fed decision differently, with the spread between the two venues at its widest level in a month."
  - "Polymarket traders put the odds of a 25bp cut at 41%. Kalshi traders put it at 32%. The 9-point gap has only been seen four times in the past 30 days, all clustered after the May 7 Fed meeting."
  - "Volume favors Polymarket's read: $2.4 million of 24-hour trading versus Kalshi's $0.9 million."
  - "May 28 brings the next test, when April CPI prints. The FOMC itself is 26 days out — past the typical window for cross-venue spreads to converge on their own."
  - "One reason for the gap: Polymarket's international traders historically react harder to Fed-speaker remarks than Kalshi's US-onshore base."
atomic_claims:
  - type: "cross_venue_spread"
    significance:
      threshold: 5.0
      threshold_unit: "pp"
      current: 9.0
      passed: true
      percentile_30d: 96
      reason: "spread exceeded 5pp detection threshold; widest in 30 days (prior max 7.2pp on 2026-05-04)"
    spread_pp: 9.0
    threshold_pp: 5.0
    percentile_30d: 96
    prior_max_pp: 7.2
    prior_max_date: "2026-05-04"
    days_above_threshold_30d: 4
    field_provenance:
      spread_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["primary_market.current_price (polymarket)", "related_markets[0].current_price (kalshi)"]
        note: "abs(poly_price - kalshi_price) at t=now"
      percentile_30d:
        tier: "derived"
        method: "rank_in_cm_marks_history"
        inputs: ["spread_pp", "cm_marks_history (30d window)"]
        note: "current spread_pp vs all observed spreads in trailing 30d"
      prior_max_pp:
        tier: "derived"
        method: "max_in_cm_marks_history"
        inputs: ["cm_marks_history (30d window)"]
        note: "max observed spread_pp in trailing 30d"
  - type: "divergence_context"
    poly_vol_24h_usd: 2400000
    kalshi_vol_24h_usd: 890000
    volume_ratio: 2.7
    next_catalyst:
      type: "cpi"
      date: "2026-05-28"
      days_out: 6
    fomc_date: "2026-06-17"
    fomc_days_out: 26
    audience_note: "Polymarket international base reacts more sharply to Fed-speaker remarks than Kalshi's CFTC-eligible US base"
    field_provenance:
      poly_vol_24h_usd:
        tier: "direct"
        method: "polymarket_clob_api"
        retrieved_at: "2026-05-22T09:30:00-04:00"
      kalshi_vol_24h_usd:
        tier: "direct"
        method: "kalshi_api"
        retrieved_at: "2026-05-22T09:30:00-04:00"
      next_catalyst:
        tier: "direct"
        method: "bls_release_calendar"
        source: "BLS schedule"
        source_url: "https://www.bls.gov/schedule/news_release/cpi.htm"
      audience_note:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CME FedWatch tool"
    url: "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
    retrieved_at: "2026-05-22T09:00:00-04:00"
field_provenance:
  pm_data: "polymarket_clob_api, kalshi_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

Cross-venue spread on the Fed June 25bp-cut question. Both venues are inside the FedWatch envelope but on opposite sides — sentiment-population signal rather than directional bet.
</content>
</invoke>