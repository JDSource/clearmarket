---
signal_id: "CMSIG20261030VS05"
signal_slug: "will-the-margin-of-victory-for-democrats-vol-30682"
headline: "NC Senate Dem margin: 98% on $31K Kalshi"
semantic_title: "NC Senate Democratic margin locks in at 98%"
telemetry: "98% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-22Y3TGXT19"
event_slug: "kxmidtermmov-ncsend"
event_question: "Will the North Carolina Senate margin of victory be less than 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-NCSEND-P1"
  question_raw: "Will the margin of victory for Democrats in the U.S. Senate election in North Carolina be at least 1 percentage points?"
  current_price: 0.98
  volume_24h_usd: 30682.65
  volume_cumulative_usd: 41530.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "98% prices it as near-certain Democrats win the North Carolina Senate race by their targeted margin."
  - "$31K in 24h covers 74% of all-time volume, nearly the full contract lifecycle compressed into one session."
  - "A margin-of-victory contract at 98% with this volume share suggests final settlement buying."
  - "Resolves on certified North Carolina Senate vote margin."
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
      kalshi_vol_24h_usd: 30682.65
sources:
  - label: "ClearMarket market record: Will the North Carolina Senate margin of victory be les"
    url: "https://clearmarket.fyi/events/kxmidtermmov-ncsend"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

74% of lifetime volume on a 98% contract in a single session indicates this is a closing print, desks are settling margin positions rather than opening new directional risk.
