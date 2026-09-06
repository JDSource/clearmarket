---
signal_id: "CMSIG20260906DV00"
signal_slug: "arc-token-event-k38-p15"
headline: "Arc token before Jan 2027: Kalshi 38% vs Polymarket 15%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 38%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-06T11:55:02+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 156316.616642
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.38
bullets:
  - "Kalshi prices the launch at 38%, Polymarket at 15%, a 23pp gap with under four months to resolution."
  - "Kalshi sits higher with $4,841 cumulative volume; Polymarket carries the dominant liquidity at $156,317."
  - "Thin Kalshi volume likely inflates its price; Polymarket's deeper book makes its 15% the more market-tested read."
  - "Resolves YES if Arc publicly launches a token on any network before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 27.71
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-06T11:55:02+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 23pp spread almost certainly reflects Kalshi's thin liquidity rather than a genuine information edge, a desk should treat Polymarket's 15% as the credible anchor and view Kalshi as offering a potential long if its book deepens toward the better-informed price.
