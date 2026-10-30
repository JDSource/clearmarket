---
signal_id: "CMSIG20261030DV01"
signal_slug: "arc-token-event-k10-p4"
headline: "Arc token launch before 2027: Kalshi 10% vs Polymarket 4%"
semantic_title: "Arc token-before-2027 prices far apart on the major prediction desks"
telemetry: "Polymarket 4% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-30T07:49:21+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.04
  volume_cumulative_usd: 192296.05753599998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.1
bullets:
  - "Kalshi prices an Arc token launch at 10%; Polymarket at 4%, a 6pp gap."
  - "Kalshi holds higher odds on $2,281 volume; Polymarket anchors lower with $192,296 behind it."
  - "Both venues lean heavily against a 2026 launch; Polymarket's deeper book puts longer odds on the event."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 4.18
      poly_vol_24h_usd: 846.08455
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-30T07:49:21+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With only two months left in the horizon and Polymarket's liquid market pricing the event near 4%, the Kalshi premium looks like a thin-book artifact, a desk should treat the low-single-digit range as the credible fair value.
