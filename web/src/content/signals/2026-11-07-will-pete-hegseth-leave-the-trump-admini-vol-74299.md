---
signal_id: "CMSIG20261107VS05"
signal_slug: "will-pete-hegseth-leave-the-trump-admini-vol-74299"
headline: "Hegseth leaves admin: 32% on $74K surge"
semantic_title: "Hegseth exit odds hold at 32% through a volume push"
telemetry: "32% · $74K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xeae757a623cf6a8e4d63ab5ebca6739519f87f3506accbfdd75ae514a72bf461"
  question_raw: "Will Pete Hegseth leave the Trump administration before 2027?"
  current_price: 0.32
  volume_24h_usd: 74299.75838
  volume_cumulative_usd: 274017.046664
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Hegseth leaving before 2027 at 32%, elevated tail risk, nearly one-in-three implied probability."
  - "$74K in 24h is 27% of all-time volume, the largest single-session share the contract has seen."
  - "32% is a meaningfully high exit probability for a sitting cabinet secretary, suggesting ongoing controversy is being priced."
  - "Resolves end-2026; weeks remain for a potential personnel change."
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
      poly_vol_24h_usd: 74299.75838
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 32% departure probability with accelerating volume is a live risk signal for a desk tracking defense policy continuity, this is not a settled market and warrants monitoring for catalyst news.
