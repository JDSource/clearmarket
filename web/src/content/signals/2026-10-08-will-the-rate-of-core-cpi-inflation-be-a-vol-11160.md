---
signal_id: "CMSIG20261008VS04"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-11160"
headline: "Core CPI >2.4% Sep yr: 47% on $11K"
semantic_title: "Core CPI above 2.4% for the year ending September sits near 50%"
telemetry: "47% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-M6P410PY45"
event_slug: "kxcpicoreyoy-26sep"
event_question: "Will core inflation in September 2026 (Core CPI YoY) meet the specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26SEP-T2.4"
  question_raw: "Will the rate of core CPI inflation be above 2.4% for the year ending in September 2026?"
  current_price: 0.47
  volume_24h_usd: 11160.35
  volume_cumulative_usd: 37591.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-21T14:00:00Z"
bullets:
  - "Market at 47%, nearly coin-flip on whether trailing 12-month core CPI clears the 2.4% line."
  - "24h volume of $11K is 30% of all-time, meaningful single-session flow ahead of the September CPI release."
  - "September CPI data due imminently; traders are squaring positions on the inflation threshold call."
  - "Resolves on BLS September CPI annual core rate print."
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
      kalshi_vol_24h_usd: 11160.35
sources:
  - label: "ClearMarket market record: Will core inflation in September 2026 (Core CPI YoY) me"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26sep"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-50% pricing with a 30% all-time volume day reflects maximum uncertainty on the core inflation threshold, desks should flag this as a live macro binary ahead of the print.
