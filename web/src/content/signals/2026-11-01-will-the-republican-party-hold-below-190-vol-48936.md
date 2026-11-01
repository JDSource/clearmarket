---
signal_id: "CMSIG20261101VS06"
signal_slug: "will-the-republican-party-hold-below-190-vol-48936"
headline: "GOP below 190 seats: 36% on $49K inflow"
semantic_title: "Betting picks up on Republicans staying under 190 House seats"
telemetry: "36% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-HZZP4JMQ30"
event_slug: "republican-house-seats-after-the-2026-midterm-elections"
event_question: "Will Republicans win more than 218 House seats in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa2e43598547f2e90e3eee195812c8814202b9b66f6c540d7e15a265cbe93f68f"
  question_raw: "Will the Republican Party hold below 190 House seats after the 2026 midterm elections?"
  current_price: 0.36
  volume_24h_usd: 48936.621236
  volume_cumulative_usd: 145607.22959499998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 36%, Polymarket says there is a meaningful but minority chance Republicans fall under 190 seats after 2026."
  - "$49K in 24h, 34% of all-time, signals renewed interest in downside Republican House scenarios."
  - "Sub-190 pricing is a direct proxy for the probability of a Democratic House takeover of substantial size."
  - "Resolves after all 2026 midterm House seats are called."
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
      poly_vol_24h_usd: 48936.621236
sources:
  - label: "ClearMarket market record: Will Republicans win more than 218 House seats in the 2"
    url: "https://clearmarket.fyi/events/republican-house-seats-after-the-2026-midterm-elections"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 36% price on sub-190 GOP seats combined with a volume surge tells desks the market sees a Democratic House sweep as a live tail risk worth hedging into the midterm cycle.
