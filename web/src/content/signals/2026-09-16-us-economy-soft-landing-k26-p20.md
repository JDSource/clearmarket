---
signal_id: "CMSIG20260916DV02"
signal_slug: "us-economy-soft-landing-k26-p20"
headline: "Economy in recession end-2026: Kalshi 27% vs Polymarket 20%"
semantic_title: "Recession-scenario odds diverge across venues into year-end"
telemetry: "Polymarket 20% vs Kalshi 27%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-16T13:04:24+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.2
  volume_cumulative_usd: 39716.387087999996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.267
bullets:
  - "Kalshi marks a recessionary economy outcome at 27%, Polymarket at 20%, a 7pp gap"
  - "Kalshi is the higher-priced venue; Polymarket holds roughly 6x the cumulative volume"
  - "Resolution ambiguity is likely central: each platform may apply a different definition of 'recession' at end of 2026"
  - "Definitional differences in resolution criteria are the key wedge a desk must resolve before trading the spread"
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
      kalshi_vol_24h_usd: 74.91
      poly_vol_24h_usd: 635.23487
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-16T13:04:24+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap likely reflects definitional divergence in how each venue specifies recession criteria rather than genuine probability disagreement, a desk must reconcile resolution language before treating this as a clean arb.
