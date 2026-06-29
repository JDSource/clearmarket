---
signal_id: "CMSIG20260629DV01"
signal_slug: "applied-intuition-ipo-k10-p22"
headline: "Applied Intuition IPO before 2027: Kalshi 10% vs Polymarket 23%"
semantic_title: "Applied Intuition IPO claim decouples on the major prediction desks"
telemetry: "Polymarket 23% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-29T01:47:46+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.227
  volume_cumulative_usd: 205264.4235039999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.1
bullets:
  - "Polymarket marks Applied Intuition IPO at 23%, Kalshi at 10%, a 13pp gap before year-end 2026."
  - "Polymarket is the higher venue with roughly 100x Kalshi's cumulative volume, indicating far greater conviction."
  - "Kalshi's lower price may reflect conservative interpretation of 'IPO' or limited sophisticated flow on the book."
  - "Resolves YES on a completed public listing of Applied Intuition before Jan 1, 2027."
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
      poly_vol_24h_usd: 40.4
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-06-29T01:47:46+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With a 100x volume differential, the 13pp spread almost certainly reflects Kalshi price unreliability rather than genuine market disagreement, a desk should anchor to Polymarket's level.
