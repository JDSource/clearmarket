---
signal_id: "CMSIG20261030VS07"
signal_slug: "will-the-republican-party-win-the-govern-vol-58991"
headline: "TN GOP governor: 94% on $59K Kalshi spike"
semantic_title: "Tennessee governor stays a GOP lock at 94%"
telemetry: "94% · $59K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-S594KBZJM4"
event_slug: "govpartytn-26"
event_question: "Will there be a new Tennessee Governor by 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYTN-26-R"
  question_raw: "Will the Republican party win the governorship in Tennessee"
  current_price: 0.936
  volume_24h_usd: 58991.29
  volume_cumulative_usd: 168506.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-19T15:00:00Z"
bullets:
  - "94% prices Tennessee's governorship as a safe Republican hold with minimal upset risk."
  - "$59K in 24h is 35% of all-time volume, steady late-cycle interest on a low-volatility contract."
  - "Volume on a high-conviction, non-competitive race suggests basket-level Senate/governor positioning."
  - "Resolves on certified Tennessee gubernatorial election result."
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
      kalshi_vol_24h_usd: 58991.29
sources:
  - label: "ClearMarket market record: Will there be a new Tennessee Governor by 2027?"
    url: "https://clearmarket.fyi/events/govpartytn-26"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Moderate volume on a 94% gubernatorial contract is consistent with desks assembling or unwinding Republican-sweep baskets rather than expressing a standalone Tennessee view.
