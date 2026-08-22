---
signal_id: "CMSIG20260822VS03"
signal_slug: "will-solana-reach-120-by-december-31-2-vol-18357"
headline: "Solana $120 by Dec 31: 50% on $18K spike"
semantic_title: "Solana at $120 by year-end sits right at 50%"
telemetry: "50% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-BBD03M42C1"
event_slug: "what-price-will-solana-hit-before-2027"
event_question: "Will Solana reach a specific price level in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7bd108cb4e84d39db267ae09d19536805a874e540905f0b3b0fad8154170b4c2"
  question_raw: "Will Solana reach $120 by December 31, 2026?"
  current_price: 0.5
  volume_24h_usd: 18357.121626
  volume_cumulative_usd: 25099.868745
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices exactly 50%, true coin-flip, market finds no edge in either direction."
  - "24h volume $18K is 73% of all-time, making this session the dominant liquidity event for the contract."
  - "Even-odds print at peak volume often precedes a catalyst that breaks the stalemate."
  - "Resolves December 31, 2026."
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
      poly_vol_24h_usd: 18357.121626
sources:
  - label: "ClearMarket market record: Will Solana reach a specific price level in 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-solana-hit-before-2027"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A contract printing 73% of its lifetime volume at exactly 50% signals that the market has arrived at maximum uncertainty, any near-term Solana catalyst will move this price sharply.
