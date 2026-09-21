---
signal_id: "CMSIG20260921VS04"
signal_slug: "will-the-republicans-win-the-ohio-senate-vol-63116"
headline: "GOP Ohio Senate: 43% on $63K volume surge"
semantic_title: "Republicans slip below 50% in the Ohio Senate race"
telemetry: "43% · $63K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-53NPW6YWF1"
event_slug: "ohio-senate-election-winner"
event_question: "Will the winner of the Ohio Senate election be decided by DATE?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x771873c365f87bffd990644e4b688aebc1be7f18396d2eab64b996ff66e88669"
  question_raw: "Will the Republicans win the Ohio Senate race in 2026?"
  current_price: 0.43
  volume_24h_usd: 63116.788283999995
  volume_cumulative_usd: 239906.71761
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 43% in Ohio, below 50%, making this a market-implied toss-up leaning Democratic."
  - "26% of all-time volume traded in 24h, consistent with the broad Senate-cycle volume event today."
  - "Ohio at 43% Republican is a notable read given the state's recent rightward drift; fresh volume endorses the competitive framing."
  - "Resolves on 2026 Ohio Senate general election outcome."
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
      poly_vol_24h_usd: 63116.788283999995
sources:
  - label: "ClearMarket market record: Will the winner of the Ohio Senate election be decided "
    url: "https://clearmarket.fyi/events/ohio-senate-election-winner"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Republicans priced below 50% in Ohio with a volume surge is the highest-signal item in this Senate batch, desks should flag this as a potentially tradeable competitive-seat call worth cross-referencing with live polling.
