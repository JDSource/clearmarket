---
signal_id: "CMSIG20261005DV01"
signal_slug: "us-economy-soft-landing-k32-p27"
headline: "Economy state end of 2026 'good/great': Kalshi 33% vs Polymarket 27%"
semantic_title: "End-of-2026 economy outlook builds a premium on Kalshi"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-05T16:45:44+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47047.88071300001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.329
bullets:
  - "Kalshi prices a positive economy outcome at 33%, Polymarket at 27%, a 6pp spread"
  - "Kalshi is the higher-priced venue; Polymarket holds roughly twice Kalshi's cumulative volume on this claim"
  - "Audience and resolution-criteria differences likely drive the gap, subjective economy grading leaves room for platform-specific interpretations to diverge"
  - "Resolves based on an agreed assessment of U.S. economic conditions at end of 2026"
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
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-05T16:45:44+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp divergence on a subjectively graded macro claim signals that resolution-criteria ambiguity is doing most of the work, desks should reconcile each venue's exact resolution rules before treating either price as a clean probability read.
