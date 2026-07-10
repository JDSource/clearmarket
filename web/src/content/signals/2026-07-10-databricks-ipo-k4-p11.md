---
signal_id: "CMSIG20260710DV03"
signal_slug: "databricks-ipo-k4-p11"
headline: "Databricks IPO before 2027: Kalshi 4% vs Polymarket 11%"
semantic_title: "Databricks IPO odds bridge unevenly across venues"
telemetry: "Polymarket 11% vs Kalshi 4%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-10T10:50:52+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.11
  volume_cumulative_usd: 482833.9704749999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.04
bullets:
  - "Polymarket prices 11%, Kalshi 4%, a 7pp gap with Polymarket the higher venue."
  - "Polymarket dominates volume by more than 56-to-1; Kalshi's print reflects a very thin book."
  - "Kalshi's near-zero price may simply reflect insufficient participants to move the market off a floor."
  - "Resolves YES on Databricks pricing or first trading day before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 26.8
      poly_vol_24h_usd: 443.5
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-10T10:50:52+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Kalshi's illiquidity likely explains the entire gap here; a desk should treat the Polymarket figure as the operative probability and monitor for any S-1 catalyst.
