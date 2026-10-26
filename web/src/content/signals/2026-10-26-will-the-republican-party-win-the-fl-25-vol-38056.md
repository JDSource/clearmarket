---
signal_id: "CMSIG20261026VS03"
signal_slug: "will-the-republican-party-win-the-fl-25-vol-38056"
headline: "GOP FL-25: 20% on $38K, 57% of all-time flow"
semantic_title: "GOP odds in FL-25 slip to 20% as fresh volume pours in"
telemetry: "20% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-HQP7KZ8L31"
event_slug: "fl-25-house-election-winner"
event_question: "Will the Republican candidate win the FL-25 House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x45d599b1d25f7c090ef0f40de0b728ec4cc91c9d6d6d17092d4c19e226100c24"
  question_raw: "Will the Republican Party win the FL-25 House seat?"
  current_price: 0.2
  volume_24h_usd: 38056.910107
  volume_cumulative_usd: 66228.797116
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 20%, the market prices Republicans as underdogs to flip or hold FL-25."
  - "57% of all-time volume arrived in 24 hours alongside the companion Democratic contract."
  - "FL-25 mirrors a Democrat-favored district; capital is re-rating the Republican path lower."
  - "Resolves on the 2026 FL-25 House general election result."
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
      poly_vol_24h_usd: 38056.910107
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the FL-25 House elect"
    url: "https://clearmarket.fyi/events/fl-25-house-election-winner"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired FL-25 spikes on both party contracts, with GOP at 20% and Democrat at 79%, indicate a coordinated re-pricing event, likely tied to candidate news or a fresh district poll.
