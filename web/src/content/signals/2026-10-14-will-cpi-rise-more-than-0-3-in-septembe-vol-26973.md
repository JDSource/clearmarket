---
signal_id: "CMSIG20261014VS06"
signal_slug: "will-cpi-rise-more-than-0-3-in-septembe-vol-26973"
headline: "CPI >0.3% Sept 2026: 99% on $27K volume spike"
semantic_title: "September CPI above 0.3% trades at near-certainty on Kalshi"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.3"
  question_raw: "Will CPI rise more than 0.3% in September 2026?"
  current_price: 0.99
  volume_24h_usd: 26973.75
  volume_cumulative_usd: 70751.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "99% price means the market has fully priced a September CPI monthly gain above 0.3%, essentially a consensus fait accompli."
  - "24h volume of $27K is 38% of all-time handle, indicating fresh capital is still flowing in to lock the position."
  - "Spike likely follows a preview of component data, shelter, energy, or services prints, landing above threshold estimates."
  - "Resolves on BLS September CPI release; a sub-0.3% print would be a significant macro surprise against current consensus."
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
      kalshi_vol_24h_usd: 26973.75
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at 99% on a macro inflation contract signals that rates desks are using this as a hedge or confirmation vehicle, a sub-0.3% September print would be a high-impact surprise relative to current market positioning.
