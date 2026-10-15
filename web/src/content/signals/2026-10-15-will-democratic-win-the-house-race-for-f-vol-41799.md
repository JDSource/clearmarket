---
signal_id: "CMSIG20261015VS05"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-41799"
headline: "FL-25 Dem win: 79% on $41.8K Kalshi activity"
semantic_title: "FL-25 Democratic odds hold firm through a volume push"
telemetry: "79% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-D"
  question_raw: "Will Democratic win the House race for FL-25?"
  current_price: 0.79
  volume_24h_usd: 41799.83
  volume_cumulative_usd: 155835.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Democrats at 79% in FL-25, market leans clearly blue but retains meaningful Republican tail risk."
  - "$41.8K in 24h is 27% of all-time, steady rather than extreme but still the contract's busiest recent stretch."
  - "A Florida seat with residual uncertainty at 79% flags either a credible Republican challenger or shifting local fundamentals."
  - "Resolves on 2026 FL-25 House election result."
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
      kalshi_vol_24h_usd: 41799.83
sources:
  - label: "ClearMarket market record: Will the Florida 25th House seat be won in the next ele"
    url: "https://clearmarket.fyi/events/kxhouserace-fl25-26"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained volume at a 79% Democratic price in a Florida district is worth monitoring, that level of uncertainty in a nominally blue seat could reflect a competitive challenger narrative not yet fully reflected in polling.
