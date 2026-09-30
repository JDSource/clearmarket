---
signal_id: "CMSIG20260930VS07"
signal_slug: "will-the-democratic-party-win-the-nc-02-vol-10918"
headline: "NC-02 Dem House: 98% on $11K, 64% of all-time"
semantic_title: "NC-02 Democrats hold at 98% as volume surges on a safe seat"
telemetry: "98% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-5J1SZPC334"
event_slug: "nc-02-house-election-winner"
event_question: "Will the winner of the NC-02 House election be determined by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x32014816dbc86acb28695b8eb4e1fda3f4bfefad68bbeb79479fb2080c0c9791"
  question_raw: "Will the Democratic Party win the NC-02 House seat?"
  current_price: 0.98
  volume_24h_usd: 10918.12015
  volume_cumulative_usd: 17184.257598999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at 98% to win North Carolina's 2nd House seat, the market treats this as effectively settled."
  - "$11K in 24h equals 64% of all-time contract volume, the single dominant session in the contract's history."
  - "NC-02 is a Democratic-leaning district; concentrated late volume at 98% likely reflects settlement arbitrage or cleanup flow."
  - "Contract resolves on the November 2026 NC-02 House general election."
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
      poly_vol_24h_usd: 10918.12015
sources:
  - label: "ClearMarket market record: Will the winner of the NC-02 House election be determin"
    url: "https://clearmarket.fyi/events/nc-02-house-election-winner"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Like KY-05, a near-certain contract absorbing the majority of its lifetime volume in one day points to mechanical end-of-cycle positioning rather than new information, flag for settlement desk, not fundamental research.
