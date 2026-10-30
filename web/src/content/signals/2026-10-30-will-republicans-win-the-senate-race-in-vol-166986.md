---
signal_id: "CMSIG20261030VS01"
signal_slug: "will-republicans-win-the-senate-race-in-vol-166986"
headline: "MS Senate GOP: 89% on $167K Kalshi surge"
semantic_title: "Mississippi Senate stays a safe GOP hold at 89%"
telemetry: "89% · $167K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.89
  volume_24h_usd: 166986.26
  volume_cumulative_usd: 530080.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "89% prices Mississippi Senate as a strong but not certain Republican retention."
  - "$167K in 24h represents 32% of all-time volume, notable fresh interest on a presumed safe seat."
  - "Volume on a high-conviction race suggests portfolio rebalancing or late hedging activity."
  - "Resolves on Mississippi Senate election outcome."
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
      kalshi_vol_24h_usd: 166986.26
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume on a near-locked Republican seat suggests desks are using Mississippi as a low-volatility hedge leg within a broader Senate-control basket.
