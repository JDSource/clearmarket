---
signal_id: "CMSIG20261007VS04"
signal_slug: "will-the-democratic-party-win-the-wi-05-vol-16246"
headline: "WI-05 Dem House: 1% on $16K volume"
semantic_title: "Democrats face steep odds holding WI-05 House seat"
telemetry: "1% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T07:48:37+00:00"
event_id: "CM-EVT-7FT1CNWRP8"
event_slug: "wi-05-house-election-winner"
event_question: "Will the WI-05 House election winner be decided by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x44cd40c8dba4fefaa8f689b35107712657cdbca8824868db5acd761531679604"
  question_raw: "Will the Democratic Party win the WI-05 House seat?"
  current_price: 0.013
  volume_24h_usd: 16246.387055
  volume_cumulative_usd: 42981.37042200001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in Wisconsin's 5th district at 1%, effectively ruled out."
  - "24h volume of $16K is 38% of all-time, a meaningful single-session share in a House district race."
  - "WI-05 is a historically safe Republican seat; fresh volume likely reflects late hedging or arbitrage closure."
  - "Resolves on WI-05 House race certified result."
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
      poly_vol_24h_usd: 16246.387055
sources:
  - label: "ClearMarket market record: Will the WI-05 House election winner be decided by Nove"
    url: "https://clearmarket.fyi/events/wi-05-house-election-winner"
    retrieved_at: "2026-10-07T07:48:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 1% price with a sizable volume flush tells a desk this contract is being cleaned up rather than contested, residual liquidity is being absorbed as the race approaches resolution.
