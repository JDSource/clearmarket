---
signal_id: "CMSIG20260930VS07"
signal_slug: "will-the-democratic-party-win-the-nc-02-vol-11295"
headline: "Dems NC-02: 98% on $11K, 64% all-time share"
semantic_title: "NC-02 Democratic win draws bulk of all-time volume today"
telemetry: "98% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-5J1SZPC334"
event_slug: "nc-02-house-election-winner"
event_question: "Will the winner of the NC-02 House election be determined by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x32014816dbc86acb28695b8eb4e1fda3f4bfefad68bbeb79479fb2080c0c9791"
  question_raw: "Will the Democratic Party win the NC-02 House seat?"
  current_price: 0.982
  volume_24h_usd: 11295.650694000002
  volume_cumulative_usd: 17561.788142999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic NC-02 House win at 98%, the seat is treated as a done deal."
  - "64% of all-time volume on this contract traded in the past 24 hours, an extreme concentration event."
  - "Thin overall liquidity amplifies the all-time share; still, the sudden interest warrants a check for redistricting or candidate news."
  - "Resolves on the 2026 NC-02 House general election result."
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
      poly_vol_24h_usd: 11295.650694000002
sources:
  - label: "ClearMarket market record: Will the winner of the NC-02 House election be determin"
    url: "https://clearmarket.fyi/events/nc-02-house-election-winner"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 64% all-time volume share in one session on a 98% contract is an anomaly desks should note, in low-liquidity markets even small flows can signal that someone has received material information about the race.
