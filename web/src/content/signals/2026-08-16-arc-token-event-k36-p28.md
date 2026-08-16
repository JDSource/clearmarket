---
signal_id: "CMSIG20260816DV00"
signal_slug: "arc-token-event-k36-p28"
headline: "Will Arc launch a token before Jan 1, 2027? Kalshi 36% vs Polymarket 28%"
semantic_title: "Arc token launch odds split across venues before 2027"
telemetry: "Polymarket 28% vs Kalshi 36%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-16T08:24:18+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Arc launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0a8d89321f01639ec17b6bcf1ef0b6c15137b1934605f8bffeb50b2f291756d4"
  question_raw: "Will Arc launch a token by December 31 2026?"
  current_price: 0.28
  volume_cumulative_usd: 148739.28647200007
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-ARC"
    question_raw: "Will Arc launch a token before Jan 1, 2027?"
    current_price: 0.36
bullets:
  - "Kalshi prices 36%, Polymarket 28%, an 8pp gap on the same binary claim"
  - "Kalshi is the higher venue; liquidity is thin ($3,458 cum vol) vs Polymarket's deep book ($148,739)"
  - "Thin Kalshi volume likely reflects a small number of informed or speculative positions skewing the price upward"
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
      kalshi_vol_24h_usd: 111.6
      poly_vol_24h_usd: 96.445772
sources:
  - label: "ClearMarket cross-venue record: Will Arc launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/arc-token-event-y-2026"
    retrieved_at: "2026-08-16T08:24:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp spread with a nearly 43x liquidity gap suggests Kalshi's price is noise-prone and Polymarket's 28% is the more reliable anchor for a desk assessing this claim.
