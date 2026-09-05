---
signal_id: "CMSIG20260905DV00"
signal_slug: "arc-token-event-k37-p15"
headline: "Arc token launch before 2027: Kalshi 37% vs Polymarket 15%"
semantic_title: "Arc token-before-2027 trades far apart across venues"
telemetry: "Polymarket 15% vs Kalshi 37%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-05T11:35:42+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 156316.61664200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.37
bullets:
  - "Kalshi prices 37%, Polymarket 15%, a 22pp spread on the same binary claim."
  - "Kalshi sits higher with $4,687 cumulative volume; Polymarket lower with $156,317."
  - "Polymarket's deeper liquidity likely reflects more informed price discovery, making 15% the harder number to fade."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027; roughly 4 months remain."
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
      kalshi_vol_24h_usd: 7.7
      poly_vol_24h_usd: 62.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-05T11:35:42+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 22pp gap, with volume heavily skewed to the lower-priced venue, suggests Kalshi's thin book may be mispricing this, and a desk with confidence in Polymarket's signal could find a straightforward long on that side.
