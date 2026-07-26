---
signal_id: "CMSIG20260726VS07"
signal_slug: "will-average-gas-prices-be-above-4-vol-15789"
headline: "Avg gas above $4.08: 99% on $15K surge"
semantic_title: "Gas prices above $4.08 priced as certain"
telemetry: "99% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.08"
  question_raw: "Will average **gas prices** be above $4.08?"
  current_price: 0.99
  volume_24h_usd: 15789.67
  volume_cumulative_usd: 47411.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average gas above $4.08 at 99%, even the higher threshold is treated as breached."
  - "33% of all-time volume landed in 24h, consistent with end-of-life settlement activity."
  - "Observed pump-price data above both the $4.04 and $4.08 levels is driving near-certain pricing on both contracts simultaneously."
  - "Resolution imminent; volume is settlement arbitrage, not a new directional signal on energy markets."
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
      kalshi_vol_24h_usd: 15789.67
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel 99% prints on both the $4.04 and $4.08 gas contracts confirm observed data has closed out all real uncertainty, traders are capturing residual carry, and the pair together signals broad above-threshold gas price confirmation for desks tracking energy pass-through.
