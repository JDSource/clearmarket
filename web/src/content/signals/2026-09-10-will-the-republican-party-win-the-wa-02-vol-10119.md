---
signal_id: "CMSIG20260910VS06"
signal_slug: "will-the-republican-party-win-the-wa-02-vol-10119"
headline: "WA-02 GOP seat: 1% on $10K surge"
semantic_title: "Traders back the Democrat in WA-02 at 99% through volume spike"
telemetry: "1% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-0243WFQBC2"
event_slug: "wa-02-house-election-winner"
event_question: "WA-02 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x90f15a7d54cc507dabd869d0c92b870449703437eac9c7814518c81f46f6ab7a"
  question_raw: "Will the Republican Party win the WA-02 House seat?"
  current_price: 0.01
  volume_24h_usd: 10119.989666
  volume_cumulative_usd: 17544.549666
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win in WA-02 at just 1%, firmly handing the seat to the Democrat."
  - "58% of all-time volume traded in 24 hours, the contract is reaching resolution-level conviction."
  - "WA-02 is a historically blue district; this spike likely reflects late money confirming a lopsided race with no path for the GOP."
  - "Resolves on the 2026 WA-02 House general election."
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
      poly_vol_24h_usd: 10119.989666
sources:
  - label: "ClearMarket market record: WA-02 House Election Winner"
    url: "https://clearmarket.fyi/events/wa-02-house-election-winner"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 58% all-time volume concentration at 1% Republican odds signals this seat is locked for Democrats, relevant as a firm non-competitive marker in any 2026 House majority model.
