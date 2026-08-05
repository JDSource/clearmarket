---
signal_id: "CMSIG20260805VS07"
signal_slug: "will-todd-blanche-leaves-deputy-attorney-vol-62382"
headline: "Blanche exits DAG before 2027: 92% on $62K"
semantic_title: "Fresh volume backs Blanche leaving DAG role before 2027"
telemetry: "92% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-TBLA"
  question_raw: "Will Todd Blanche leaves Deputy Attorney General in before 2027?"
  current_price: 0.921
  volume_24h_usd: 62382.9
  volume_cumulative_usd: 226450.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "Kalshi prices a Blanche departure before 2027 at 92%, market leans heavily toward an exit."
  - "28% of all-time volume in 24h; this contract has a longer history, making today's spike notable."
  - "Renewed activity may reflect reporting on DOJ staffing, Senate confirmation of a successor, or direct news."
  - "Resolves if Blanche vacates the Deputy Attorney General role before January 1, 2027."
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
      kalshi_vol_24h_usd: 62382.9
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

92% pricing on a senior DOJ departure with a fresh volume spike is a signal worth flagging for desks tracking rule-of-law and DOJ operational-continuity risk heading into 2027.
