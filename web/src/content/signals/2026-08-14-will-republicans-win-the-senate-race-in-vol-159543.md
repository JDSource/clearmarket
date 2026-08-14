---
signal_id: "CMSIG20260814VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-159543"
headline: "Iowa Senate (R): 57% on $160K volume surge"
semantic_title: "Republicans lead the Iowa Senate race at 57%"
telemetry: "57% · $160K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-R8V0583H75"
event_slug: "senateia-26"
event_question: "Iowa Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEIA-26-R"
  question_raw: "Will Republicans win the Senate race in Iowa?"
  current_price: 0.57
  volume_24h_usd: 159543.71
  volume_cumulative_usd: 480467.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "57% implies GOP is modest favorite, well short of lock status."
  - "$160K traded in 24h, 33% of all-time volume floods in at once."
  - "Late-summer Senate map attention; Iowa suddenly a live battleground watch."
  - "Resolves on November 2026 general election result."
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
      kalshi_vol_24h_usd: 159543.71
sources:
  - label: "ClearMarket market record: Iowa Senate winner?"
    url: "https://clearmarket.fyi/events/senateia-26"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-day volume equal to a third of all-time flow signals desks are repricing Iowa Senate competitiveness ahead of fall campaign developments.
