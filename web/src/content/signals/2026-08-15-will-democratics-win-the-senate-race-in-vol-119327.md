---
signal_id: "CMSIG20260815VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-119327"
headline: "Iowa Senate Dem win: 45% on $119K surge"
semantic_title: "Democrats trail in Iowa Senate but odds stay close to 50%"
telemetry: "45% · $119K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-15T08:22:27+00:00"
event_id: "CM-EVT-R8V0583H75"
event_slug: "senateia-26"
event_question: "Iowa Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEIA-26-D"
  question_raw: "Will Democratics win the Senate race in Iowa?"
  current_price: 0.45
  volume_24h_usd: 119327.27
  volume_cumulative_usd: 338955.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "45% price puts Democrats just below even money, signaling a genuine toss-up with a slight Republican lean."
  - "24h volume of $119K is 35% of all-time contract volume, marking one of the heaviest single-day sessions on Kalshi."
  - "Mid-August attention spike suggests a catalyst, candidate news, polling, or fundraising disclosure, is drawing fresh capital."
  - "Contract resolves on Iowa 2026 general election result."
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
      kalshi_vol_24h_usd: 119327.27
sources:
  - label: "ClearMarket market record: Iowa Senate winner?"
    url: "https://clearmarket.fyi/events/senateia-26"
    retrieved_at: "2026-08-15T08:22:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds absorbing a major volume day means the Iowa Senate race is being actively re-priced as competitive, warranting close monitoring for any polling or news catalyst that could break the 50% threshold.
