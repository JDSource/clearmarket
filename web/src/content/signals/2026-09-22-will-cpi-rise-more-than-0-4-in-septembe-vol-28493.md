---
signal_id: "CMSIG20260922VS04"
signal_slug: "will-cpi-rise-more-than-0-4-in-septembe-vol-28493"
headline: "CPI above 0.4% in Sept 2026: 90% on $28K surge"
semantic_title: "Hot CPI bet prices above-0.4% September read at 90%"
telemetry: "90% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.4"
  question_raw: "Will CPI rise more than 0.4% in September 2026?"
  current_price: 0.9
  volume_24h_usd: 28493.9
  volume_cumulative_usd: 63698.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "At 90%, Kalshi traders are near-certain September CPI will print above the 0.4% month-over-month threshold."
  - "45% of all-time volume entered in 24 hours, this contract is drawing fresh capital rapidly approaching resolution."
  - "September CPI data is due within weeks; positioning at 90% implies strong consensus around a hot print."
  - "Resolves on Bureau of Labor Statistics September 2026 CPI release."
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
      kalshi_vol_24h_usd: 28493.9
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 90% price on an above-threshold CPI print, with nearly half of all-time volume arriving in one session, is a macro signal a rates desk cannot ignore, traders are pricing a hot September number as base case.
