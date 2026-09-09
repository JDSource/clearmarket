---
signal_id: "CMSIG20260909VS02"
signal_slug: "will-cpi-rise-more-than-0-1-in-august-2-vol-29430"
headline: "Aug CPI >0.1%: 99% on $29K vol spike"
semantic_title: "August CPI above 0.1% priced as near-certain"
telemetry: "99% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-D057W6W251"
event_slug: "kxcpi-26aug"
event_question: "Will the Consumer Price Index increase in August?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26AUG-T0.1"
  question_raw: "Will CPI rise more than 0.1% in August 2026?"
  current_price: 0.99
  volume_24h_usd: 29430.9
  volume_cumulative_usd: 59573.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-11T13:56:00Z"
bullets:
  - "Kalshi prices a greater-than-0.1% August CPI print at 99%, effectively a consensus lock-in."
  - "49% of all-time volume cleared in 24h, coinciding with proximity to the scheduled BLS release."
  - "Near-unanimous pricing leaves almost no tradeable edge; volume likely reflects hedging rather than directional bets."
  - "Resolves on BLS August 2026 CPI release, expected mid-September 2026."
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
      kalshi_vol_24h_usd: 29430.9
sources:
  - label: "ClearMarket market record: Will the Consumer Price Index increase in August?"
    url: "https://clearmarket.fyi/events/kxcpi-26aug"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this spike as a hedging flow around an imminent macro print rather than a directional signal, the 99% price leaves no meaningful tail to trade against.
