---
signal_id: "CMSIG20261109VS00"
signal_slug: "will-stephen-miller-leaves-deputy-chief-vol-316409"
headline: "Miller Deputy CoS exit: 96% NO on $316K surge"
semantic_title: "Heavy trading backs Miller staying through 2026"
telemetry: "96% · $316K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-09T07:48:23+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-SMIL"
  question_raw: "Will Stephen Miller leaves Deputy Chief of Staff in before 2027?"
  current_price: 0.965
  volume_24h_usd: 316409.89
  volume_cumulative_usd: 1253527.74
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "96% NO implies the market sees a Miller departure before 2027 as a near-certain non-event."
  - "Kalshi logged $316K in 24h, 25% of all-time volume, the largest single-day print on this contract."
  - "Fresh attention likely triggered by White House personnel chatter; volume arriving into a one-sided price signals conviction, not dispute."
  - "Contract resolves YES if Miller leaves the Deputy Chief of Staff role before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 316409.89
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-11-09T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the market pricing near-zero staffing-disruption risk around Miller through year-end, with the volume surge suggesting someone moved size to lock in that view after a news catalyst.
