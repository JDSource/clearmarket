---
signal_id: "CMSIG20261025DV00"
signal_slug: "arc-token-event-k14-p9"
headline: "Arc token launch before 2027: Kalshi 14% vs Polymarket 9%"
semantic_title: "Arc token-before-2027 odds run higher on one venue"
telemetry: "Polymarket 9% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-25T07:49:29+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.09
  volume_cumulative_usd: 184557.302986
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices the Arc token launch at 14%, Polymarket at 9%, a 5pp gap with under ten weeks to resolution."
  - "Kalshi is the higher-priced venue; Polymarket carries the dominant liquidity at roughly 60x Kalshi's cumulative volume."
  - "Thin Kalshi volume may skew its price upward; Polymarket's deeper market likely reflects broader consensus at the lower probability."
  - "Resolution hinges on a verifiable Arc token launch announcement on or before Dec 31, 2026."
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
      kalshi_vol_24h_usd: 19.53
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-25T07:49:29+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket carrying nearly all the liquidity and pricing the event lower, a desk leaning on volume-weighted consensus would treat 9% as the more reliable signal, while the Kalshi premium likely reflects a shallow, easily moved market rather than genuine informational edge.
