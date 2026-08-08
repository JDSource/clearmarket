---
signal_id: "CMSIG20260808DV00"
signal_slug: "arc-token-event-k45-p31"
headline: "Arc token launch before 2027: Kalshi 45% vs Polymarket 31%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 31% vs Kalshi 45%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-08T08:36:39+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.31
  volume_cumulative_usd: 142577.03232899992
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.45
bullets:
  - "Kalshi prices the launch at 45%, Polymarket at 31%, a 14pp gap"
  - "Kalshi sits higher; Polymarket carries far deeper liquidity at roughly 44x Kalshi volume"
  - "Thin Kalshi book may reflect a small concentrated position; Polymarket's larger pool likely prices the claim more robustly"
  - "Resolves YES on any confirmed Arc token public launch before Jan 1, 2027"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-F36B8880EB); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 27.76
      poly_vol_24h_usd: 5044.5
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-08T08:36:39+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The wide spread against a heavily lopsided liquidity profile suggests Kalshi's higher price is noise from a thin book rather than a genuine informational edge, a desk leaning on the more liquid venue would treat 31% as the cleaner reference.
