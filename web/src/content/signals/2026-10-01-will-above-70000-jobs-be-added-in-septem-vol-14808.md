---
signal_id: "CMSIG20261001VS04"
signal_slug: "will-above-70000-jobs-be-added-in-septem-vol-14808"
headline: "Sept jobs above 70K: 67% on $15K surge"
semantic_title: "September jobs above 70K holds a clear majority price"
telemetry: "67% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T15:04:01+00:00"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "Will the September 2026 jobs report show positive job growth?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T70000"
  question_raw: "Will above 70000 jobs be added in September 2026?"
  current_price: 0.67
  volume_24h_usd: 14808.93
  volume_cumulative_usd: 22446.33
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi prices a 67% chance September 2026 payrolls come in above 70,000, a majority lean but far from a lock."
  - "24h volume of $15K is 66% of all-time, suggesting the contract is drawing concentrated late-stage positioning."
  - "Timing on Oct 1 points directly to imminent September jobs data; this is classic pre-release positioning."
  - "Resolves on the September employment report; a miss below 70K would be a sharp repricing event."
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
      kalshi_vol_24h_usd: 14808.93
sources:
  - label: "ClearMarket market record: Will the September 2026 jobs report show positive job g"
    url: "https://clearmarket.fyi/events/kxpayrolls-26sep"
    retrieved_at: "2026-10-01T15:04:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 66%-of-all-time volume day directly ahead of the jobs print tells desks this contract is live event-risk exposure, the 67% price implies a modest but priced-in labor market softening relative to prior months.
