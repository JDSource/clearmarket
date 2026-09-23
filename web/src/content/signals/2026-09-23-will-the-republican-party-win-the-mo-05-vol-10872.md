---
signal_id: "CMSIG20260923VS07"
signal_slug: "will-the-republican-party-win-the-mo-05-vol-10872"
headline: "MO-05 GOP seat: 13% on $11K inflow"
semantic_title: "MO-05 Republican seat trades at 13% despite volume push"
telemetry: "13% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-0TPY2JS6W0"
event_slug: "mo-05-house-election-winner"
event_question: "MO-05 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb54ccf642fdfab45637e1f093509e5ee69fcb1ff25979c11cf04650f18c3f97e"
  question_raw: "Will the Republican Party win the MO-05 House seat?"
  current_price: 0.131
  volume_24h_usd: 10872.160469999997
  volume_cumulative_usd: 38450.16713100001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 13% in MO-05, a heavy underdog read in what appears to be a Democratically favored district."
  - "24h volume of $11K equals 28% of all-time, marking a meaningful uptick in a previously light contract."
  - "GOP at 13% with fresh buying suggests either speculative long-shot positioning or new information narrowing the gap slightly."
  - "Resolves on the November 2026 MO-05 House general election result."
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
      poly_vol_24h_usd: 10872.160469999997
sources:
  - label: "ClearMarket market record: MO-05 House Election Winner"
    url: "https://clearmarket.fyi/events/mo-05-house-election-winner"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume arriving on a 13% Republican contract in MO-05 warrants a check on whether district demographics or candidate developments have shifted, at 13%, even modest new information could move the price materially.
