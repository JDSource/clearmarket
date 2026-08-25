---
signal_id: "CMSIG20260825DV00"
signal_slug: "arc-token-event-k33-p21"
headline: "Arc token launch before 2027: Kalshi 33% vs Polymarket 21%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 21% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-25T08:38:13+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.21
  volume_cumulative_usd: 151564.26787800004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.33
bullets:
  - "Kalshi prices Arc token launch at 33%, Polymarket at 21%, a 12pp gap"
  - "Kalshi is the higher venue; Polymarket carries vastly deeper liquidity at $151K cumulative vs $3.6K"
  - "Thin Kalshi volume may reflect a small concentrated view; Polymarket's larger pool likely prices the claim more reliably"
  - "Resolves YES if Arc publicly launches a token on any network before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 58.2
      poly_vol_24h_usd: 214.16000000000003
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-25T08:38:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 12pp spread, combined with a 40-to-1 liquidity imbalance in Polymarket's favor, suggests the higher Kalshi price reflects thin-market noise rather than a genuine information edge, desks should weight the Polymarket read.
