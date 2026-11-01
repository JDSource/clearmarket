---
signal_id: "CMSIG20261101VS05"
signal_slug: "will-the-republican-party-win-the-co-05-vol-13887"
headline: "CO-05 GOP win: 58% on $14K surge"
semantic_title: "Traders split near evenly on Republican hold of CO-05"
telemetry: "58% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-FMXJH0P4G0"
event_slug: "co-05-house-election-winner"
event_question: "Will the CO-05 House seat be won by a Republican in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb00b60bd8636a38909fe71a19bf89b67a4352981690264091d2091393b8413df"
  question_raw: "Will the Republican Party win the CO-05 House seat?"
  current_price: 0.58
  volume_24h_usd: 13887.167134
  volume_cumulative_usd: 30921.032309
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 58% on Polymarket, the Republican hold of CO-05 is favored but far from certain, a genuine toss-up zone."
  - "$14K in 24h is 45% of all-time volume, pointing to a sharp uptick in Election Day attention on this race."
  - "CO-05 has trended competitive in a redistricted environment; 58% reflects meaningful Democratic threat."
  - "Resolves on the certified 2026 CO-05 House race result."
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
      poly_vol_24h_usd: 13887.167134
sources:
  - label: "ClearMarket market record: Will the CO-05 House seat be won by a Republican in the"
    url: "https://clearmarket.fyi/events/co-05-house-election-winner"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all lifetime volume hitting on Election Day at near-coin-flip odds marks CO-05 as a live upset watch for any desk tracking House seat count scenarios.
