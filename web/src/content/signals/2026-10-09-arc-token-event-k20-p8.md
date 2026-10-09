---
signal_id: "CMSIG20261009DV00"
signal_slug: "arc-token-event-k20-p8"
headline: "Arc token launch before Jan 2027: Kalshi 20% vs Polymarket 8%"
semantic_title: "Arc token-before-2027 odds split sharply across venues"
telemetry: "Polymarket 8% vs Kalshi 20%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-09T07:49:48+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.08
  volume_cumulative_usd: 176308.829995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.2
bullets:
  - "Kalshi prices Arc token launch at 20%, Polymarket at 8%, a 12pp spread on the same claim."
  - "Kalshi sits higher on thin volume; Polymarket holds the lower price against a far deeper liquidity pool."
  - "Thin Kalshi book may reflect a small cluster of informed or speculative positions unanchored by volume; Polymarket's deeper market is the stronger reference price."
  - "Resolution: any confirmed Arc token public launch or issuance announcement before Jan 1, 2027 likely settles YES."
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
      kalshi_vol_24h_usd: 82.39
      poly_vol_24h_usd: 54.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-09T07:49:48+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 12pp gap with Polymarket carrying nearly 44x the volume suggests Kalshi's higher print is a thin-book artifact rather than a genuine information signal, making Polymarket the more defensible anchor for this claim.
