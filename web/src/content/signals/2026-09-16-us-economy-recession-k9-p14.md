---
signal_id: "CMSIG20260916DV04"
signal_slug: "us-economy-recession-k9-p14"
headline: "US recession in 2026: Kalshi 9% vs Polymarket 14%"
semantic_title: "US recession in 2026 stays near long-shot odds, gaps modestly across desks"
telemetry: "Polymarket 14% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-16T13:04:24+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.14
  volume_cumulative_usd: 1946555.666463
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.09
bullets:
  - "Kalshi prices a 2026 recession at 9%, Polymarket at 14%, a 5pp gap"
  - "Polymarket is the higher venue and holds roughly 6x Kalshi's cumulative volume"
  - "Both venues carry substantial liquidity here, making this the most credibly contested divergence in the batch"
  - "Resolution hinges on the official definition of recession applied, typically two consecutive quarters of negative GDP"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-2FB03D51D4); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 1866.53
      poly_vol_24h_usd: 193300.093286
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-16T13:04:24+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With deep books on both sides, this 5pp gap is the most structurally meaningful divergence in the set, a desk should scrutinize the resolution criteria on each platform, as a definitional difference may be sustaining what would otherwise be an arb opportunity.
