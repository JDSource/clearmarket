---
signal_id: "CMSIG20260805VS02"
signal_slug: "will-the-margin-of-victory-for-abdul-el-vol-441696"
headline: "El-Sayed margin contract: 99% on $442K in 24h"
semantic_title: "Odds hold high on a wide El-Sayed primary margin"
telemetry: "99% · $442K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-GCZLRSF2K2"
event_slug: "kxprimarymov-kxsenatemid26"
event_question: "What will be the margin of victory in the Michigan Democratic Senate primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYMOV-KXSENATEMID26-AELS-P1"
  question_raw: "Will the margin of victory for Abdul El-Sayed in the 2026 Michigan Democratic Senate primary be between 0% and 3%?"
  current_price: 0.99
  volume_24h_usd: 441696.72
  volume_cumulative_usd: 522944.33
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi contract pricing a wide victory margin at 99%, blowout outcome near-certain per market."
  - "84% of all-time volume hit in 24h; contract is essentially fully discovered."
  - "Complements the nominee contract, traders are pricing both the win and the size of it."
  - "Resolves once official Michigan primary canvass reports the margin."
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
      kalshi_vol_24h_usd: 441696.72
sources:
  - label: "ClearMarket market record: What will be the margin of victory in the Michigan Demo"
    url: "https://clearmarket.fyi/events/kxprimarymov-kxsenatemid26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A margin contract at 99% with 84% of its lifetime volume in one session tells a desk the primary result was not just a win but a lopsided one, useful context for downstream general-election positioning.
