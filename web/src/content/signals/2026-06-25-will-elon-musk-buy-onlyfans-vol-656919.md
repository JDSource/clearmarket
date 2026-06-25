---
signal_id: "CMSIG20260625VS01"
signal_slug: "will-elon-musk-buy-onlyfans-vol-656919"
headline: "Musk buys OnlyFans: 0% on $657K surge"
semantic_title: "Market writes off an Elon Musk OnlyFans acquisition"
telemetry: "0% · $657K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-25T10:39:33+00:00"
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
  - "Polymarket prices the acquisition at 0%, capital deployed overwhelmingly to the 'No' side."
  - "80% of all-time volume transacted in 24h, the sharpest single-session consensus flush on record for this contract."
  - "Fresh attention likely triggered by a public denial, Musk statement, or viral rumor requiring institutional clarification."
  - "Contract pricing is terminal; residual volume reflects cleanup, not genuine uncertainty."
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
    retrieved_at: "2026-06-25T10:39:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume-to-price configuration signals a rumor-squash event, a desk can file this as noise resolved, with the 80% all-time share confirming the market absorbed and dismissed the thesis in a single session.
