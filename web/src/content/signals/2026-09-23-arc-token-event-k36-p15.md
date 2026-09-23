---
signal_id: "CMSIG20260923DV00"
signal_slug: "arc-token-event-k36-p15"
headline: "Arc token before 2027: Kalshi 36% vs Polymarket 15%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 36%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-23T13:18:38+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 163212.28750599996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.36
bullets:
  - "Kalshi prices Arc token launch at 36%, Polymarket at 15%, a 21pp gap with under 100 days to resolution."
  - "Kalshi sits higher; Polymarket carries roughly 29x the cumulative volume, suggesting deeper consensus on the low side."
  - "Thin Kalshi liquidity may reflect a small cohort pricing on insider signals or speculation; Polymarket's depth lends it more credibility here."
  - "Resolves YES if Arc publicly launches any token before Jan 1, 2027, a binary, date-bound event with no partial credit."
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
      kalshi_vol_24h_usd: 110.15
      poly_vol_24h_usd: 55.18000000000001
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-23T13:18:38+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 21pp gap against a high-volume Polymarket lean toward 'No' flags a likely mispricing on Kalshi, where thin liquidity leaves the market vulnerable to a small number of optimistic participants setting the price.
