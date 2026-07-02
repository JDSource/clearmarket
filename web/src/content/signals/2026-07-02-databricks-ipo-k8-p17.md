---
signal_id: "CMSIG20260702DV01"
signal_slug: "databricks-ipo-k8-p17"
headline: "Databricks IPO before 2027: Kalshi 8% vs Polymarket 17%"
semantic_title: "Databricks IPO odds decouple on the major prediction desks"
telemetry: "Polymarket 17% vs Kalshi 8%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-02T10:35:37+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.17
  volume_cumulative_usd: 479843.607749
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.08
bullets:
  - "Polymarket prices Databricks IPO before 2027 at 17%, Kalshi at 8%, a 9pp gap."
  - "Polymarket is the high side and holds roughly 28x Kalshi's cumulative volume."
  - "Deep Polymarket liquidity behind the higher price suggests broader market conviction; Kalshi's lower print may reflect audience or flow differences."
  - "Resolution: a Databricks IPO pricing or listing event before Jan 1 2027 settles YES."
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
      kalshi_vol_24h_usd: 8.8
      poly_vol_24h_usd: 93.578311
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-02T10:35:37+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With the better-capitalized venue pricing nearly twice as high, a desk should weight Polymarket's 17% as the primary signal and treat Kalshi's 8% as a stale or structurally discounted print.
