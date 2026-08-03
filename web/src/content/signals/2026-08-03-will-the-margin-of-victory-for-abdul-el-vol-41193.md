---
signal_id: "CMSIG20260803VS00"
signal_slug: "will-the-margin-of-victory-for-abdul-el-vol-41193"
headline: "El-Sayed MI Senate margin: 45% on $41K surge"
semantic_title: "Heavy trading tests El-Sayed MI Senate margin odds"
telemetry: "45% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-03T11:19:10+00:00"
event_id: "CM-EVT-GCZLRSF2K2"
event_slug: "kxprimarymov-kxsenatemid26"
event_question: "What will be the margin of victory in the Michigan Democratic Senate primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYMOV-KXSENATEMID26-AELS-P57"
  question_raw: "Will the margin of victory for Abdul El-Sayed in the 2026 Michigan Democratic Senate primary be above 15%?"
  current_price: 0.45
  volume_24h_usd: 41193.48
  volume_cumulative_usd: 156591.22
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Market prices a 45% chance El-Sayed wins by the specified margin, a near-toss-up on the spread."
  - "$41K traded in 24h equals 26% of all-time volume, signaling a sharp burst of fresh attention."
  - "Michigan's Democratic primary is a closely watched bellwether; margin bets attract late-deciding capital as results near."
  - "Resolves on certified margin data from the Michigan primary."
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
      kalshi_vol_24h_usd: 41193.48
sources:
  - label: "ClearMarket market record: What will be the margin of victory in the Michigan Demo"
    url: "https://clearmarket.fyi/events/kxprimarymov-kxsenatemid26"
    retrieved_at: "2026-08-03T11:19:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A sudden concentration of volume at near-even odds on the margin contract suggests desks are actively pricing a contested primary outcome rather than a runaway win for El-Sayed.
