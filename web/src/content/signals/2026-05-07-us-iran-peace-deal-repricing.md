---
signal_id: "CMSIG2026050700001"
signal_slug: "us-iran-peace-deal-repricing-2026-05-07"
headline: "Polymarket odds of US-Iran peace deal jump on proposal reports"
category_tag: "MOMENTUM_REPRICING"
secondary_tags: ["COVERAGE_GAP"]
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-07T20:35:00-04:00"
event_id: "CMI3R4N4P5C1"
event_slug: "us-iran-peace-deal-may-2026"
event_question: "Will the US and Iran sign a permanent peace deal by May 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa1b2c3d4e5"
  question_raw: "US × Iran permanent peace deal by May 31, 2026"
  current_price: 0.345
  price_24h_ago: 0.285
  volume_24h_usd: 2940000
  volume_7d_usd: 7710000
  volume_cumulative_usd: 16780000
  arbitration_model: "uma_oracle"
  resolution_source: "Credible news reporting"
  resolves_at: "2026-05-31T23:59:59Z"
related_markets: []
bullets:
  - "Polymarket traders are pricing higher odds of a US-Iran peace deal by month-end, after a week of escalating diplomatic signals."
  - "The contract trades at 34.5%, up from 18.5% on April 30 — a 16-point move in seven days, with 6 of those points coming in the last 24 hours."
  - "The repricing followed three signals: Trump told reporters a deal is \"very possible,\" the State Department confirmed a US proposal for a 20-year uranium enrichment ban, and Iran's foreign ministry acknowledged receipt."
  - "Volume on the contract reached $2.94 million over 24 hours and $7.71 million for the week, making it one of Polymarket's most actively traded geopolitical positions."
  - "Kalshi has no equivalent contract — CFTC political-event restrictions leave Polymarket as the only liquid prediction-market read on the proposal phase. The deal would need to be signed by May 31 to resolve YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      current: 2
      passed: true
      reason: "story ranked #2 in daily Perplexity top-stories scan; mechanically matched to active Polymarket contract"
    story: "Trump signals US-Iran proposal openness; Iran foreign ministry confirms receipt of US demand for 20-year uranium enrichment ban"
    publisher: "Reuters / Bloomberg / WSJ (multi-source)"
    published_at: "2026-05-07T15:42:00Z"
    source_url: "https://www.reuters.com/world/middle-east/us-iran-talks-may-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "perplexity_grounded"
        source: "Reuters / Bloomberg / WSJ"
        retrieved_at: "2026-05-07T20:00:00-04:00"
      source_url:
        tier: "mediated"
        method: "perplexity_grounded"
        source: "Reuters"
        source_url: "https://www.reuters.com/world/middle-east/us-iran-talks-may-2026"
        retrieved_at: "2026-05-07T20:00:00-04:00"
  - type: "pm_response"
    poly_price_change_pp: 6.0
    lead_lag_minutes_poly: -42
    liquidity_context:
      poly_vol_24h_usd: 2940000
      poly_vol_7d_usd: 7710000
      poly_open_interest_usd: 16780000
    notes: "Polymarket sole liquid venue — CFTC political-event restrictions block Kalshi listing. Repricing path: 18.5% (Apr 30) → 28.5% (May 6) → 34.5% (May 7). Cumulative +16pp over 7 days on $7.71M volume. 24h move began ~42 minutes before peak Reuters headline crossed the wire."
    field_provenance:
      poly_price_change_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["cm_marks_history (price series for this contract, 24h window from story_published_at)"]
        note: "price_at(story_published_at + 24h) - price_at(story_published_at)"
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Polymarket — US × Iran peace deal contract"
    url: "https://polymarket.com/event/us-iran-peace-deal-2026"
    retrieved_at: "2026-05-07T20:30:00-04:00"
  - label: "Reuters — US-Iran proposal coverage"
    url: "https://www.reuters.com/world/middle-east/us-iran-talks-may-2026"
    retrieved_at: "2026-05-07T20:30:00-04:00"
field_provenance:
  pm_data: "polymarket_clob_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "none (deterministic news-cycle scan)"
---

Surfaced by the daily 04:00 ET news-cycle scan: US-Iran diplomatic developments were one of the day's top stories, and Polymarket's US-Iran peace deal contract was the liquid prediction-market expression. No judge gate — news-cycle wires publish on coverage, not editorial selection.
