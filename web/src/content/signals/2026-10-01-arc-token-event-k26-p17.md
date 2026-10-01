---
signal_id: "CMSIG20261001DV00"
signal_slug: "arc-token-event-k26-p17"
headline: "Arc token launch before 2027: Kalshi 26% vs Polymarket 17%"
semantic_title: "Arc token-launch odds carry a premium across venues"
telemetry: "Polymarket 17% vs Kalshi 26%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-01T15:04:26+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.17
  volume_cumulative_usd: 166698.64217799998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.26
bullets:
  - "Kalshi prices Arc token launch at 26%, Polymarket at 17%, a 9pp gap with three months left on the clock."
  - "Kalshi is the higher venue; liquidity is thin on both sides, with Polymarket holding the deeper book by far."
  - "Kalshi's smaller, less liquid market may be repricing on thinner evidence; Polymarket's crowd at scale likely reflects a more settled view."
  - "Resolution: contract settles YES if Arc publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 37.77
      poly_vol_24h_usd: 1351.285295
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-01T15:04:26+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread with lopsided liquidity suggests Kalshi's price is less reliable signal here, a desk should weight Polymarket's 17% as the more informed read until Kalshi volume catches up.
