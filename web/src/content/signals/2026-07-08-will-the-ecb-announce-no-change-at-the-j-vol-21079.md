---
signal_id: "CMSIG20260708VS07"
signal_slug: "will-the-ecb-announce-no-change-at-the-j-vol-21079"
headline: "ECB July no change: 98% on $21K Polymarket flow"
semantic_title: "ECB July hold priced near certainty at 98%"
telemetry: "98% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-RPR6R3R686"
event_slug: "ecb-interest-rates-july-2026"
event_question: "Will the ECB interest rates change by July 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x13ca23189a09423b464147d3fa35bc210f6bd589ee115d947676784ec2418e71"
  question_raw: "Will the ECB announce no change at the July 2026 meeting?"
  current_price: 0.978
  volume_24h_usd: 21079.131773000005
  volume_cumulative_usd: 76150.64127799998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-23T00:00:00Z"
bullets:
  - "98% price signals near-unanimous market expectation of an ECB hold at the July 2026 meeting."
  - "24h volume $21K is 28% of all-time, suggesting late-stage positioning as the meeting approaches."
  - "Volume at 98% likely reflects arbitrage close-out or confirmation-seeking after ECB communication."
  - "Resolves at the ECB July 2026 policy announcement."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 21079.131773000005
sources:
  - label: "ClearMarket market record: Will the ECB interest rates change by July 2026?"
    url: "https://clearmarket.fyi/events/ecb-interest-rates-july-2026"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A European rates desk can treat the 98% price as a near-resolved contract, the volume surge is consistent with final arbitrage compression ahead of the meeting, not a genuine uncertainty repricing.
