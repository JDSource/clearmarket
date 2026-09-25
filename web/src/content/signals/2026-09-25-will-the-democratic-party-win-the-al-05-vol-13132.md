---
signal_id: "CMSIG20260925VS06"
signal_slug: "will-the-democratic-party-win-the-al-05-vol-13132"
headline: "AL-05 Dem House: 3% on $13K Polymarket surge"
semantic_title: "AL-05 Democratic House bid stays a long shot at 3%"
telemetry: "3% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-LN7341VVS9"
event_slug: "al-05-house-election-winner"
event_question: "Will a Republican win the AL-05 House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x983d15d52f8780293cfb996daee22ce1327bf5349ac473b02c6ef07829ffb6f0"
  question_raw: "Will the Democratic Party win the AL-05 House seat?"
  current_price: 0.03
  volume_24h_usd: 13132.05889
  volume_cumulative_usd: 34994.951516
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic win at 3%, placing AL-05 firmly in near-certain Republican territory for a deep-red Alabama district."
  - "24h volume of $13K represents 38% of all-time handle, a notable surge for a contract priced at near-zero."
  - "Volume spikes on near-zero contracts often signal a specific event, candidate disqualification, scandal, or filing change, that prompted a reassessment."
  - "Resolves on the 2026 AL-05 general election result."
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
      poly_vol_24h_usd: 13132.05889
sources:
  - label: "ClearMarket market record: Will a Republican win the AL-05 House election in 2026?"
    url: "https://clearmarket.fyi/events/al-05-house-election-winner"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 38% all-time volume day on a 3% contract is anomalous; a desk should investigate whether there is a candidate-level development in AL-05 that briefly raised Democratic prospects before being discounted.
