---
signal_id: "CMSIG20260727VS03"
signal_slug: "will-average-gas-prices-be-above-4-vol-22075"
headline: "US gas above $4.02: 99% on $22K volume"
semantic_title: "Gas prices staying above $4.02 draws near-certain odds"
telemetry: "99% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.02"
  question_raw: "Will average **gas prices** be above $4.02?"
  current_price: 0.99
  volume_24h_usd: 22075.61
  volume_cumulative_usd: 30913.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average US gas above $4.02 at 99%, market treats this as a foregone conclusion."
  - "24h volume $22K is 71% of all-time, indicating fresh late-cycle positioning on a near-expired contract."
  - "Current pump prices running well above the $4.02 threshold make this essentially a cash collection."
  - "Resolution tied to next EIA weekly average print."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 22075.61
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 99% with heavy all-time volume, this is liquidity-seeking on a near-certain outcome, desks can use the cluster of gas-price contracts to triangulate where the market sees the first real uncertainty threshold.
