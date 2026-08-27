---
signal_id: "CMSIG20260827DV00"
signal_slug: "us-economy-soft-landing-k55-p61"
headline: "State of economy end-2026: Kalshi 55% vs Polymarket 61%"
semantic_title: "Economy-end-2026 outlook carries a premium across venues"
telemetry: "Polymarket 61% vs Kalshi 55%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-27T18:47:54+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.61
  volume_cumulative_usd: 33425.225934
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.551
bullets:
  - "Polymarket prices this 6pp higher than Kalshi, 61% vs 55%, a meaningful spread on a soft macro call."
  - "Polymarket is the higher-priced venue with roughly three times the cumulative volume behind it."
  - "Thinner liquidity on Kalshi may reflect ambiguity in the resolution criteria for a qualitative 'state of economy' claim."
  - "Resolution likely hinges on a designated index, panel, or editorial call, subjective definitions can drive venue-level disagreement."
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
      kalshi_vol_24h_usd: 2.76
      poly_vol_24h_usd: 9.2
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-27T18:47:54+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a qualitative macro claim suggests desks should scrutinize the exact resolution oracle before leaning on either price as a reliable signal.
