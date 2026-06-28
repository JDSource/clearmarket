---
signal_id: "CMSIG20260628DV05"
signal_slug: "databricks-ipo-k10-p16"
headline: "Databricks IPO before 2027: Kalshi 10% vs Polymarket 16%"
semantic_title: "Databricks IPO mirrors a consistent venue gap on the major desks"
telemetry: "Polymarket 16% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-28T10:26:29+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.16
  volume_cumulative_usd: 478881.38061
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.1
bullets:
  - "Kalshi at 10%, Polymarket at 16%, a 6pp spread with Polymarket the high side."
  - "Polymarket commands roughly 23x Kalshi's cumulative volume on this contract."
  - "Databricks' widely-discussed IPO readiness likely sustains Polymarket's higher, better-supported print."
  - "Resolves on a confirmed public listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 27.7
      poly_vol_24h_usd: 1012.4
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-28T10:26:29+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Polymarket's higher and far more liquid consensus on Databricks is the credible reference price; desks should treat Kalshi's 10% as a discount artifact of thin participation rather than a meaningful bearish signal.
