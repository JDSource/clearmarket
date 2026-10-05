---
signal_id: "CMSIG20261005DV00"
signal_slug: "arc-token-event-k18-p10"
headline: "Arc token launch before 2027: Kalshi 18% vs Polymarket 10%"
semantic_title: "Arc token-launch odds split sharply across venues"
telemetry: "Polymarket 10% vs Kalshi 18%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-05T07:48:26+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.1
  volume_cumulative_usd: 175713.82999499992
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.18
bullets:
  - "Kalshi prices Arc token launch at 18%, Polymarket at 10%, an 8pp gap on the same claim."
  - "Kalshi carries the higher price; Kalshi cumulative volume $3,503 vs Polymarket $175,714."
  - "Polymarket's much deeper liquidity likely anchors its lower price closer to true consensus; Kalshi's thin book leaves it more exposed to single-actor positioning."
  - "Resolution hinges on a verifiable Arc token launch announcement or on-chain deployment before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 194.58
      poly_vol_24h_usd: 505.22666
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-05T07:48:26+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp spread on a thin-vs-deep volume split suggests Kalshi's elevated price reflects limited price discovery rather than genuine informational edge, making the Polymarket side the more liquidity-supported reference for a desk pricing this risk.
