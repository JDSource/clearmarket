---
signal_id: "CMSIG20261004VS04"
signal_slug: "will-flavio-bolsonaro-qualify-for-brazil-vol-56923"
headline: "F. Bolsonaro runoff: 98% on $57K volume"
semantic_title: "Flávio Bolsonaro runoff qualification priced near certain at 98%"
telemetry: "98% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-J1PPP75GK3"
event_slug: "which-candidates-will-advance-to-brazils-presidential-runoff"
event_question: "Will two candidates advance to Brazil's presidential runoff?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x023a8c2fd2a78c29c9748a44205e2cbe624d86c11ee41b81d4067ddbbf2a135f"
  question_raw: "Will Flavio Bolsonaro qualify for Brazil's presidential runoff?"
  current_price: 0.985
  volume_24h_usd: 56923.98493499999
  volume_cumulative_usd: 218343.6624069999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Flávio Bolsonaro qualifying for a presidential runoff at 98%, treating it as a virtual lock."
  - "$56,924 in 24h is 26% of all-time volume, confirming traders are actively reaffirming, not just passively holding, this near-certainty."
  - "High confidence in runoff qualification aligns with polling showing Bolsonaro as the clear second-place consolidator on the right."
  - "Resolves YES if Flávio Bolsonaro finishes top-two in the first round."
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
      poly_vol_24h_usd: 56923.98493499999
sources:
  - label: "ClearMarket market record: Will two candidates advance to Brazil's presidential ru"
    url: "https://clearmarket.fyi/events/which-candidates-will-advance-to-brazils-presidential-runoff"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain runoff pricing with fresh volume activity suggests the market is stress-testing this assumption against a new data point, desks should check whether any eligibility or coalition news could disrupt the consensus.
