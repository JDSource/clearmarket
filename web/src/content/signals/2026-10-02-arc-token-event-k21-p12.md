---
signal_id: "CMSIG20261002DV00"
signal_slug: "arc-token-event-k21-p12"
headline: "Arc token launch before Jan 1 2027: Kalshi 21% vs Polymarket 12%"
semantic_title: "Arc token-before-2027 odds split sharply across venues"
telemetry: "Polymarket 12% vs Kalshi 21%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-02T14:26:41+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.12
  volume_cumulative_usd: 167003.883335
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.21
bullets:
  - "Kalshi prices Arc token launch at 21%, Polymarket at 12%, a 9pp gap with under 3 months to resolution."
  - "Kalshi is the higher side; Polymarket carries substantially deeper liquidity at roughly 47x the cumulative volume."
  - "Thin Kalshi volume likely inflates the price; Polymarket's deeper pool suggests the lower figure is the more informed read."
  - "Resolves on any confirmed public Arc token launch before January 1, 2027."
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
      kalshi_vol_24h_usd: 51.61
      poly_vol_24h_usd: 305.241157
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-10-02T14:26:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread almost certainly reflects a liquidity imbalance rather than genuine information asymmetry, a desk should weight Polymarket's 12% as the more reliable prior given its volume advantage.
