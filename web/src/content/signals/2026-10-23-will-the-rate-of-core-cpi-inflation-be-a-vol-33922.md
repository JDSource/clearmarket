---
signal_id: "CMSIG20261023VS03"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-33922"
headline: "Core CPI >2.2% Nov: 99% on $34K, 76% of all-time"
semantic_title: "Core CPI above 2.2% through November stays the heavy favorite"
telemetry: "99% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Will core inflation in November 2026 be measured by Core CPI year-over-year change?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.2"
  question_raw: "Will the rate of core CPI inflation be above 2.2% for the year ending in November 2026?"
  current_price: 0.99
  volume_24h_usd: 33922.15
  volume_cumulative_usd: 44491.97
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "99% price on Kalshi means the market treats above-2.2% core CPI for the year ending November as essentially certain."
  - "$33,922 in 24h volume is a striking 76% of all-time handle, nearly the entire lifetime of this market turned over today."
  - "Likely triggered by an October CPI print or Fed communication reinforcing sticky inflation expectations."
  - "Resolves on BLS core CPI release covering the year ending November 2026."
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
      kalshi_vol_24h_usd: 33922.15
sources:
  - label: "ClearMarket market record: Will core inflation in November 2026 be measured by Cor"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26nov"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 76% all-time volume flush into a 99% contract is a strong signal that a macro catalyst, likely a CPI print, just confirmed inflation persistence; desks should treat this as a real-money inflation-expectations read.
