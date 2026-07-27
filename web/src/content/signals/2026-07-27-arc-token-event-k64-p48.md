---
signal_id: "CMSIG20260727DV00"
signal_slug: "arc-token-event-k64-p48"
headline: "Arc token launch before 2027: Kalshi 64% vs Polymarket 48%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 48% vs Kalshi 64%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-27T11:16:57+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.48
  volume_cumulative_usd: 95902.28003900008
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.64
bullets:
  - "Kalshi prices Arc token launch at 64%, Polymarket at 48%, a 16pp gap"
  - "Kalshi is the higher venue; liquidity thin at $4K cumulative vs $96K on Polymarket"
  - "Polymarket's deeper market likely reflects broader crowd; Kalshi price may reflect thin-book distortion"
  - "Resolves YES if Arc officially launches a token before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 136.05
      poly_vol_24h_usd: 2915.4842889999995
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-27T11:16:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 16pp spread with a 23x liquidity imbalance strongly suggests Kalshi's higher price is a thin-book artifact, the Polymarket 48% read carries more weight for a desk sizing any position.
