---
signal_id: "CMSIG20260917DV00"
signal_slug: "arc-token-event-k36-p25"
headline: "Arc token launch before 2027: Kalshi 36% vs Polymarket 25%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 25% vs Kalshi 36%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-17T13:06:01+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.25
  volume_cumulative_usd: 161318.53593700007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.36
bullets:
  - "Kalshi prices Arc token launch at 36%, Polymarket at 25%, an 11pp gap with weeks left on the clock."
  - "Kalshi is the higher venue; Polymarket carries the deeper book by a wide margin."
  - "Thin Kalshi volume may reflect a smaller, more speculative audience bidding up a low-liquidity contract; Polymarket's larger pool likely reflects broader consensus."
  - "Resolves YES if Arc officially launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 398.45
      poly_vol_24h_usd: 744.530411
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-17T13:06:01+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp gap on a near-term binary with little time to resolution suggests Kalshi's thin book is driving noise rather than signal, Polymarket's price carries more weight here.
