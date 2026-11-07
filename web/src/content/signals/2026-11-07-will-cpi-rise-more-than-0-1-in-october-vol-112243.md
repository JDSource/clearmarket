---
signal_id: "CMSIG20261107VS03"
signal_slug: "will-cpi-rise-more-than-0-1-in-october-vol-112243"
headline: "October CPI >0.1%: 93% on $112K surge"
semantic_title: "Buyers back a hot October CPI print above 0.1%"
telemetry: "93% · $112K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.1"
  question_raw: "Will CPI rise more than 0.1% in October 2026?"
  current_price: 0.93
  volume_24h_usd: 112243.28
  volume_cumulative_usd: 339468.96
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "Kalshi prices October CPI rising more than 0.1% at 93%, reflecting strong consensus for an above-floor print."
  - "$112K in 24h is 33% of all-time volume, a meaningful single-session share ahead of the data release."
  - "October CPI data is likely imminent or just released, driving last-minute positioning or resolution-adjacent flow."
  - "Contract resolves on the official BLS October 2026 CPI release."
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
      kalshi_vol_24h_usd: 112243.28
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering near 93% ahead of a CPI release tells a macro desk the market sees minimal risk of a sub-0.1% print; monitor for the actual BLS number to confirm or bust the consensus.
