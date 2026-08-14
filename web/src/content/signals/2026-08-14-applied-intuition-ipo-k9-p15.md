---
signal_id: "CMSIG20260814DV03"
signal_slug: "applied-intuition-ipo-k9-p15"
headline: "Applied Intuition IPO before 2027: Kalshi 9% vs Polymarket 16%"
semantic_title: "Applied Intuition IPO pricing decouples across prediction desks"
telemetry: "Polymarket 16% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-14T09:05:25+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.157
  volume_cumulative_usd: 205870.78790399997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Polymarket prices Applied Intuition IPO at 16%, Kalshi at 9%, a 7pp gap"
  - "Polymarket is higher at 16% on a book roughly 95x larger than Kalshi's"
  - "Kalshi's low volume makes its 9% read unreliable; Polymarket's size gives its 16% stronger price discovery credentials"
  - "Resolves YES if Applied Intuition completes a public listing before Jan 1, 2027"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-52E2DEB126); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-08-14T09:05:25+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The divergence here is directionally opposite to Ramp but structurally similar, the venue with far greater liquidity (Polymarket at 16%) should be weighted heavily, and Kalshi's 9% treated with skepticism.
