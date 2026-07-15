---
signal_id: "CMSIG20260715VS01"
signal_slug: "will-bitcoin-reach-80-000-by-december-3-vol-29213"
headline: "Bitcoin $80K by Dec 31: 33% on fresh $29K inflow"
semantic_title: "Bitcoin $80K by year-end faces heavy fade pressure at one-in-three"
telemetry: "33% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-15T10:00:41+00:00"
event_id: "CM-EVT-2S263KKBP2"
event_slug: "what-price-will-bitcoin-hit-before-2027"
event_question: "What price will Bitcoin reach by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc564e47b7a853f3e52ea7b8e28d69ed99fcb284929364fd0f8024c2bca03ea96"
  question_raw: "Will Bitcoin reach $80,000 by December 31, 2026?"
  current_price: 0.33
  volume_24h_usd: 29213.333427
  volume_cumulative_usd: 109286.322692
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices 33% odds Bitcoin retraces to $80K by December 31, 2026, a bearish lean from current levels."
  - "24h volume of $29,213 is 27% of all-time handle, reflecting a meaningful but non-climactic positioning wave."
  - "Fresh capital appears to be hedging or fading a drawdown scenario amid mid-July macro crosscurrents."
  - "Resolves YES only if BTC closes at or below $80K on December 31, 2026."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 29213.333427
sources:
  - label: "ClearMarket market record: What price will Bitcoin reach by the end of 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-before-2027"
    retrieved_at: "2026-07-15T10:00:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

One-third odds on a sub-$80K Bitcoin by year-end with renewed volume suggests options desks and crypto funds are actively pricing tail-downside, worth monitoring alongside BTC derivatives skew.
