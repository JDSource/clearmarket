---
signal_id: "CMSIG20260714VS00"
signal_slug: "will-the-rate-of-cpi-inflation-be-above-vol-79972"
headline: "June CPI above 3.6%: 99% on $80K Kalshi surge"
semantic_title: "Traders lock in June CPI breach above 3.6% as near-certainty"
telemetry: "99% · $80K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-14T09:55:02+00:00"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "Will inflation in June 2026 be measured by year-over-year CPI?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.6"
  question_raw: "Will the rate of CPI inflation be above 3.6% for the year ending in June 2026?"
  current_price: 0.99
  volume_24h_usd: 79972.44
  volume_cumulative_usd: 178038.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "99% price leaves virtually no doubt: market reads June CPI print as confirmed above 3.6%."
  - "Kalshi sees $79,972 in 24h, 45% of the contract's entire all-time volume in a single session."
  - "Resolution likely imminent as the BLS June CPI release lands mid-July, driving late positioning."
  - "Contract resolves on official BLS year-over-year figure; near-zero residual uncertainty priced."
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
      kalshi_vol_24h_usd: 79972.44
sources:
  - label: "ClearMarket market record: Will inflation in June 2026 be measured by year-over-ye"
    url: "https://clearmarket.fyi/events/kxcpiyoy-26jun"
    retrieved_at: "2026-07-14T09:55:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The extreme price and volume concentration signal that a desk should treat above-3.6% June CPI as the base case and re-examine any rate-cut positioning premised on softer inflation.
