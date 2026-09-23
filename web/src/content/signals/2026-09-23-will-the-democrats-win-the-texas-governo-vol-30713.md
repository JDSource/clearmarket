---
signal_id: "CMSIG20260923VS03"
signal_slug: "will-the-democrats-win-the-texas-governo-vol-30713"
headline: "TX governor Dem win: 28% on $31K surge"
semantic_title: "Texas governor odds hold under 30% through surge"
telemetry: "28% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-HCY4NZ1SN4"
event_slug: "texas-governor-winner-2026"
event_question: "Will the Texas Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12b727031b38130d945b3e164386874360d9a32fdd7e3d00ed2adb13857e089b"
  question_raw: "Will the Democrats win the Texas governor race in 2026?"
  current_price: 0.28
  volume_24h_usd: 30713.013463999996
  volume_cumulative_usd: 101568.23413800001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 28% in the Texas governor race, below 1-in-4 territory, reflecting deep structural disadvantage."
  - "24h volume of $31K is 30% of all-time, suggesting a notable burst of attention on a long-shot contract."
  - "Fresh volume near 28% could reflect a speculative bet on candidate news, a GOP stumble, or simply odds-chasing."
  - "Resolves on the November 2026 Texas gubernatorial election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 30713.013463999996
sources:
  - label: "ClearMarket market record: Will the Texas Governor election be won by the Republic"
    url: "https://clearmarket.fyi/events/texas-governor-winner-2026"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained volume on a sub-30% long-shot in a reliably red state warrants monitoring, either a credible catalyst is circulating or speculative flow is testing a floor, both of which matter for correlated state-level contracts.
