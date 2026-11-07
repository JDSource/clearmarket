---
signal_id: "CMSIG20261107VS07"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-15672"
headline: "Core CPI above 2.5% thru Nov: 99% on $16K Kalshi surge"
semantic_title: "Core CPI above 2.5% for the year ending November stays a near-lock"
telemetry: "99% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Will core inflation in November 2026 be measured by Core CPI year-over-year change?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.5"
  question_raw: "Will the rate of core CPI inflation be above 2.5% for the year ending in November 2026?"
  current_price: 0.99
  volume_24h_usd: 15672.69
  volume_cumulative_usd: 28498.82
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "99% pricing is effectively a resolved trade, market sees above-2.5% core as certain."
  - "Kalshi sees $15.7K in 24h, 55% of all-time, notable given the near-certain price."
  - "Volume at 99% suggests participants are still opening positions despite near-zero edge, possibly hedging portfolio inflation exposure."
  - "Resolves upon BLS release of CPI data for the year ending November 2026."
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
      kalshi_vol_24h_usd: 15672.69
sources:
  - label: "ClearMarket market record: Will core inflation in November 2026 be measured by Cor"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26nov"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read residual volume at 99% as hedging activity rather than price discovery, someone is still willing to pay up for the inflation confirmation leg as an offsetting position.
