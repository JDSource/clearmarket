---
signal_id: "CMSIG20261013VS06"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-20084"
headline: "Core CPI >2.4% yr/yr Sept: 44% on $20K"
semantic_title: "Core CPI above 2.4% for the year ending September sits near 50%"
telemetry: "44% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-M6P410PY45"
event_slug: "kxcpicoreyoy-26sep"
event_question: "Will core inflation in September 2026 (Core CPI YoY) meet the specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26SEP-T2.4"
  question_raw: "Will the rate of core CPI inflation be above 2.4% for the year ending in September 2026?"
  current_price: 0.44
  volume_24h_usd: 20084.28
  volume_cumulative_usd: 76491.19
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-21T14:00:00Z"
bullets:
  - "Kalshi prices annual core CPI above 2.4% through September at 44%, market nearly split on the threshold."
  - "$20K in 24h is 26% of all-time volume; fresh flow ahead of the BLS release reflects genuine macro uncertainty."
  - "The 2.4% line is a credible battleground given recent shelter disinflation vs. sticky services readings."
  - "Resolves on the official BLS year-over-year core CPI figure for September 2026."
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
      kalshi_vol_24h_usd: 20084.28
sources:
  - label: "ClearMarket market record: Will core inflation in September 2026 (Core CPI YoY) me"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26sep"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 44% and climbing in volume just ahead of the CPI print, this contract is a live macro signal for rates desks, a read above 2.4% would complicate the Fed's easing narrative meaningfully.
