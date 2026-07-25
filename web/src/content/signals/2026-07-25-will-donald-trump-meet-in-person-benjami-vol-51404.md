---
signal_id: "CMSIG20260725VS03"
signal_slug: "will-donald-trump-meet-in-person-benjami-vol-51404"
headline: "Trump, Netanyahu meeting by Aug 1: 97% on $51K"
semantic_title: "Trump, Netanyahu in-person meeting before Aug 1 stays at 97%"
telemetry: "97% · $51K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-DFKW6SYBM7"
event_slug: "kxtrumpbibimeet-26aug01"
event_question: "Will Trump and Netanyahu meet?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPBIBIMEET-26AUG01-AUG01"
  question_raw: "Will Donald Trump meet in person Benjamin Netanyahu before Aug 1, 2026?"
  current_price: 0.97
  volume_24h_usd: 51404.11
  volume_cumulative_usd: 105944.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-08T14:00:00Z"
bullets:
  - "Kalshi prices the meeting at 97%, traders treat this as a near-certainty with one week remaining."
  - "$51K in 24h covers 49% of all-time volume, suggesting the market is actively closing out the residual 3% doubt."
  - "Volume this close to resolution and this close to 100% typically reflects final position squaring ahead of the Aug 1 deadline."
  - "Contract resolves if an in-person meeting between Trump and Netanyahu occurs before August 1, 2026."
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
      kalshi_vol_24h_usd: 51404.11
sources:
  - label: "ClearMarket market record: Will Trump and Netanyahu meet?"
    url: "https://clearmarket.fyi/events/kxtrumpbibimeet-26aug01"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% contract drawing half its lifetime volume days before expiry is a liquidation signal, not a new directional bet, desks should note the meeting is operationally expected by the market.
