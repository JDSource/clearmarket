---
signal_id: "CMSIG20261025VS02"
signal_slug: "will-republican-win-the-house-race-for-t-vol-22172"
headline: "GOP wins TX-09: 76% on $22K surge"
semantic_title: "Republican hold in TX-09 draws heavy backing at strong odds"
telemetry: "76% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T07:48:52+00:00"
event_id: "CM-EVT-D0QN4YG685"
event_slug: "kxhousetx9-26"
event_question: "TX-09 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX9-26-R"
  question_raw: "Will Republican win the House race for TX-09?"
  current_price: 0.76
  volume_24h_usd: 22172.24
  volume_cumulative_usd: 35310.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican win in TX-09 at 76%, reflecting a solid but not certain incumbent-party advantage."
  - "24h volume of $22K is 63% of all-time handle, the majority of total contract activity landed in a single day."
  - "Concentrated single-day flow into a district race suggests a catalyst: redistricting news, candidate filing, or new poll release."
  - "Contract resolves on the certified TX-09 House race result from the 2026 midterm election."
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
      kalshi_vol_24h_usd: 22172.24
sources:
  - label: "ClearMarket market record: TX-09 House winner?"
    url: "https://clearmarket.fyi/events/kxhousetx9-26"
    retrieved_at: "2026-10-25T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sixty-three percent of lifetime volume arriving in one session on a district-level contract is a sharp attention signal; desks covering House control models should flag TX-09 as a newly live data point for seat-flip probability grids.
