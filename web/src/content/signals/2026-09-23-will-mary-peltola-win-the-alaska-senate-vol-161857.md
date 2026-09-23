---
signal_id: "CMSIG20260923VS00"
signal_slug: "will-mary-peltola-win-the-alaska-senate-vol-161857"
headline: "Peltola AK Senate: 79% on heavy $162K session"
semantic_title: "Peltola holds a strong lead in the Alaska Senate race"
telemetry: "79% · $162K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-FSS872PZ65"
event_slug: "alaska-senate-election-winner"
event_question: "Alaska Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x19d2ff72e389d190c183e6b114817301d29eba651d67d75a38ee201a05188fd9"
  question_raw: "Will Mary Peltola win the Alaska Senate race in 2026?"
  current_price: 0.79
  volume_24h_usd: 161857.944001
  volume_cumulative_usd: 546852.6613190001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 79%, Polymarket treats Peltola as a near-certain winner of the 2026 Alaska Senate seat."
  - "24h volume of $162K equals 30% of all-time handle, a major single-session commitment."
  - "Fresh capital at elevated odds suggests the market is absorbing new polling or campaign news backing her position."
  - "Contract resolves on the November 2026 Alaska Senate election result."
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
      poly_vol_24h_usd: 161857.944001
sources:
  - label: "ClearMarket market record: Alaska Senate Election Winner"
    url: "https://clearmarket.fyi/events/alaska-senate-election-winner"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that sustained high-conviction pricing above 75% with a large volume flush typically precedes a news catalyst confirming frontrunner status, worth monitoring Alaska polling drops.
