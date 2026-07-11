---
signal_id: "CMSIG20260711DV04"
signal_slug: "databricks-ipo-k9-p14"
headline: "Databricks IPO before 2027: Kalshi 9% vs Polymarket 14%"
semantic_title: "Databricks IPO spread bridges across prediction venues"
telemetry: "Polymarket 14% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-11T09:25:37+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.14
  volume_cumulative_usd: 482895.0304749999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Kalshi at 9%, Polymarket at 14%, a 5pp gap on a low-probability near-term claim."
  - "Polymarket is higher and carries roughly 25x Kalshi's cumulative volume."
  - "Polymarket's deeper liquidity makes its 14% more credible; Kalshi at 9% may reflect lower engagement on this name."
  - "Resolves on a confirmed Databricks public listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 6.84
      poly_vol_24h_usd: 61.06
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-11T09:25:37+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 5pp gap is modest in absolute terms but meaningful at this probability level; with the liquidity advantage firmly at Polymarket, desks should treat 14% as the reference price for Databricks near-term IPO risk.
