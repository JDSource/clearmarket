---
signal_id: "CMSIG20261010DV00"
signal_slug: "arc-token-event-k20-p11"
headline: "Arc token before 2027: Kalshi 20% vs Polymarket 11%"
semantic_title: "Arc token launch odds trade far apart across venues"
telemetry: "Polymarket 11% vs Kalshi 20%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-10T14:13:22+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.11
  volume_cumulative_usd: 177086.74999500002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.2
bullets:
  - "Kalshi prices Arc token launch at 20%, Polymarket at 11%, a 9pp gap on the same claim."
  - "Kalshi sits higher at 20% with thin liquidity ($4K cumulative); Polymarket holds 11% on $177K volume."
  - "Polymarket's deeper liquidity makes its 11% the more crowd-tested level; Kalshi's premium likely reflects a smaller, less informed pool."
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
      kalshi_vol_24h_usd: 128.01
      poly_vol_24h_usd: 777.92
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-10T14:13:22+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread, heavily skewed by Polymarket's liquidity advantage, suggests Kalshi's 20% is noise from a thin market rather than a genuine informational signal, the Polymarket 11% is the more reliable reference price.
