---
signal_id: "CMSIG20260809DV01"
signal_slug: "us-economy-soft-landing-k62-p54"
headline: "U.S. economy state end-2026: Kalshi 62% vs Polymarket 54%"
semantic_title: "Economy-in-recession odds carry a premium on the low-liquidity desk"
telemetry: "Polymarket 54% vs Kalshi 62%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-09T08:38:03+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.54
  volume_cumulative_usd: 30678.147992999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.62
bullets:
  - "Kalshi prices the pessimistic outcome at 62%, Polymarket at 54%, an 8pp gap"
  - "Kalshi is the higher venue; volume stands at $12K vs $31K, both relatively thin"
  - "Ambiguous resolution criteria across platforms may explain the gap; contract wording differences likely drive divergence more than information asymmetry"
  - "Resolves based on defined economic-state criteria at end of calendar year 2026"
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
      kalshi_vol_24h_usd: 23.74
      poly_vol_24h_usd: 159.4
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-09T08:38:03+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 8pp spread on a subjectively defined macro claim signals that contract specification differences, not genuine probability disagreement, are the likely culprit, desks should verify resolution rules before acting on the gap.
