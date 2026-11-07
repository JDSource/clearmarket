---
signal_id: "CMSIG20261107VS07"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-15672"
headline: "Core CPI >2.5% thru Nov 2026: 99% on $16K"
semantic_title: "Core CPI above 2.5% through November stays a near-lock"
telemetry: "99% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
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
  - "Kalshi prices core CPI staying above 2.5% for the year ending November 2026 at 99%, market treats it as resolved."
  - "$16K in 24h is 55% of all-time volume, signaling fresh interest in an already-consensus inflation call."
  - "Volume into a 99% contract likely reflects late arbitrage or hedging against portfolio inflation assumptions."
  - "Resolves on the official BLS core CPI figure for November 2026."
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
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a confirmed inflation signal, the market has effectively declared core CPI entrenched above 2.5% through November 2026, relevant for any rates or duration positioning tied to Fed targets.
