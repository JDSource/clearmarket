---
signal_id: "CMSIG20260707DV03"
signal_slug: "databricks-ipo-k8-p18"
headline: "Databricks IPO before 2027: Kalshi 8% vs Polymarket 18%"
semantic_title: "Databricks IPO market fragments, venues tracking opposite ends"
telemetry: "Polymarket 18% vs Kalshi 8%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-07T10:53:30+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.18
  volume_cumulative_usd: 480639.517923
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.08
bullets:
  - "Kalshi at 8%, Polymarket at 18%, a 10pp gap, Polymarket the higher venue."
  - "Polymarket is higher and holds roughly 28x the cumulative volume of Kalshi's book."
  - "Polymarket's better-capitalized crowd likely tracking Databricks' active financing rounds and IPO chatter; Kalshi may lag on information."
  - "Resolves YES if Databricks prices or completes a public offering before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 54.37
      poly_vol_24h_usd: 68.134145
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-07T10:53:30+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket running at more than double Kalshi's probability on 28x the volume, a desk should weight the higher price as the informed consensus and treat Kalshi's 8% as stale or data-poor.
