---
signal_id: "CMSIG20260924VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-115785"
headline: "GOP Alaska Senate: 29% on $116K spike"
semantic_title: "Republicans slip to 29% in Alaska Senate as volume surges"
telemetry: "29% · $116K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T07:48:17+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-R"
  question_raw: "Will Republicans win the Senate race in Alaska?"
  current_price: 0.29
  volume_24h_usd: 115785.49
  volume_cumulative_usd: 328595.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Alaska Senate win at just 29%, making it a clear underdog contract."
  - "$115.8K in 24h represents 35% of all-time volume, the sharpest single-day interest to date."
  - "Elevated activity this far from November suggests new polling or candidate news is driving reassessment."
  - "Outcome resolves on Alaska 2026 general election results."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 115785.49
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-09-24T07:48:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Substantial fresh volume pricing Republicans below 30% in a traditionally safe Alaska seat warrants attention from political-risk desks monitoring Senate control probabilities.
