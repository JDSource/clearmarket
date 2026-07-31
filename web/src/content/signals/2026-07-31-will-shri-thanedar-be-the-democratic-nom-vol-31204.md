---
signal_id: "CMSIG20260731VS06"
signal_slug: "will-shri-thanedar-be-the-democratic-nom-vol-31204"
headline: "Thanedar MI-13 Dem nominee: 18% on $31K"
semantic_title: "A Thanedar MI-13 Democratic nomination stays a long shot at 18%"
telemetry: "18% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-31T10:35:22+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x399b69600812f9997ee0dcac06c74c9351f230baa53765eacbc443a77bc520b9"
  question_raw: "Will Shri Thanedar be the Democratic Nominee for MI-13?"
  current_price: 0.18
  volume_24h_usd: 31204.112808
  volume_cumulative_usd: 65942.12531200003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "At 18%, Polymarket traders price Thanedar as a clear underdog for the MI-13 Democratic nomination."
  - "$31K in 24h is 47% of all-time volume, nearly half the contract's lifetime in one session."
  - "Volume surge mirrors Kalshi's McKinney spike; the two contracts are effectively paired."
  - "Resolves on official MI-13 Democratic nominee certification."
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
      poly_vol_24h_usd: 31204.112808
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-07-31T10:35:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The coordinated volume across both MI-13 nominee markets on the same day points to a definitive catalyst, a desk covering House races should check for a primary vote, court ruling, or candidate withdrawal.
