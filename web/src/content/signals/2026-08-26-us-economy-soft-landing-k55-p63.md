---
signal_id: "CMSIG20260826DV00"
signal_slug: "us-economy-soft-landing-k55-p63"
headline: "State of economy end-2026: Kalshi 55% vs Polymarket 63%"
semantic_title: "Economy-end-2026 outlook carries a premium across venues"
telemetry: "Polymarket 63% vs Kalshi 55%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-26T08:38:56+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.63
  volume_cumulative_usd: 33411.025934
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.551
bullets:
  - "Polymarket prices the positive outcome at 63%, Kalshi at 55%, an 8pp spread."
  - "Polymarket sits higher with significantly deeper liquidity; Kalshi volume is thin by comparison."
  - "Vague resolution language likely drives the gap, 'state of economy' leaves room for subjective calls, and deeper-liquid venues often converge on more cautious reads."
  - "Resolution depends on which economic indicators or editorial criteria the market operator designates at year-end."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
    field_provenance:
      kalshi_price:
        tier: "direct"
        method: "kalshi_api"
      poly_price:
        tier: "direct"
        method: "polymarket_clob_api"
      divergence_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["kalshi_price", "poly_price"]
    liquidity_context:
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 244.48315600000004
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-26T08:38:56+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp spread on a subjectively worded claim signals that a desk should treat both prices as noisy until the resolution criteria are published and standardized.
