---
signal_id: "CMSIG20261007VS00"
signal_slug: "will-cpi-rise-more-than-0-5-in-septembe-vol-71198"
headline: "Sept CPI >0.5%: 49% on $71K volume surge"
semantic_title: "CPI above 0.5% in September sits at a coin-flip"
telemetry: "49% · $71K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T15:02:49+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.5"
  question_raw: "Will CPI rise more than 0.5% in September 2026?"
  current_price: 0.49
  volume_24h_usd: 71198.97
  volume_cumulative_usd: 160315.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices the September CPI overshoot at 49%, effectively dead even, implying no consensus on a hot print."
  - "24h volume of $71K is 44% of all-time handle, marking this as the sharpest single-day interest the contract has seen."
  - "September CPI data is imminent, drawing traders to stake out positions before the release resolves the contract."
  - "Resolves on official BLS September 2026 CPI print; a >0.5% month-over-month rise needed for YES."
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
      kalshi_vol_24h_usd: 71198.97
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-07T15:02:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even pricing on heavy volume signals genuine macro uncertainty heading into the CPI print, a desk should treat this as a live rate-path signal, not a settled view.
