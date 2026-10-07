---
signal_id: "CMSIG20261007VS02"
signal_slug: "will-cpi-rise-more-than-0-4-in-septembe-vol-42871"
headline: "Sept CPI >0.4%: 83% on $42K inflow"
semantic_title: "Traders back a September CPI print above 0.4%"
telemetry: "83% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T07:48:37+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.4"
  question_raw: "Will CPI rise more than 0.4% in September 2026?"
  current_price: 0.83
  volume_24h_usd: 42871.41
  volume_cumulative_usd: 163565.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "83% odds indicate strong consensus that September CPI clears the 0.4% month-over-month bar."
  - "24h volume of $42K equals 26% of all-time, a notable single-session share ahead of the data release."
  - "Paired with the near-50% contract at 0.5%, the spread implies the market expects a print in the 0.4, 0.5% corridor."
  - "Resolves on BLS September 2026 CPI release."
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
      kalshi_vol_24h_usd: 42871.41
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-07T07:48:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Reading both CPI contracts together, a desk can infer the market's modal inflation forecast sits between 0.4% and 0.5%, useful calibration ahead of the print.
