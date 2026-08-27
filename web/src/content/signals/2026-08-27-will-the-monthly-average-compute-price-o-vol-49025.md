---
signal_id: "CMSIG20260827VS00"
signal_slug: "will-the-monthly-average-compute-price-o-vol-49025"
headline: "H200 above $2.00: 99% on $49K surge"
semantic_title: "H200 compute above $2.00 in August stays a near-certainty"
telemetry: "99% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-0T7SDX2738"
event_slug: "kxh200ms-26aug"
event_question: "Will the NVIDIA H200 average hourly price in August reach a specified threshold?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXH200MS-26AUG-2.000"
  question_raw: "Will the monthly average compute price of NVIDIA's H200 be above $2.00 in August 2026?"
  current_price: 0.99
  volume_24h_usd: 49025.51
  volume_cumulative_usd: 67723.05
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi prices 99%, market treats the $2.00 floor as effectively resolved."
  - "24h volume of $49K is 72% of all-time, signaling a late-month settlement rush."
  - "August closes in days; traders appear to be locking in final positions before resolution."
  - "Resolves on monthly average H200 compute price for August 2026."
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
      kalshi_vol_24h_usd: 49025.51
sources:
  - label: "ClearMarket market record: Will the NVIDIA H200 average hourly price in August rea"
    url: "https://clearmarket.fyi/events/kxh200ms-26aug"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume spike looks like a settlement-window squeeze, desks closing or hedging positions ahead of imminent August resolution rather than expressing new directional views.
