---
signal_id: "CMSIG20260701DV00"
signal_slug: "databricks-ipo-k6-p17"
headline: "Databricks IPO before 2027: Kalshi 6% vs Polymarket 17%"
semantic_title: "Databricks before 2027 splits sharply across venues"
telemetry: "Polymarket 17% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-01T11:22:20+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.17
  volume_cumulative_usd: 479750.029438
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.06
bullets:
  - "Polymarket prices the Databricks IPO at 17%, Kalshi at 6%, an 11pp spread."
  - "Polymarket is the higher-priced venue, carrying the dominant liquidity; Kalshi is thinly traded on this contract."
  - "Shallow Kalshi volume may reflect stale price discovery; Polymarket's deeper pool likely better incorporates current IPO-window signals."
  - "Contract resolves YES if Databricks completes an IPO before January 1, 2027."
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
      kalshi_vol_24h_usd: 4.47
      poly_vol_24h_usd: 68.112641
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-01T11:22:20+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp gap and lopsided liquidity suggest Kalshi's 6% print is an artifact of low activity rather than a genuine consensus, making Polymarket's 17% the more reliable reference for a desk pricing near-term IPO probability.
