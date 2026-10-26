---
signal_id: "CMSIG20261026DV00"
signal_slug: "arc-token-event-k15-p6"
headline: "Arc token launch before 2027: Kalshi 15% vs Polymarket 6%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 6% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-26T14:49:17+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.06
  volume_cumulative_usd: 185773.35298599998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.15
bullets:
  - "Kalshi prices the launch at 15%, Polymarket at 6%, a 9pp gap with under 68 days to resolution."
  - "Kalshi sits higher with cumulative volume near $3K; Polymarket carries the deeper market at $185K+."
  - "Thin Kalshi liquidity likely drives the premium, Polymarket's larger crowd suggests lower credibility for a near-term launch."
  - "Resolves YES if Arc announces and launches a token on-chain before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 4.16
      poly_vol_24h_usd: 632.46
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-26T14:49:17+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With resolution weeks away and Polymarket showing overwhelming volume behind the 6% price, the Kalshi 15% reads as a thin-market artifact rather than genuine disagreement, a desk should treat Polymarket as the reference price here.
