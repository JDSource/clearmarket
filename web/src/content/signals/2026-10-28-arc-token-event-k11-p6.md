---
signal_id: "CMSIG20261028DV01"
signal_slug: "arc-token-event-k11-p6"
headline: "Arc token before 2027: Kalshi 11% vs Polymarket 6%"
semantic_title: "Arc token-launch odds carry a premium on one major desk"
telemetry: "Polymarket 6% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-28T15:35:41+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.06
  volume_cumulative_usd: 186060.432986
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.11
bullets:
  - "Kalshi prices Arc token launch at 11%, Polymarket at 6%, a 5pp gap"
  - "Kalshi is the higher venue; Polymarket holds $186K cumulative volume against Kalshi's $2.5K"
  - "With under 65 days to resolution and both venues pricing this below 15%, the spread likely reflects thin Kalshi order flow rather than a differing view on Arc's launch timeline"
  - "Resolves YES if Arc publicly launches a token before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 63.99
      poly_vol_24h_usd: 39.99
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-28T15:35:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 5pp gap is notable in absolute terms but both venues agree this is a low-probability event; the Kalshi premium is most plausibly a liquidity artifact, and a desk would anchor to Polymarket's 6% as the more informed price.
