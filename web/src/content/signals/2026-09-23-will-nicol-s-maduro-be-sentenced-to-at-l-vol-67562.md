---
signal_id: "CMSIG20260923VS02"
signal_slug: "will-nicol-s-maduro-be-sentenced-to-at-l-vol-67562"
headline: "Maduro 60-yr sentence: 30% on $68K volume surge"
semantic_title: "Odds on a Maduro 60-year sentence stay below 50% at 30%"
telemetry: "30% · $68K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-DYN1XGWYT5"
event_slug: "maduro-prison-time-527"
event_question: "Will Nicolás Maduro serve prison time?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xce500e0cdc77863e3ae46ea2f8fc7afea2e94e703761e4004065e23fe8629881"
  question_raw: "Will Nicolás Maduro be sentenced to at least 60 years in prison?"
  current_price: 0.3
  volume_24h_usd: 67562.62
  volume_cumulative_usd: 159512.53398
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "At 30%, Polymarket prices a 60-year-or-more prison sentence for Maduro as unlikely but with meaningful probability."
  - "24h volume of $68K is 42% of all-time handle, a concentrated burst of fresh attention on this contract."
  - "The spike likely reflects news around ICC proceedings, U.S. sanctions escalation, or Venezuelan political developments."
  - "Contract resolves on a confirmed judicial sentence of at least 60 years against Nicolás Maduro."
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
      poly_vol_24h_usd: 67562.62
sources:
  - label: "ClearMarket market record: Will Nicolás Maduro serve prison time?"
    url: "https://clearmarket.fyi/events/maduro-prison-time-527"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk tracking Venezuela exposure or Latin American political risk should treat this volume surge as a signal to monitor legal and diplomatic developments, the 30% odds imply real but minority probability of a regime-ending judicial event.
