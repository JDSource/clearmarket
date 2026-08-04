---
signal_id: "CMSIG20260804VS00"
signal_slug: "will-shri-thanedar-be-the-democratic-nom-vol-117036"
headline: "Thanedar MI-13 nominee: 13% on $117K surge"
semantic_title: "Thanedar MI-13 nomination bid trades as a long shot"
telemetry: "13% · $117K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x399b69600812f9997ee0dcac06c74c9351f230baa53765eacbc443a77bc520b9"
  question_raw: "Will Shri Thanedar be the Democratic Nominee for MI-13?"
  current_price: 0.13
  volume_24h_usd: 117036.33418799998
  volume_cumulative_usd: 294136.212798
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "At 13%, Polymarket sees Thanedar as a heavy underdog in the MI-13 Democratic primary."
  - "24h volume of $117K equals 40% of all-time handle, a decisive single-session repositioning."
  - "Capital flooding in alongside the McKinney contract (87%) signals the field is near-settled against Thanedar."
  - "Resolves on the MI-13 Democratic primary result."
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
      poly_vol_24h_usd: 117036.33418799998
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The paired volume on Thanedar and McKinney contracts suggests the market is actively closing out residual Thanedar probability, a desk should treat this as a near-lock on McKinney.
