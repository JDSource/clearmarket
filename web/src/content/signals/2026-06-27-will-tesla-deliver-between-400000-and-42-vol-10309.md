---
signal_id: "CMSIG20260627VS05"
signal_slug: "will-tesla-deliver-between-400000-and-42-vol-10309"
headline: "Tesla Q2 400K, 425K deliveries: 29% on $10K"
semantic_title: "Tesla 400K, 425K delivery band targeted by late Q2 capital"
telemetry: "29% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-TKB6WQH0P3"
event_slug: "how-many-tesla-deliveries-in-q2-2026"
event_question: "Will Tesla deliver between 350000 and 375000 vehicles in Q2 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb98ca5f27a851fd490082e9d3f3058e9a8cf0266ec207854395693015acbd293"
  question_raw: "Will Tesla deliver between 400000 and 425000 vehicles in Q2 2026"
  current_price: 0.289
  volume_24h_usd: 10309.068382
  volume_cumulative_usd: 27592.236915000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket at 29%, modest plurality implies this band is the modal miss scenario among bearish delivery views."
  - "$10K in 24h equals 37% of all-time volume; activity concentrated at the wire with hours left in Q2."
  - "Combined with the ≥475K contract (Spike 2 at 26%), capital is distributing across miss scenarios rather than committing to one."
  - "Resolves on Q2 delivery report; band specificity makes this a precision trade on production output."
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
      poly_vol_24h_usd: 10309.068382
sources:
  - label: "ClearMarket market record: Will Tesla deliver between 350000 and 375000 vehicles i"
    url: "https://clearmarket.fyi/events/how-many-tesla-deliveries-in-q2-2026"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel late-session flows across multiple Tesla delivery bands suggest desks are hedging delivery uncertainty with a spread strategy rather than a single directional position.
