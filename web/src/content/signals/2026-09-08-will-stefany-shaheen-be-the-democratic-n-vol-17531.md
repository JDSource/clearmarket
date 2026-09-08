---
signal_id: "CMSIG20260908VS02"
signal_slug: "will-stefany-shaheen-be-the-democratic-n-vol-17531"
headline: "Shaheen NH-01 Dem primary: 17% on $18K surge"
semantic_title: "Shaheen NH-01 bid stays a long shot through a volume spike"
telemetry: "17% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-BHSCBSRT91"
event_slug: "nh-01-democratic-primary-winner"
event_question: "Will a Democrat win the NH-01 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf64108affb6c655b7a50d662d2c508bef1897e40bb3106f7405552c177c92d78"
  question_raw: "Will Stefany Shaheen be the Democratic nominee for NH-01?"
  current_price: 0.17
  volume_24h_usd: 17531.28338
  volume_cumulative_usd: 66536.308929
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket marks Shaheen at 17%, the market assigns her a meaningful but minority chance against Sullivan."
  - "$17.5K in 24h is 26% of all-time volume, mirroring the Sullivan spike as the same primary draws both sides."
  - "Paired volume across Sullivan and Shaheen contracts points to active two-sided positioning on the same race."
  - "Both contracts resolve on the Democratic primary outcome for NH-01."
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
      poly_vol_24h_usd: 17531.28338
sources:
  - label: "ClearMarket market record: Will a Democrat win the NH-01 primary election?"
    url: "https://clearmarket.fyi/events/nh-01-democratic-primary-winner"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Shaheen and Sullivan spikes are best read together, the same primary catalyst is drawing traders to both sides, and a desk should monitor for any development that compresses Sullivan's lead toward 75%.
