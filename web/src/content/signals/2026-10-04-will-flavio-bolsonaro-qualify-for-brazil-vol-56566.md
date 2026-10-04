---
signal_id: "CMSIG20261004VS04"
signal_slug: "will-flavio-bolsonaro-qualify-for-brazil-vol-56566"
headline: "F. Bolsonaro qualifies runoff: 97% on $57K"
semantic_title: "Flavio Bolsonaro runoff qualifying priced at 97%"
telemetry: "97% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-J1PPP75GK3"
event_slug: "which-candidates-will-advance-to-brazils-presidential-runoff"
event_question: "Will two candidates advance to Brazil's presidential runoff?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x023a8c2fd2a78c29c9748a44205e2cbe624d86c11ee41b81d4067ddbbf2a135f"
  question_raw: "Will Flavio Bolsonaro qualify for Brazil's presidential runoff?"
  current_price: 0.971
  volume_24h_usd: 56566.752005
  volume_cumulative_usd: 216138.15888899995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Flavio Bolsonaro reaching Brazil's presidential runoff at 97%, near certainty."
  - "26% of all-time volume hit in 24h, affirming the market has little doubt about this outcome."
  - "Volume likely reflects traders hedging or closing positions as the question nears resolution."
  - "Resolves on official Brazilian first-round results in 2026."
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
      poly_vol_24h_usd: 56566.752005
sources:
  - label: "ClearMarket market record: Will two candidates advance to Brazil's presidential ru"
    url: "https://clearmarket.fyi/events/which-candidates-will-advance-to-brazils-presidential-runoff"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% contract drawing 26% of its all-time volume in one day signals desks are treating Flavio Bolsonaro's runoff qualification as settled and positioning around downstream Brazil election contracts instead.
