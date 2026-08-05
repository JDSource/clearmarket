---
signal_id: "CMSIG20260805VS01"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-1143669"
headline: "McKinney MI-13 nominee: 95% on $1.1M volume spike"
semantic_title: "Heavy trading backs McKinney as MI-13 Dem nominee"
telemetry: "95% · $1.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-CYX84N0L20"
event_slug: "kxmi13d-26"
event_question: "Will the Democratic nominee for Michigan's 13th congressional district be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMI13D-26-DMCK"
  question_raw: "Will Donavan McKinney be the Democratic nominee for MI-13?"
  current_price: 0.946
  volume_24h_usd: 1143669.66
  volume_cumulative_usd: 1506626.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices McKinney at 95%, strong but not yet fully collapsed to certainty."
  - "76% of all-time volume arrived in 24h, signaling a decisive informational event."
  - "Surge likely tied to same Michigan primary cycle driving the El-Sayed contract."
  - "Resolves on certification of MI-13 Democratic primary winner."
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
      kalshi_vol_24h_usd: 1143669.66
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Michigan's 13th congres"
    url: "https://clearmarket.fyi/events/kxmi13d-26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 95% price with three-quarters of all-time volume in one day points to a near-called primary, desks should treat this as a closing settlement trade, not a directional bet.
