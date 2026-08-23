---
signal_id: "CMSIG20260823VS01"
signal_slug: "will-solana-reach-120-by-december-31-2-vol-13360"
headline: "Solana $120 by Dec 31: 52% on $13K surge"
semantic_title: "Odds hold near 50% as $120 Solana bet draws heavy trading"
telemetry: "52% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-23T08:24:40+00:00"
event_id: "CM-EVT-BBD03M42C1"
event_slug: "what-price-will-solana-hit-before-2027"
event_question: "Will Solana reach a specific price level in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7bd108cb4e84d39db267ae09d19536805a874e540905f0b3b0fad8154170b4c2"
  question_raw: "Will Solana reach $120 by December 31, 2026?"
  current_price: 0.52
  volume_24h_usd: 13360.109359999999
  volume_cumulative_usd: 38459.978104999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket sits at 52%, essentially a coin-flip, meaning the market sees the $120 target as right at the edge of probable."
  - "24h volume of $13K is 35% of all-time handle, indicating concentrated fresh interest compressing into a near-binary outcome."
  - "At 52%, new capital is being deployed on both sides of the line, consistent with a macro or crypto-sector catalyst sharpening conviction."
  - "Resolves Dec 31, 2026; with SOL near the threshold implied by market pricing, small price moves carry outsized resolution risk."
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
      poly_vol_24h_usd: 13360.109359999999
sources:
  - label: "ClearMarket market record: Will Solana reach a specific price level in 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-solana-hit-before-2027"
    retrieved_at: "2026-08-23T08:24:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 35% all-time volume day at near-50% odds means the market is actively disputed, not settled, desks should treat this as a live risk event and monitor spot SOL price action and broader crypto-market sentiment for directional resolution clues.
