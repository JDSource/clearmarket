---
signal_id: "CMSIG20260801VS07"
signal_slug: "will-shri-thanedar-be-the-democratic-nom-vol-35374"
headline: "Thanedar MI-13 Dem nominee: 15% on $35K Polymarket"
semantic_title: "Thanedar MI-13 nomination bid trades at 15% under fresh selling pressure"
telemetry: "15% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x399b69600812f9997ee0dcac06c74c9351f230baa53765eacbc443a77bc520b9"
  question_raw: "Will Shri Thanedar be the Democratic Nominee for MI-13?"
  current_price: 0.15
  volume_24h_usd: 35374.93054600001
  volume_cumulative_usd: 101317.05585799998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "Polymarket prices Thanedar at 15% to win the MI-13 Democratic nomination, clear underdog read."
  - "24h volume of $35K is 35% of all-time flow, active but below the McKinney contract's intensity."
  - "The inverse of McKinney's 85% leaves no probability gap, market treats this as a two-horse race."
  - "Resolves on primary; Thanedar held MI-13 previously, giving the contract residual attention."
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
      poly_vol_24h_usd: 35374.93054600001
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume on both the McKinney and Thanedar Polymarket contracts confirms traders are actively taking sides in the MI-13 primary, not just buying the favorite, a desk should monitor for any endorsement or news that could compress the 70-point gap.
