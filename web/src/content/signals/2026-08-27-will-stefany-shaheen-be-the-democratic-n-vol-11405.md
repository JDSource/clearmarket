---
signal_id: "CMSIG20260827VS05"
signal_slug: "will-stefany-shaheen-be-the-democratic-n-vol-11405"
headline: "Shaheen NH-01 Dem nominee: 41% on $11K"
semantic_title: "Stefany Shaheen NH-01 Democratic nominee race stays wide open"
telemetry: "41% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-BHSCBSRT91"
event_slug: "nh-01-democratic-primary-winner"
event_question: "Will a Democrat win the NH-01 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf64108affb6c655b7a50d662d2c508bef1897e40bb3106f7405552c177c92d78"
  question_raw: "Will Stefany Shaheen be the Democratic nominee for NH-01?"
  current_price: 0.41
  volume_24h_usd: 11405.145524
  volume_cumulative_usd: 30171.044663000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket prices Shaheen at 41%, a genuinely contested primary with meaningful opposition priced in."
  - "24h volume of $11K is 38% of all-time, pointing to a specific catalyst driving fresh attention."
  - "At 41%, the market is far from crowning a frontrunner, a challenger event or poll likely triggered the spike."
  - "Resolves on the Democratic primary result for New Hampshire's 1st Congressional District."
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
      poly_vol_24h_usd: 11405.145524
sources:
  - label: "ClearMarket market record: Will a Democrat win the NH-01 primary election?"
    url: "https://clearmarket.fyi/events/nh-01-democratic-primary-winner"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-split 41% price with a 38% all-time volume day signals a contested primary is heating up, desks tracking New Hampshire congressional seats should monitor for challenger announcements or endorsements.
