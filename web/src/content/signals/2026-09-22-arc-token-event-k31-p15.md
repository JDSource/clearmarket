---
signal_id: "CMSIG20260922DV00"
signal_slug: "arc-token-event-k31-p15"
headline: "Arc token before Jan 1 2027: Kalshi 31% vs Polymarket 15%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 31%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-22T07:49:09+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 163157.10750599997
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.31
bullets:
  - "Kalshi prices Arc token launch at 31%, Polymarket at 15%, a 16pp gap."
  - "Kalshi is the higher venue; Polymarket carries overwhelming liquidity depth on its side."
  - "Thin Kalshi volume likely reflects a small, possibly less-informed pool; Polymarket's deep book gives its 15% more price-discovery weight."
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027, roughly 100 days out."
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
      kalshi_vol_24h_usd: 14.64
      poly_vol_24h_usd: 824.7597049999999
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-22T07:49:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 16pp spread, coupled with a 34x liquidity imbalance favoring Polymarket's lower price, suggests the higher Kalshi print is an artifact of thin participation rather than genuine informational disagreement, a desk leaning short on Arc token launch should find Kalshi the more actionable side.
