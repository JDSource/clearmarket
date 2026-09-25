---
signal_id: "CMSIG20260925VS04"
signal_slug: "will-the-republican-party-win-the-ca-20-vol-15261"
headline: "CA-20 GOP House: 96% on $15K Polymarket surge"
semantic_title: "CA-20 Republican seat all but locked in at 96%"
telemetry: "96% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-9KGFX70F78"
event_slug: "ca-20-house-election-winner"
event_question: "Will the CA-20 House seat be won in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc4ceb029b48b2d326a968cc417aef28462cf4b8a3c0b61ff7ca76271e0f693e1"
  question_raw: "Will the Republican Party win the CA-20 House seat?"
  current_price: 0.965
  volume_24h_usd: 15261.156166
  volume_cumulative_usd: 28151.840066000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican win at 96%, reflecting a near-certain outcome in a heavily red California district."
  - "24h volume is 54% of all-time handle, an unusually large single-session share for a contract already at near-resolution pricing."
  - "Volume at ceiling prices typically signals late confirmation activity, traders closing out or adding to near-certain positions before resolution."
  - "Resolves on the 2026 CA-20 general election result."
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
      poly_vol_24h_usd: 15261.156166
sources:
  - label: "ClearMarket market record: Will the CA-20 House seat be won in the 2026 election?"
    url: "https://clearmarket.fyi/events/ca-20-house-election-winner"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-confidence, high-volume activity at 96% likely reflects late-stage position squaring rather than new information, but any deviation from that price would be immediately significant.
