---
signal_id: "CMSIG20261008VS02"
signal_slug: "will-cpi-rise-more-than-0-5-in-septembe-vol-52184"
headline: "CPI +0.5% Sept: 48% as volume hits 25% ATH"
semantic_title: "September CPI above 0.5% stays a coin-flip bet"
telemetry: "48% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T07:49:04+00:00"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "Will CPI in September be above expectations?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.5"
  question_raw: "Will CPI rise more than 0.5% in September 2026?"
  current_price: 0.48
  volume_24h_usd: 52184.15
  volume_cumulative_usd: 205250.26
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi prices a September CPI print above 0.5% month-on-month at 48%, effectively a coin-flip on hot inflation."
  - "24h volume of $52.2K represents 25% of all-time, a clean landmark share arriving as the release window nears."
  - "Attention at near-50% odds signals genuine two-sided uncertainty: no consensus on whether energy or shelter drives a big print."
  - "Resolves on September 2026 BLS CPI release; 48% implies the market sees the 0.5% threshold as a live risk."
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
      kalshi_vol_24h_usd: 52184.15
sources:
  - label: "ClearMarket market record: Will CPI in September be above expectations?"
    url: "https://clearmarket.fyi/events/kxcpi-26sep"
    retrieved_at: "2026-10-08T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The coin-flip pricing and fresh 25% all-time volume share signal that rates desks are actively hedging September CPI tail risk ahead of the print, with no clear directional lean established.
