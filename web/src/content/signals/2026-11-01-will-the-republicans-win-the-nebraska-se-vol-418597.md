---
signal_id: "CMSIG20261101VS01"
signal_slug: "will-the-republicans-win-the-nebraska-se-vol-418597"
headline: "Nebraska Senate GOP: 74% on $419K volume"
semantic_title: "Traders pile into Nebraska Senate as GOP odds hold at 74%"
telemetry: "74% · $419K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x71e9f5312aac62bdc9b87fa8d171fa929eca6243d815298c4c7d61303f7d53dd"
  question_raw: "Will the Republicans win the Nebraska Senate race in 2026?"
  current_price: 0.74
  volume_24h_usd: 418597.9467750002
  volume_cumulative_usd: 1188158.589333
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 74%, Polymarket prices Nebraska as a likely Republican hold with meaningful residual risk."
  - "$419K in 24h, 35% of all-time, marks the heaviest single-day session on this contract."
  - "Surge likely tied to candidate-field clarity or independent threat reassessment in the state."
  - "Resolves on the November 2026 election result."
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
      poly_vol_24h_usd: 418597.9467750002
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

35% of all-time volume in one session on a 74% GOP contract points to active hedging between the Republican and independent legs of the Nebraska race.
