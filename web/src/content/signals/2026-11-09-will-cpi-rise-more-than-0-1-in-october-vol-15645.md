---
signal_id: "CMSIG20261109VS02"
signal_slug: "will-cpi-rise-more-than-0-1-in-october-vol-15645"
headline: "CPI Oct >-0.1%: 99% on $15K Kalshi volume burst"
semantic_title: "October CPI above -0.1% stays a near-certain call on Kalshi"
telemetry: "99% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-09T07:48:23+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in October 2026?"
  current_price: 0.99
  volume_24h_usd: 15645.85
  volume_cumulative_usd: 51696.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "99% leaves almost no probability that October CPI prints at -0.1% or lower, deflation is essentially ruled out."
  - "Kalshi recorded $15.6K in 24h, 30% of all-time volume, concentrated ahead of the imminent data release."
  - "Pre-release positioning typical: traders closing or initiating last-minute size on a contract with clear, imminent resolution."
  - "Contract resolves YES if the October 2026 CPI monthly change exceeds -0.1%; data release is the hard catalyst."
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
      kalshi_vol_24h_usd: 15645.85
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-11-09T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a clean pre-data flush, the market is not debating the direction, only mopping up residual short positions before the print, and the 30% all-time share in one session confirms deadline-driven rather than informational flow.
