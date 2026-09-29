---
signal_id: "CMSIG20260929VS01"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-39138"
headline: "U-3 Sept above 3.9%: 94% on $39K one-day surge"
semantic_title: "U-3 above 3.9% in September holds near-certain odds"
telemetry: "94% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-29T07:47:54+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T3.9"
  question_raw: "Will the unemployment rate (U-3) be above 3.9% in September?"
  current_price: 0.94
  volume_24h_usd: 39138.37
  volume_cumulative_usd: 102403.11
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi prices a 94% probability that September U-3 unemployment prints above 3.9%, reflecting near-consensus conviction."
  - "38% of all-time volume, $39.1K, traded in 24 hours, a notable single-session concentration ahead of imminent resolution."
  - "Contract resolves on the September BLS jobs report, likely due within days given today is September 29."
  - "High price plus rising volume suggests traders are locking in near-certain payouts, not debating the outcome."
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
      kalshi_vol_24h_usd: 39138.37
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-09-29T07:47:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-full consensus pricing with a fresh volume spike this close to the report date signals the desk should treat above-3.9% U-3 as the base case for September macro models.
