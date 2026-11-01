---
signal_id: "CMSIG20261101VS05"
signal_slug: "will-the-republican-party-win-the-fl-09-vol-29499"
headline: "FL-09 GOP seat: 65% on $29K surge"
semantic_title: "FL-09 Republican odds hold at 65% through a volume surge"
telemetry: "65% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-3ZLX48RMQ5"
event_slug: "fl-09-house-election-winner"
event_question: "Will the winner of the FL-09 House election be determined by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2c93da161ae234a971d93533333455c8fa79804ba7592503a22cde151b1b8e6f"
  question_raw: "Will the Republican Party win the FL-09 House seat?"
  current_price: 0.65
  volume_24h_usd: 29499.250142000004
  volume_cumulative_usd: 52699.80272300001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 65%, Polymarket prices FL-09 as a likely but not certain Republican pickup or hold."
  - "$29K in 24h, 56% of all-time, makes this the most concentrated single-day session on the contract."
  - "FL-09 activity may reflect candidate development or district-level demographic data drawing fresh scrutiny."
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
      poly_vol_24h_usd: 29499.250142000004
sources:
  - label: "ClearMarket market record: Will the winner of the FL-09 House election be determin"
    url: "https://clearmarket.fyi/events/fl-09-house-election-winner"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume printing in one day on a mid-tier House contract is a strong signal that FL-09 has entered active monitoring for those building House-majority models.
