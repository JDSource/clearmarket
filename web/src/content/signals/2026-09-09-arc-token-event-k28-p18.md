---
signal_id: "CMSIG20260909DV01"
signal_slug: "arc-token-event-k28-p18"
headline: "Arc token launch before Jan 1 2027: Kalshi 28% vs Polymarket 18%"
semantic_title: "Arc token-launch odds carry a premium on Kalshi over the major desks"
telemetry: "Polymarket 18% vs Kalshi 28%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-09T12:41:30+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.18
  volume_cumulative_usd: 157650.150586
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.28
bullets:
  - "Kalshi prices an Arc token launch before 2027 at 28%; Polymarket at 18%, a 10pp gap."
  - "Kalshi is higher; volume heavily one-sided at $3.7K vs Polymarket's $157.7K."
  - "Polymarket's pool is 43x larger, making its 18% price far more battle-tested and credible."
  - "Resolution: any publicly announced Arc token launch event before January 1, 2027."
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
      kalshi_vol_24h_usd: 33.31
      poly_vol_24h_usd: 129.395122
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-09T12:41:30+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 10pp premium on the thin-liquidity Kalshi side is a classic low-volume distortion, Polymarket's 18% on $157K of traded volume is the price a desk should weight most heavily.
