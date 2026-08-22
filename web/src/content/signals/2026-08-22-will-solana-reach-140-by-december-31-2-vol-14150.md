---
signal_id: "CMSIG20260822VS07"
signal_slug: "will-solana-reach-140-by-december-31-2-vol-14150"
headline: "Solana $140 by Dec 31: 27% on $14K surge"
semantic_title: "Long-shot Solana $140 by year-end draws heavy trading"
telemetry: "27% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-BBD03M42C1"
event_slug: "what-price-will-solana-hit-before-2027"
event_question: "Will Solana reach a specific price level in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8b2c465928dfda7a0decfb93bc4bbd60e067a6c57016d678dd97c49ba76f3bdd"
  question_raw: "Will Solana reach $140 by December 31, 2026?"
  current_price: 0.27
  volume_24h_usd: 14150.021149
  volume_cumulative_usd: 22798.485853
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices 27%, market treats $140 as an upside scenario, not a base case."
  - "24h volume $14K is 62% of all-time, a majority of lifetime flow in one session."
  - "Active alongside the $120 contract, suggesting traders are positioning across a Solana price ladder."
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
      poly_vol_24h_usd: 14150.021149
sources:
  - label: "ClearMarket market record: Will Solana reach a specific price level in 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-solana-hit-before-2027"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume across Solana's $120 and $140 year-end contracts points to structured range-expression trades, desks building SOL exposure should note the implied distribution skews below $140.
