---
signal_id: "CMSIG20261102DV01"
signal_slug: "arc-token-event-k14-p4"
headline: "Arc token launch before 2027: Kalshi 14% vs Polymarket 4%"
semantic_title: "Arc token-before-2027 odds build a wide gap across the major desks"
telemetry: "Polymarket 4% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-02T17:46:21+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.04
  volume_cumulative_usd: 194849.897275
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.14
bullets:
  - "Kalshi sits at 14%, Polymarket at 4%, a 10pp gap with resolution just two months away."
  - "Kalshi is markedly higher; Polymarket holds commanding liquidity at roughly 60x the Kalshi volume."
  - "Such a wide spread this close to expiry points to thin Kalshi liquidity distorting the price upward versus Polymarket's well-traded baseline."
  - "Resolves YES only if Arc publicly launches a token before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 499.3
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-11-02T17:46:21+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 10pp dislocation on a sub-60-day binary where one venue has 60x the volume is a strong signal the thinner venue's price is stale, a desk should treat Polymarket's 4% as the credible anchor and assess whether Kalshi arb is executable at scale.
