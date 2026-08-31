---
signal_id: "CMSIG20260831VS02"
signal_slug: "will-russia-enter-pokrovskoe-by-december-vol-10438"
headline: "Russia takes Pokrovskoe by Dec: 20% on $10K"
semantic_title: "Odds stay low as fresh volume tests the Pokrovskoe advance"
telemetry: "20% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-31T15:48:06+00:00"
event_id: "CM-EVT-BZ1CKVQNR0"
event_slug: "will-russia-enter-pokrovskoe-by"
event_question: "Will Russia enter Pokrovskoe by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3ab254eba59333a4165e744c03eb523591d5beb52475ac79d3521ab97f06f103"
  question_raw: "Will Russia enter Pokrovskoe by December 31, 2026?"
  current_price: 0.2
  volume_24h_usd: 10438.42
  volume_cumulative_usd: 19106.482546999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Russian capture of Pokrovskoe by December 31 at just 20%, market leans against."
  - "24h volume of $10.4K is 55% of all-time, indicating this contract is newly active."
  - "Fresh attention likely follows a battlefield development or logistics report near the town."
  - "Resolves December 31, 2026, on confirmed territorial control."
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
      poly_vol_24h_usd: 10438.42
sources:
  - label: "ClearMarket market record: Will Russia enter Pokrovskoe by the settlement date?"
    url: "https://clearmarket.fyi/events/will-russia-enter-pokrovskoe-by"
    retrieved_at: "2026-08-31T15:48:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of lifetime volume arriving today on a low-probability contract suggests new geopolitical information is circulating, desks tracking Eastern European risk should treat this as an early signal worth monitoring.
