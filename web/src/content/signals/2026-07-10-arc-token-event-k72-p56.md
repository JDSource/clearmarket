---
signal_id: "CMSIG20260710DV00"
signal_slug: "arc-token-event-k72-p56"
headline: "Arc token launch before 2027: Kalshi 72% vs Polymarket 57%"
semantic_title: "Arc token-launch odds split sharply across venues"
telemetry: "Polymarket 57% vs Kalshi 72%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-10T10:50:52+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.57
  volume_cumulative_usd: 59385.1271930001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.72
bullets:
  - "Kalshi prices 72%, Polymarket 57%, a 15pp spread on the same binary claim."
  - "Kalshi is the higher venue; Polymarket carries substantially deeper liquidity on this contract."
  - "Thin Kalshi volume likely amplifies noise; Polymarket's crowd may better reflect crypto-insider base rates."
  - "Resolves YES if Arc's token goes live on any chain before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 8.26
      poly_vol_24h_usd: 190.57299999999998
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-07-10T10:50:52+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The wide spread against shallow Kalshi volume suggests the higher print is noise-driven rather than informed, and a desk should weight the Polymarket figure as more reliable.
