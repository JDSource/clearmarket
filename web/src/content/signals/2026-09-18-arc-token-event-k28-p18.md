---
signal_id: "CMSIG20260918DV00"
signal_slug: "arc-token-event-k28-p18"
headline: "Arc token before 2027: Kalshi 29% vs Polymarket 18%, 11pp gap"
semantic_title: "Arc token launch odds carry a premium on the low-volume desk"
telemetry: "Polymarket 18% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-18T12:40:20+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.18
  volume_cumulative_usd: 161836.68180799996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.29
bullets:
  - "Kalshi prices Arc token launch at 29%, Polymarket at 18%, an 11pp spread."
  - "Kalshi is the higher side with thin liquidity; Polymarket holds the deeper book."
  - "Deeper Polymarket volume likely reflects broader participant consensus, making its 18% the more tested read."
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
      kalshi_vol_24h_usd: 8.5
      poly_vol_24h_usd: 518.145871
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-18T12:40:20+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp spread with a heavily lopsided volume ratio suggests the Kalshi price is noise from a thin book, and a desk should weight Polymarket's 18% as the more reliable signal.
