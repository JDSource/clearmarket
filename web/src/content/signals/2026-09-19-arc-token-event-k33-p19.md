---
signal_id: "CMSIG20260919DV00"
signal_slug: "arc-token-event-k33-p19"
headline: "Arc token before 2027: Kalshi 33% vs Polymarket 19%"
semantic_title: "Arc token launch odds split sharply across venues"
telemetry: "Polymarket 19% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-19T12:16:09+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.19
  volume_cumulative_usd: 162157.66180799995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.33
bullets:
  - "14pp gap: Kalshi prices Arc token launch at 33%, Polymarket at 19% ahead of Jan 1, 2027."
  - "Kalshi sits higher; Polymarket carries roughly 32x more cumulative volume, reflecting deeper market conviction on the lower price."
  - "Thin Kalshi liquidity may leave its price more sensitive to a handful of trades, while Polymarket's larger pool likely prices in stronger evidence against a near-term launch."
  - "Resolves YES if Arc publishes or deploys an official token on any network before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 7.25
      poly_vol_24h_usd: 320.98
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-09-19T12:16:09+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The wide 14pp spread against lopsided volume strongly favors Polymarket's 19% as the more reliable signal, suggesting Kalshi's elevated print reflects thin-market noise rather than genuine informational edge.
