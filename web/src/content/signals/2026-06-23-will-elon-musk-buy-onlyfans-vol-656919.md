---
signal_id: "CMSIG20260623VS01"
signal_slug: "will-elon-musk-buy-onlyfans-vol-656919"
headline: "Musk OnlyFans buy: 0% on $657K inflow"
semantic_title: "Market writes off an Elon Musk OnlyFans acquisition"
telemetry: "0% · $657K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-23T10:59:55+00:00"
event_id: "CM-EVT-GD190B3CN0"
event_slug: "will-elon-musk-buy-onlyfans"
event_question: "Will Elon Musk acquire OnlyFans?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xabc61993dc1a40e91c3ae966bae63245906e92f706f98c9382ca4c33d945ccb5"
  question_raw: "Will Elon Musk buy OnlyFans?"
  current_price: 0.005
  volume_24h_usd: 656919.864867
  volume_cumulative_usd: 818416.589837
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices zero probability, market has reached hard consensus against the scenario."
  - "80% of all-time volume traded in 24h, the sharpest single-session concentration in this contract."
  - "Spike likely follows a denial, public statement, or news cycle closing the narrative window."
  - "Resolution context: capital deployed here is expressing conviction the question will settle NO."
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
      poly_vol_24h_usd: 656919.864867
sources:
  - label: "ClearMarket market record: Will Elon Musk acquire OnlyFans?"
    url: "https://clearmarket.fyi/events/will-elon-musk-buy-onlyfans"
    retrieved_at: "2026-06-23T10:59:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The combination of 0% price and 80% all-time volume in one day signals a decisive news catalyst has collapsed the probability, desks can treat the narrative as closed.
