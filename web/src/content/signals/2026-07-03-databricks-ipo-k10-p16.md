---
signal_id: "CMSIG20260703DV02"
signal_slug: "databricks-ipo-k10-p16"
headline: "Databricks IPO before 2027: Kalshi 10% vs Polymarket 16%"
semantic_title: "Databricks IPO before 2027 isolates a spread across venues"
telemetry: "Polymarket 16% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-03T10:33:13+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.16
  volume_cumulative_usd: 480005.798224
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.1
bullets:
  - "Polymarket prices Databricks IPO before 2027 at 16%; Kalshi at 10%, a 6pp gap."
  - "Polymarket is the higher side and commands a substantially larger cumulative volume base."
  - "Databricks' well-publicized late-stage funding rounds may be priced in more fully on Polymarket's larger crowd."
  - "Resolves YES if Databricks lists publicly on a major exchange before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 9.2
      poly_vol_24h_usd: 162.190475
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-03T10:33:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread on a relatively well-covered name like Databricks points to audience fragmentation, Polymarket's larger, tech-focused crowd is pricing a modestly higher IPO probability that Kalshi's thinner market has not yet absorbed.
