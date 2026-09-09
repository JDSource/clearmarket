---
signal_id: "CMSIG20260909VS00"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-73026"
headline: "NJ-7 Democrat: 71% on dominant $73K surge"
semantic_title: "Democrats hold heavy odds in NJ-7 House race"
telemetry: "71% · $73K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-P0428D3JR9"
event_slug: "housenj7-26"
event_question: "Who will win the New Jersey 7th Congressional District House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENJ7-26-D"
  question_raw: "Will Democratic win the House race for NJ-7?"
  current_price: 0.71
  volume_24h_usd: 73026.78
  volume_cumulative_usd: 86974.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 71%, a solid but not decisive lead with two months to Election Day."
  - "84% of all-time contract volume hit in 24h, a near-total lifecycle flush into one session."
  - "NJ-7 is a perennial swing district; concentrated late volume suggests fresh polling or candidate news."
  - "Resolves on 2026 midterm Election Night results for New Jersey's 7th Congressional District."
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
      kalshi_vol_24h_usd: 73026.78
sources:
  - label: "ClearMarket market record: Who will win the New Jersey 7th Congressional District "
    url: "https://clearmarket.fyi/events/housenj7-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag this as a district moving from background noise to active pricing, the near-exhaustion of all-time volume in one day demands attention to any imminent NJ-7 news catalyst.
