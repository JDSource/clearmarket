---
signal_id: "CMSIG20261013VS02"
signal_slug: "will-cpi-rise-more-than-0-2-in-septembe-vol-34084"
headline: "CPI >0.2% Sept: 99% on $34K inflow"
semantic_title: "September CPI above 0.2% trades as a near-certainty at 99%"
telemetry: "99% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.2"
  question_raw: "Will CPI rise more than 0.2% in September 2026?"
  current_price: 0.99
  volume_24h_usd: 34084.88
  volume_cumulative_usd: 62789.9
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices a September monthly CPI beat above 0.2% at 99%, essentially resolved pre-print."
  - "$34K in 24h volume is 54% of all-time, showing fresh positioning ahead of the imminent data release."
  - "Consensus forecasts and recent shelter/services readings make a sub-0.2% print highly implausible."
  - "Resolves on official BLS September 2026 CPI release."
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
      kalshi_vol_24h_usd: 34084.88
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume surging to 54% of all-time at 99% odds just before the CPI print suggests traders are locking in near-riskless positions, worth flagging for any desk running rates or inflation-linked exposure.
