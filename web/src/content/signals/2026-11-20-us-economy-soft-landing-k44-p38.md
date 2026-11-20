---
signal_id: "CMSIG20261120DV00"
signal_slug: "us-economy-soft-landing-k44-p38"
headline: "Economy at end-2026: Kalshi 44% vs Polymarket 38%"
semantic_title: "End-2026 economy outlook prices higher on one major desk"
telemetry: "Polymarket 38% vs Kalshi 44%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-20T07:48:05+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.385
  volume_cumulative_usd: 66300.424357
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.44
bullets:
  - "Kalshi prices this 6pp above Polymarket, a meaningful spread on a macro sentiment claim."
  - "Kalshi sits at the higher mark with roughly half the liquidity of Polymarket's deeper book."
  - "Thinner Kalshi volume may reflect a more optimistic niche audience; Polymarket's larger pool likely carries more weight."
  - "Resolution depends on an agreed economic benchmark, ambiguity in the claim definition may itself be driving the gap."
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
      kalshi_vol_24h_usd: 24.75
      poly_vol_24h_usd: 40.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-11-20T07:48:05+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp spread on a loosely worded macro claim suggests resolution ambiguity is the primary driver, and a desk should treat the Polymarket print as the more credible reference given its deeper cumulative volume.
