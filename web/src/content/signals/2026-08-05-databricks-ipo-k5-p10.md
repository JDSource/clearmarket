---
signal_id: "CMSIG20260805DV03"
signal_slug: "databricks-ipo-k5-p10"
headline: "Databricks IPO before 2027: Kalshi 5% vs Polymarket 10%"
semantic_title: "Databricks IPO pricing runs in opposite directions across venues"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-05T10:32:12+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 485852.77207500004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Kalshi prices 5% vs Polymarket 10%, a 5pp gap with the cheaper venue being the larger-volume one"
  - "Polymarket is higher at 10% with $486K behind it; Kalshi is lower at 5% with only $11K"
  - "Unusually, the thinner desk is more bearish, Polymarket's deeply liquid 10% is the stronger signal here"
  - "Resolution requires a completed Databricks public listing before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 0.55
      poly_vol_24h_usd: 10.19
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-08-05T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This is the batch's cleanest inversion, the high-volume venue is the optimistic one, suggesting Kalshi's 5% is the stale or neglected price, and a desk should weight Polymarket's 10% as the live consensus.
