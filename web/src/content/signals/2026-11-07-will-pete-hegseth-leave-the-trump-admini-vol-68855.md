---
signal_id: "CMSIG20261107VS05"
signal_slug: "will-pete-hegseth-leave-the-trump-admini-vol-68855"
headline: "Hegseth leaves admin: 32% on $69K Polymarket flow"
semantic_title: "Fresh volume tests Hegseth departure odds at roughly one-in-three"
telemetry: "32% · $69K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xeae757a623cf6a8e4d63ab5ebca6739519f87f3506accbfdd75ae514a72bf461"
  question_raw: "Will Pete Hegseth leave the Trump administration before 2027?"
  current_price: 0.32
  volume_24h_usd: 68855.42894000001
  volume_cumulative_usd: 268146.29528900003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "32% pricing gives Hegseth's departure meaningful but sub-50% probability before 2027."
  - "Polymarket records $69K in 24h, 26% of all-time, a steady broad-based flow."
  - "Contrast with Miller (3%) and Bessent (8%) shows Hegseth carries the highest exit risk in this cohort."
  - "Resolves end of 2026; still-open question keeps two-way trading active."
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
      poly_vol_24h_usd: 68855.42894000001
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 32%, Hegseth is the administration exit contract a desk should watch most closely, it is liquid enough and uncertain enough to reprice sharply on any credible personnel news.
