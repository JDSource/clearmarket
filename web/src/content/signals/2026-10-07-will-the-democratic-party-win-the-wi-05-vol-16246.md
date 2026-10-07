---
signal_id: "CMSIG20261007VS03"
signal_slug: "will-the-democratic-party-win-the-wi-05-vol-16246"
headline: "Dems WI-05 House seat: 1% on $16K surge"
semantic_title: "Democrats win WI-05 priced out at 1% on fresh volume"
telemetry: "1% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T15:02:49+00:00"
event_id: "CM-EVT-7FT1CNWRP8"
event_slug: "wi-05-house-election-winner"
event_question: "Will the WI-05 House election winner be decided by November 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x44cd40c8dba4fefaa8f689b35107712657cdbca8824868db5acd761531679604"
  question_raw: "Will the Democratic Party win the WI-05 House seat?"
  current_price: 0.013
  volume_24h_usd: 16246.387055
  volume_cumulative_usd: 42981.37042199999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in Wisconsin's 5th congressional district at 1%, the market treats this race as decided."
  - "38% of all-time volume, $16K, traded in 24 hours, indicating renewed attention on a previously quiet contract."
  - "WI-05 is a heavily Republican-leaning district; volume at near-zero odds likely reflects arbitrage or election-portfolio balancing."
  - "Resolves on the certified House election result for Wisconsin's 5th district."
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
    retrieved_at: "2026-10-07T15:02:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 1% contract in a non-competitive district points to mechanical portfolio activity rather than a fundamental reassessment, low signal for a desk but worth flagging for House-majority aggregate models.
