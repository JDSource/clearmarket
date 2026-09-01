---
signal_id: "CMSIG20260901VS01"
signal_slug: "will-russia-enter-pokrovskoe-by-december-vol-10130"
headline: "Russia takes Pokrovskoe by Dec 31: 20% on $10K"
semantic_title: "Odds hold low as fresh volume tests Russia at Pokrovskoe"
telemetry: "20% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-01T13:00:43+00:00"
event_id: "CM-EVT-BZ1CKVQNR0"
event_slug: "will-russia-enter-pokrovskoe-by"
event_question: "Will Russia enter Pokrovskoe by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3ab254eba59333a4165e744c03eb523591d5beb52475ac79d3521ab97f06f103"
  question_raw: "Will Russia enter Pokrovskoe by December 31, 2026?"
  current_price: 0.2
  volume_24h_usd: 10130.0
  volume_cumulative_usd: 19236.482547
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "20% price reflects the market treating a Russian capture of Pokrovskoe by year-end as an unlikely but non-trivial scenario."
  - "24h volume of $10K is 53% of all-time, more than half the contract's entire history traded in one day, signaling a sharp spike in attention."
  - "A burst of volume at this size on a thin contract typically precedes or follows a battlefield development or credible field report."
  - "Contract resolves December 31, 2026, on confirmed Russian control of the settlement."
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
      poly_vol_24h_usd: 10130.0
sources:
  - label: "ClearMarket market record: Will Russia enter Pokrovskoe by the settlement date?"
    url: "https://clearmarket.fyi/events/will-russia-enter-pokrovskoe-by"
    retrieved_at: "2026-09-01T13:00:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 53% of all-time volume prints in 24 hours on a thin geopolitical contract, desks should cross-reference frontline mapping sources, this level of attention on a low-liquidity line often precedes a news catalyst.
