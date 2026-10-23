---
signal_id: "CMSIG20261023VS02"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-33922"
headline: "Core CPI >2.2% Nov yr-end: 99% on $34K, 76% all-time"
semantic_title: "Core CPI above 2.2% for November year, near certainty holds"
telemetry: "99% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
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
  - "Kalshi prices core CPI above 2.2% for the November year-end period at 99%, effectively a market consensus call."
  - "24h volume is 76% of all-time total, the dominant share of all trading happened in a single day, signaling urgency."
  - "Surge likely follows fresh inflation data or Fed communications reinforcing above-target core readings."
  - "Resolves on BLS core CPI print for the 12 months ending November 2026."
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
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Three-quarters of all-time volume in one day on a 99% contract tells desks the inflation-above-threshold scenario is being treated as a near-done fact, likely used to anchor rate-path hedges.
