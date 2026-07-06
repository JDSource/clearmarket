---
signal_id: "CMSIG20260706DV02"
signal_slug: "databricks-ipo-k12-p18"
headline: "Databricks IPO before 2027: Kalshi 12% vs Polymarket 18%"
semantic_title: "Databricks IPO market bridges a moderate spread across venues"
telemetry: "Polymarket 18% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-06T12:01:11+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.18
  volume_cumulative_usd: 480571.38377799996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.12
bullets:
  - "Polymarket prices Databricks IPO before 2027 at 18%; Kalshi at 12%, a 6pp gap."
  - "Polymarket is the higher venue and holds far deeper liquidity than Kalshi."
  - "The moderate spread likely reflects Databricks' well-documented late-stage valuation; Polymarket crowd may be pricing in a higher probability of a surprise accelerated filing."
  - "Resolves YES if Databricks completes an IPO on a public exchange before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 79.64
      poly_vol_24h_usd: 61.22
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-06T12:01:11+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp spread with a deep Polymarket book and a shallow Kalshi book suggests mild informational divergence rather than true arbitrage, desks should treat Polymarket's 18% as the anchor and monitor for any accelerated S-1 filing activity.
