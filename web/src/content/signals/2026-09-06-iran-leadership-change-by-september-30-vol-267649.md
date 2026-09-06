---
signal_id: "CMSIG20260906VS00"
signal_slug: "iran-leadership-change-by-september-30-vol-267649"
headline: "Iran leadership by Sept 30: 3% on $268K surge"
semantic_title: "Traders pile into Iran leadership change by Sept 30"
telemetry: "3% · $268K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-06T11:54:44+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x094772b3529f455e881a4483eaf1c24266384f55e97c23f24f638f5726ba9920"
  question_raw: "Iran leadership change by September 30?"
  current_price: 0.029
  volume_24h_usd: 267649.945247
  volume_cumulative_usd: 1002771.940191
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Market prices near-zero odds, 3%, treating a September leadership change as a tail risk, not a base case."
  - "27% of all-time volume hit in 24 hours, signaling a sharp spike in fresh geopolitical attention."
  - "A catalyst, diplomatic, military, or domestic instability news, likely drove traders to price the tail."
  - "Contract resolves September 30; any headline in the next 24 days could reprice sharply from this floor."
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
      poly_vol_24h_usd: 267649.945247
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-09-06T11:54:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A geopolitical desk should treat this volume burst as an early-warning signal, someone is paying to own the tail, and fresh flow at 3% suggests news may be ahead of public consensus.
