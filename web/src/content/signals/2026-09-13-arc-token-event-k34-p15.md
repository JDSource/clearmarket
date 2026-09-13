---
signal_id: "CMSIG20260913DV00"
signal_slug: "arc-token-event-k34-p15"
headline: "Arc token launch before 2027: Kalshi 34% vs Polymarket 15%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 15% vs Kalshi 34%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-13T13:05:28+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.15
  volume_cumulative_usd: 158877.614976
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.34
bullets:
  - "Kalshi prices Arc token launch at 34%, Polymarket at 15%, a 19pp gap"
  - "Kalshi sits higher on thin volume; Polymarket carries the deeper book by far"
  - "Sparse liquidity on Kalshi may reflect a small, conviction-heavy position skewing the price; Polymarket's larger pool likely provides a more tested read"
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
      kalshi_vol_24h_usd: 19.61
      poly_vol_24h_usd: 367.32
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-13T13:05:28+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 19pp spread on a thin-vs-deep volume split suggests the Kalshi price is fragile and likely to compress toward Polymarket's 15% as participation grows, a desk watching this claim should weight the deeper venue's signal more heavily.
