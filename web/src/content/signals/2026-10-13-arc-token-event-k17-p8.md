---
signal_id: "CMSIG20261013DV00"
signal_slug: "arc-token-event-k17-p8"
headline: "Arc token launch before 2027: Kalshi 17% vs Polymarket 8%"
semantic_title: "Arc token launch odds run wide across venues"
telemetry: "Polymarket 8% vs Kalshi 17%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T07:49:40+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.08
  volume_cumulative_usd: 177590.63280899994
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.17
bullets:
  - "Kalshi prices Arc token launch at 17%, Polymarket at 8%, a 9pp gap on the same claim."
  - "Kalshi sits higher with thin liquidity; Polymarket holds the lower price on vastly deeper volume."
  - "Polymarket's deep market likely reflects better-informed consensus; Kalshi's elevated odds may stem from low-volume noise on a niche crypto claim."
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
      kalshi_vol_24h_usd: 79.14
      poly_vol_24h_usd: 21.96
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-13T07:49:40+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread, with Kalshi's price built on a fraction of Polymarket's volume, suggests the higher Kalshi price is unreliable, the deep Polymarket market at 8% is the more defensible anchor for a desk assessing this claim.
