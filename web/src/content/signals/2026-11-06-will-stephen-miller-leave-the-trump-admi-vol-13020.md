---
signal_id: "CMSIG20261106VS04"
signal_slug: "will-stephen-miller-leave-the-trump-admi-vol-13020"
headline: "Miller exit before 2027: 17% on $13K at Polymarket"
semantic_title: "Stephen Miller exit before 2027 trades as a long shot at 17%"
telemetry: "17% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e2c840905e4089910b2797984e2331e23be0b0071ddcb67c466a120faf05b60"
  question_raw: "Will Stephen Miller leave the Trump administration before 2027?"
  current_price: 0.17
  volume_24h_usd: 13020.824161
  volume_cumulative_usd: 20372.97211
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 17%, the market prices Miller's departure from the administration before year-end as a low-probability event."
  - "$13K in 24h is 64% of all-time volume, nearly all price discovery is concentrated in this session."
  - "Co-movement with the Rubio exit spike suggests a broader administration-reshuffling narrative is circulating."
  - "Resolves if Miller leaves any Trump administration role before Jan 1, 2027."
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
      poly_vol_24h_usd: 13020.824161
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 64% all-time volume share on a secondary administration-exit contract, trading in tandem with the Rubio contracts, suggests the market is pricing a generalized West Wing disruption scenario rather than an individual-specific rumor.
