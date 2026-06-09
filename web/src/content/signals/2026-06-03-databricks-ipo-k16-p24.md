---
signal_id: "CMSIG20260603DV00"
signal_slug: "databricks-ipo-k16-p24"
headline: "Databricks IPO before 2027: Polymarket 24% vs Kalshi 16%"
semantic_title: "Databricks IPO before 2027 decouples sharply across venues"
telemetry: "Polymarket 24% vs Kalshi 16%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-03T01:49:11+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.24
  volume_cumulative_usd: 470617.8689989999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.16
bullets:
  - "Polymarket prices 24%, Kalshi 16%, an 8pp gap on the same end-2026 horizon."
  - "Polymarket is higher; cumulative volume $470,618 vs Kalshi's thin $30,053."
  - "Kalshi's shallow book likely reflects fewer informed participants; Polymarket price carries more weight given ~16x liquidity advantage."
  - "Resolves YES only if Databricks completes an IPO on a public exchange before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 7.86
      poly_vol_24h_usd: 216.95000000000002
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-03T01:49:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp spread with a 15x liquidity imbalance suggests Kalshi's 16% is noise-driven and Polymarket's 24% is the more reliable consensus estimate for a Databricks 2026 IPO.
