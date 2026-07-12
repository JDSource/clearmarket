---
signal_id: "CMSIG20260712DV02"
signal_slug: "databricks-ipo-k6-p13"
headline: "Databricks IPO before 2027: Kalshi 6% vs Polymarket 13%"
semantic_title: "Databricks IPO-before-2027 decouples, lower on the smaller desk"
telemetry: "Polymarket 13% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-12T09:49:02+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.13
  volume_cumulative_usd: 482926.7804749999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.06
bullets:
  - "Polymarket prices Databricks IPO before 2027 at 13%; Kalshi at 6%, a 7pp gap."
  - "Polymarket is the higher-side venue with roughly 37x Kalshi's cumulative volume."
  - "Deep Polymarket liquidity lending credibility to the 13% read; Kalshi's thin book may be lagging public information."
  - "Resolves YES if Databricks lists publicly on a major exchange before January 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-EBC7EEEA61); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 5.52
      poly_vol_24h_usd: 31.75
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-12T09:49:02+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Unusually, the deeper venue holds the higher price here, a desk should treat the Polymarket 13% as better-informed and flag the Kalshi 6% as a potential stale or liquidity-constrained print.
