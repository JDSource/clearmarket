---
signal_id: "CMSIG20260627DV01"
signal_slug: "applied-intuition-ipo-k10-p20"
headline: "Applied Intuition IPO before 2027: Kalshi 10% vs Polymarket 21%"
semantic_title: "Applied Intuition IPO pricing decouples on the major prediction desks"
telemetry: "Polymarket 21% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-27T01:36:57+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.208
  volume_cumulative_usd: 204929.88350399988
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.1
bullets:
  - "Polymarket marks the IPO at 21%, Kalshi at 10%, an 11pp divergence on an identical before-2027 horizon."
  - "Polymarket holds the higher price and the dominant liquidity base at $204.9K vs Kalshi's $2K cumulative volume."
  - "Kalshi's near-zero participation makes its 10% print statistically thin; Polymarket's six-figure book reflects a broader, more engaged trader set."
  - "Resolution depends on a completed, public IPO listing for Applied Intuition before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 6.0
      poly_vol_24h_usd: 1181.848393
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-06-27T01:36:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Kalshi volume at roughly 1% of Polymarket's, the 11pp gap is almost entirely a function of market depth rather than genuine disagreement, desks should anchor to Polymarket's 21% and monitor Kalshi only for sudden volume inflows that might signal informed flow.
