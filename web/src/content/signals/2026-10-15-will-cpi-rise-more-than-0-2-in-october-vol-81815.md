---
signal_id: "CMSIG20261015VS00"
signal_slug: "will-cpi-rise-more-than-0-2-in-october-vol-81815"
headline: "October CPI >0.2%: 51% on heavy Kalshi surge"
semantic_title: "October CPI above 0.2% sits right at a coin flip"
telemetry: "51% · $82K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.2"
  question_raw: "Will CPI rise more than 0.2% in October 2026?"
  current_price: 0.51
  volume_24h_usd: 81815.2
  volume_cumulative_usd: 104588.93
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "Kalshi prices a >0.2% October CPI print at 51%, effectively no edge either way."
  - "24h volume of $81.8K is 78% of all-time, signaling concentrated fresh positioning."
  - "Mid-October timing aligns with pre-release inflation hedging ahead of the November CPI report."
  - "Resolves on official BLS October CPI release, likely mid-November."
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
      kalshi_vol_24h_usd: 81815.2
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds with most of the contract's lifetime volume printing in a single day flags CPI directional uncertainty as a live macro hedging event, desks should watch for correlated rate-vol positioning.
