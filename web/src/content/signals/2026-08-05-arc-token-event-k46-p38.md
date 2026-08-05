---
signal_id: "CMSIG20260805DV01"
signal_slug: "arc-token-event-k46-p38"
headline: "Arc token launch before Jan 1 2027: Kalshi 46% vs Polymarket 38%"
semantic_title: "Arc token launch timeline decouples on the major prediction desks"
telemetry: "Polymarket 38% vs Kalshi 46%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-05T10:32:12+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.38
  volume_cumulative_usd: 130314.829893
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.46
bullets:
  - "Kalshi sits at 46% vs Polymarket at 38%, an 8pp gap on an identical claim"
  - "Kalshi is higher on just $3K volume; Polymarket is lower but backed by $130K"
  - "Kalshi's thin book makes its 46% price fragile; Polymarket's 38% carries far more weight as a signal"
  - "Resolution turns on a verifiable public Arc token launch before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 8.81
      poly_vol_24h_usd: 460.237271
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-05T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 40x volume gap makes this a one-sided read, Polymarket's 38% is the credible anchor, and Kalshi's higher price likely reflects a small, less-contested order book rather than genuine disagreement.
