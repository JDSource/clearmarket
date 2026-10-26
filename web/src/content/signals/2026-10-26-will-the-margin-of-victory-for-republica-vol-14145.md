---
signal_id: "CMSIG20261026VS07"
signal_slug: "will-the-margin-of-victory-for-republica-vol-14145"
headline: "GOP SD Senate margin: 52% on $14K Kalshi surge"
semantic_title: "South Dakota Senate GOP margin sits at 50-50 on fresh Kalshi flow"
telemetry: "52% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-20CYP3Z7L1"
event_slug: "kxmidtermmov-scsenr"
event_question: "Will the margin of victory for Republicans in the U.S. Senate election in South Carolina be at least 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-SCSENR-P5"
  question_raw: "Will the margin of victory for Republicans in the U.S. Senate election in South Carolina be at least 5 percentage points?"
  current_price: 0.52
  volume_24h_usd: 14145.72
  volume_cumulative_usd: 46403.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "At 52%, traders see the Republican margin question in South Dakota as a near coin-flip."
  - "30% of all-time volume arrived in 24 hours, lifting activity on a previously thin contract."
  - "South Dakota is safely Republican but margin-of-victory contracts hinge on turnout specifics."
  - "Resolves on the certified margin from the 2026 South Dakota U.S. Senate election."
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
      kalshi_vol_24h_usd: 14145.72
sources:
  - label: "ClearMarket market record: Will the margin of victory for Republicans in the U.S. "
    url: "https://clearmarket.fyi/events/kxmidtermmov-scsenr"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 52% price on a margin-of-victory contract drawing 30% of lifetime volume in one day suggests a new poll or candidate dynamic is prompting active repositioning on the size of the Republican win.
