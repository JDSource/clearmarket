---
signal_id: "CMSIG20260627DV02"
signal_slug: "databricks-ipo-k13-p23"
headline: "Databricks IPO before 2027: Kalshi 13% vs Polymarket 23%"
semantic_title: "Databricks IPO spread persists across venues despite deeper liquidity"
telemetry: "Polymarket 23% vs Kalshi 13%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-27T01:36:57+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.23
  volume_cumulative_usd: 477861.86296399997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.13
bullets:
  - "Polymarket prices the Databricks IPO at 23%, Kalshi at 13%, a 10pp gap on the same before-2027 claim."
  - "Polymarket commands the higher price and substantially larger book at $477.9K vs Kalshi's $27.2K cumulative volume."
  - "Unlike the other divergences here, Kalshi carries meaningful volume, suggesting genuine cross-venue disagreement rather than a pure liquidity vacuum."
  - "Resolution requires a completed public offering for Databricks before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 89.08
      poly_vol_24h_usd: 662.5233969999999
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-27T01:36:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Databricks divergence is the most structurally interesting of the three, Kalshi's $27K book is non-trivial, making the 10pp gap a credible signal of audience or information differences between venues rather than simply an illiquidity artifact, warranting closer monitoring for convergence.
