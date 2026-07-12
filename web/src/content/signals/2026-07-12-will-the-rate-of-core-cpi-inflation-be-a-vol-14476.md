---
signal_id: "CMSIG20260712VS06"
signal_slug: "will-the-rate-of-core-cpi-inflation-be-a-vol-14476"
headline: "Core CPI above 2.6% June year-end: 99% on $14K"
semantic_title: "Core CPI above 2.6% for June year, near-certain settlement"
telemetry: "99% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-12T09:48:30+00:00"
event_id: "CM-EVT-B5KCGZG8C0"
event_slug: "kxcpicoreyoy-26jun"
event_question: "Will the core Consumer Price Index year-over-year change in June 2026 be below 3%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26JUN-T2.6"
  question_raw: "Will the rate of core CPI inflation be above 2.6% for the year ending in June 2026?"
  current_price: 0.99
  volume_24h_usd: 14476.2
  volume_cumulative_usd: 44001.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-21T14:00:00Z"
bullets:
  - "Kalshi prices core CPI above 2.6% for the year ending June 2026 at 99%, effectively a settlement trade."
  - "$14K in 24h is 33% of a $44K all-time pool, consistent with arbitrage-driven late-stage compression."
  - "June CPI print is imminent or already released, triggering resolution-window position cleanup."
  - "At 99%, any remaining 1% discount represents friction cost, not genuine inflation uncertainty."
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
      kalshi_vol_24h_usd: 14476.2
sources:
  - label: "ClearMarket market record: Will the core Consumer Price Index year-over-year chang"
    url: "https://clearmarket.fyi/events/kxcpicoreyoy-26jun"
    retrieved_at: "2026-07-12T09:48:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with a third of all-time volume in one session signals rates desks are closing out the contract mechanically ahead of confirmed CPI resolution.
