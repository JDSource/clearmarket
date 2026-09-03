---
signal_id: "CMSIG20260903VS02"
signal_slug: "will-nicol-s-maduro-be-sentenced-to-at-l-vol-36156"
headline: "Maduro 60-yr sentence: 34% on $36K volume"
semantic_title: "Maduro 60-year sentence odds hold at 34% through surge"
telemetry: "34% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-DYN1XGWYT5"
event_slug: "maduro-prison-time-527"
event_question: "Will Nicolás Maduro serve prison time?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xce500e0cdc77863e3ae46ea2f8fc7afea2e94e703761e4004065e23fe8629881"
  question_raw: "Will Nicolás Maduro be sentenced to at least 60 years in prison?"
  current_price: 0.34
  volume_24h_usd: 36156.0
  volume_cumulative_usd: 87195.87952400003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 60-year sentence at 34%, meaningful probability but the market leans against it."
  - "24h volume of $36K represents 41% of all-time flow, marking sharp renewed attention to the outcome."
  - "Geopolitical developments or court proceedings in Venezuela are likely pulling fresh capital into the contract."
  - "Resolves on formal sentencing of Nicolás Maduro to at least 60 years in prison."
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
      poly_vol_24h_usd: 36156.0
sources:
  - label: "ClearMarket market record: Will Nicolás Maduro serve prison time?"
    url: "https://clearmarket.fyi/events/maduro-prison-time-527"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 41% all-time volume share at one-in-three odds suggests a material legal or diplomatic catalyst has emerged, warranting close monitoring of Venezuelan judicial proceedings.
