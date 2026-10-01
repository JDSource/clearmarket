---
signal_id: "CMSIG20261001VS03"
signal_slug: "will-cpi-rise-more-than-0-5-in-septembe-vol-20958"
headline: "Sept CPI above 0.5%: 57% on $21K Kalshi surge"
semantic_title: "Odds stay split on a hot September CPI above 0.5%"
telemetry: "57% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T07:48:14+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.5"
  question_raw: "Will CPI rise more than 0.5% in September 2026?"
  current_price: 0.57
  volume_24h_usd: 20958.65
  volume_cumulative_usd: 65993.61
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices September CPI rising more than 0.5% month-over-month at 57%, barely above a coin-flip."
  - "32% of all-time contract volume ($21K of $66K lifetime) printed in 24h, reflecting a fresh wave of interest."
  - "Near-50 pricing with a volume spike signals genuine disagreement, energy or shelter data likely driving the dispute."
  - "Resolves on the official BLS September 2026 CPI release; a hot print would pressure Fed rate-cut expectations."
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
      kalshi_vol_24h_usd: 20958.65
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-01T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A split market drawing fresh volume right at the data window tells a desk that CPI uncertainty is live and unresolved, meaningful for front-end rates positioning and any inflation-linked hedges into the print.
