---
signal_id: "CMSIG20261029VS04"
signal_slug: "will-the-republican-party-win-the-nc-09-vol-44998"
headline: "GOP NC-09 House seat: 69% on $45K inflow"
semantic_title: "Republicans favored in NC-09 with buyers backing the lead"
telemetry: "69% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x31727e0e298757e552661f62733cc401c6066b80a7d2607d2ac56b729eb15a00"
  question_raw: "Will the Republican Party win the NC-09 House seat?"
  current_price: 0.69
  volume_24h_usd: 44998.368243
  volume_cumulative_usd: 108686.684788
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans winning NC-09 at 69%, the mirror of the Democratic contract, confirming GOP lean."
  - "$45K in 24h volume is 41% of all-time, a concentrated single-session bet relative to lifetime turnover."
  - "Paired volume across both NC-09 contracts today suggests active two-sided positioning on this specific race."
  - "Resolves on 2026 midterm election night for NC-09."
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
      poly_vol_24h_usd: 44998.368243
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes in both the Democratic and Republican NC-09 contracts signal the desk that this race is being actively repriced, likely triggered by new polling or a campaign development worth tracking.
