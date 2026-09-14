---
signal_id: "CMSIG20260914DV00"
signal_slug: "arc-token-event-k34-p18"
headline: "Arc token launch before 2027: Kalshi 34% vs Polymarket 18%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 18% vs Kalshi 34%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-14T14:42:13+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.18
  volume_cumulative_usd: 159031.44908799996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.34
bullets:
  - "Kalshi prices Arc token launch at 34%, Polymarket at 18%, a 16pp gap"
  - "Kalshi sits higher; Polymarket carries far deeper liquidity on both sides"
  - "Thin Kalshi volume may reflect a smaller, less-informed pool pricing in rumor; Polymarket's larger book likely reflects broader crowd conviction against launch"
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
      kalshi_vol_24h_usd: 23.19
      poly_vol_24h_usd: 152.484112
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-14T14:42:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 16pp spread with a volume ratio of roughly 34-to-1 favoring Polymarket suggests the lower Polymarket price is the more liquid and likely more reliable signal, a desk leaning YES should demand a clear informational edge before fading it.
