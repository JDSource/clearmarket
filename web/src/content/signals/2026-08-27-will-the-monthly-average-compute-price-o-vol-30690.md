---
signal_id: "CMSIG20260827VS01"
signal_slug: "will-the-monthly-average-compute-price-o-vol-30690"
headline: "H200 above $3.50: 99% on $31K late surge"
semantic_title: "H200 compute above $3.50 in August draws heavy late bets"
telemetry: "99% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-0T7SDX2738"
event_slug: "kxh200ms-26aug"
event_question: "Will the NVIDIA H200 average hourly price in August reach a specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200MS-26AUG-3.500"
  question_raw: "Will the monthly average compute price of NVIDIA's H200 be above $3.50 in August 2026?"
  current_price: 0.99
  volume_24h_usd: 30690.0
  volume_cumulative_usd: 34327.36
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 99%, market is equally confident the higher $3.50 threshold is cleared."
  - "24h volume hits 89% of all-time, the largest share in this batch, underscoring urgency."
  - "With August ending, observed compute prices likely already exceed $3.50, prompting flush of final trades."
  - "Resolves on August monthly average H200 compute price."
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
      kalshi_vol_24h_usd: 30690.0
sources:
  - label: "ClearMarket market record: Will the NVIDIA H200 average hourly price in August rea"
    url: "https://clearmarket.fyi/events/kxh200ms-26aug"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total all-time volume consumption in 24 hours signals a crowded exit, participants settling certainty positions before August closes, not debating the outcome.
