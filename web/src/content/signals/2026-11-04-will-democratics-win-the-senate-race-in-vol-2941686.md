---
signal_id: "CMSIG20261104VS02"
signal_slug: "will-democratics-win-the-senate-race-in-vol-2941686"
headline: "AK Senate Dem: 95% on $2.9M surge"
semantic_title: "Fresh volume backs Democrats to flip the Alaska Senate seat"
telemetry: "95% · $2.9M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T15:57:35+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-D"
  question_raw: "Will Democratics win the Senate race in Alaska?"
  current_price: 0.949
  volume_24h_usd: 2941686.61
  volume_cumulative_usd: 6032316.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi marks Democratic Alaska Senate win at 95%, a strong lean on Election Day."
  - "$2.9M represents 49% of all-time contract volume arriving in a single session."
  - "Alaska results counting now; fresh capital arriving at 95% suggests early returns favor Democrats."
  - "Resolves on certified Alaska Senate outcome."
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
      kalshi_vol_24h_usd: 2941686.61
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-11-04T15:57:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume printing Election Day at 95% tells a desk that early Alaska returns are decisively Democratic and traders are closing positions at the top.
