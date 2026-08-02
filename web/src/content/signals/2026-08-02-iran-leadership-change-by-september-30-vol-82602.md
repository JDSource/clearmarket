---
signal_id: "CMSIG20260802VS01"
signal_slug: "iran-leadership-change-by-september-30-vol-82602"
headline: "Iran change by Sep 30: 7% on $83K volume"
semantic_title: "Traders back Iran regime change odds out to September at 7%"
telemetry: "7% · $83K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x094772b3529f455e881a4483eaf1c24266384f55e97c23f24f638f5726ba9920"
  question_raw: "Iran leadership change by September 30?"
  current_price: 0.07
  volume_24h_usd: 82602.58017000004
  volume_cumulative_usd: 288292.02262800006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices Iran leadership change by Sep 30 at 7%, still deep in long-shot territory but double the August contract."
  - "29% of all-time volume printed in 24h, a meaningful flush of capital into the extended time frame."
  - "The Aug/Sep spread (3% vs. 7%) implies the market assigns incremental probability to a window between September 1, 30 specifically."
  - "Resolves Sep 30; paired activity with Spike 0 suggests coordinated hedging across both horizons."
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
      poly_vol_24h_usd: 82602.58017000004
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes across both Iran contracts suggest desks are mapping tail-risk across a two-month window rather than taking a directional view on any single catalyst.
