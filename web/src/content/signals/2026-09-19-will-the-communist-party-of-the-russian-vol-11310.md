---
signal_id: "CMSIG20260919VS05"
signal_slug: "will-the-communist-party-of-the-russian-vol-11310"
headline: "KPRF third in Duma: 5% on $11K volume"
semantic_title: "KPRF taking third-most Duma seats trades near zero"
telemetry: "5% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8dcf41c1c938ffcf4ed95da62baff3c17a102fb56a6fe524db23145213ffef0"
  question_raw: "Will the Communist Party of the Russian Federation (KPRF) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.05
  volume_24h_usd: 11310.630102
  volume_cumulative_usd: 26314.879510000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices the Communist Party (KPRF) finishing third in Duma seats at just 5%, near-total rejection."
  - "24h volume of $11K is 43% of all-time, a concentrated session betting heavily against this outcome."
  - "At 5%, the market treats KPRF's third-place finish as a tail scenario, likely displaced by New People."
  - "Resolves on official Russian State Duma seat counts, directly linked to Spike 4 pricing."
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
      poly_vol_24h_usd: 11310.630102
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The inverse of the New People surge, capital flowing in here at 5% is arbitrage-aware positioning that reinforces NL as the consensus third-place party, not KPRF.
