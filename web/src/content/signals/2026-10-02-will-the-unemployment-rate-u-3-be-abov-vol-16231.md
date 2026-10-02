---
signal_id: "CMSIG20261002VS07"
signal_slug: "will-the-unemployment-rate-u-3-be-abov-vol-16231"
headline: "U-3 above 4.0% in Sept: 71% on $16K surge"
semantic_title: "Heavy trading tests U-3 clearing 4.0% in September at 71%"
telemetry: "71% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Will the unemployment rate (U-3) be above 4.0% in September?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.0"
  question_raw: "Will the unemployment rate (U-3) be above 4.0% in September?"
  current_price: 0.71
  volume_24h_usd: 16231.54
  volume_cumulative_usd: 52602.55
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "71% price implies the market sees a better-than-even chance September unemployment breaches the 4.0% threshold."
  - "31% of all-time volume arrived today, notable given the contract has a larger all-time base than the 3.8% tier."
  - "Paired with the 3.9% contract at 92%, the market's implied probability mass sits between 3.9% and 4.0%, with a meaningful left tail above 4.0%."
  - "Resolves on the BLS official September 2026 U-3 release."
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
      kalshi_vol_24h_usd: 16231.54
sources:
  - label: "ClearMarket market record: Will the unemployment rate (U-3) be above 4.0% in Septe"
    url: "https://clearmarket.fyi/events/kxu3-26sep"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 71% market on U-3 above 4.0% is the most rate-sensitive signal in this batch, a desk pricing Fed easing expectations should treat this as the market leaning toward a September print that keeps a November cut firmly in play.
