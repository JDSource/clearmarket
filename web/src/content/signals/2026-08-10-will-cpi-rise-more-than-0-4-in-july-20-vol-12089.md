---
signal_id: "CMSIG20260810VS05"
signal_slug: "will-cpi-rise-more-than-0-4-in-july-20-vol-12089"
headline: "CPI rise above -0.4% in July: 98% on $12K surge"
semantic_title: "July CPI deflation floor bet holds near certainty at 98%"
telemetry: "98% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-10T09:15:14+00:00"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "CPI month-over-month change, July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T-0.4"
  question_raw: "Will CPI rise more than -0.4% in July 2026?"
  current_price: 0.98
  volume_24h_usd: 12089.28
  volume_cumulative_usd: 28630.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "Kalshi prices a July 2026 CPI reading above -0.4% month-over-month at 98%, near-certain the print will be less negative than that threshold."
  - "24h volume of $12K equals 42% of all-time handle, a notable concentration ahead of the July CPI release."
  - "Volume at 98% pricing suggests traders are positioning against a tail-risk deflation print, confirming consensus expectations of a mild or positive CPI."
  - "Resolves on the official BLS July 2026 CPI release; residual 2% risk reflects extreme-downside uncertainty only."
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
      kalshi_vol_24h_usd: 12089.28
sources:
  - label: "ClearMarket market record: CPI month-over-month change, July 2026"
    url: "https://clearmarket.fyi/events/kxcpi-26jul"
    retrieved_at: "2026-08-10T09:15:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certainty pricing with 42% of lifetime volume in one day tells a desk the market is treating this as a pre-release confirmation trade, worth monitoring for any surprise in the actual BLS print that could move adjacent rate contracts.
