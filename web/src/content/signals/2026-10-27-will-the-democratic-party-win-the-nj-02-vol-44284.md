---
signal_id: "CMSIG20261027VS06"
signal_slug: "will-the-democratic-party-win-the-nj-02-vol-44284"
headline: "Dem NJ-02 House seat: 30% on $44K surge"
semantic_title: "Democrats trail in NJ-02 with odds at 30%"
telemetry: "30% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-T2ZK5ZDTH1"
event_slug: "nj-02-house-election-winner"
event_question: "Will the New Jersey 2nd Congressional District House election winner be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xda6443c47be5c76cfe19a36b6de027558fbf669c825b7aa20c0642b753127b58"
  question_raw: "Will the Democratic Party win the NJ-02 House seat?"
  current_price: 0.3
  volume_24h_usd: 44284.950104
  volume_cumulative_usd: 109655.156213
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "30% price marks Democrats as underdogs in New Jersey's 2nd congressional district heading into the 2026 midterm."
  - "$44K in 24h is 40% of all-time Polymarket volume on this seat, outsized daily activity for a single House race."
  - "Fresh money into a competitive House district at this odds level points to new polling or candidate news driving reassessment."
  - "Resolves on the certified winner of the NJ-02 general election."
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
      poly_vol_24h_usd: 44284.950104
sources:
  - label: "ClearMarket market record: Will the New Jersey 2nd Congressional District House el"
    url: "https://clearmarket.fyi/events/nj-02-house-election-winner"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of all-time volume in one day on a House seat priced at 30% is worth flagging, desks tracking midterm seat-count models should update NJ-02 assumptions on incoming district-level data.
