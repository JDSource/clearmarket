---
signal_id: "CMSIG20261116VS00"
signal_slug: "will-cpi-rise-more-than-0-1-in-novembe-vol-15265"
headline: "Nov CPI above -0.1%: 59% on $15K volume surge"
semantic_title: "Traders back a November CPI beat above -0.1%"
telemetry: "59% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-16T07:48:36+00:00"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "Will the Consumer Price Index be released for November?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in November 2026?"
  current_price: 0.59
  volume_24h_usd: 15265.09
  volume_cumulative_usd: 45992.94
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi prices a November CPI print above -0.1% at 59%, implying traders expect deflation to undershoot consensus."
  - "24h volume of $15K represents 33% of all-time contract volume, a sharp concentration of fresh capital."
  - "November CPI data release imminent; heavy positioning suggests desks are hedging macro rate-path risk ahead of the print."
  - "Contract resolves on official BLS November 2026 CPI release."
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
      kalshi_vol_24h_usd: 15265.09
sources:
  - label: "ClearMarket market record: Will the Consumer Price Index be released for November?"
    url: "https://clearmarket.fyi/events/kxcpi-26nov"
    retrieved_at: "2026-11-16T07:48:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third-of-lifetime volume burst in a single session signals active macro desks are taking directional positions on the November CPI print, likely tied to Fed policy expectations and near-term rates positioning.
