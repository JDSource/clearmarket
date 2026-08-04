---
signal_id: "CMSIG20260804VS05"
signal_slug: "will-cindy-holscher-win-the-2026-kansas-vol-15764"
headline: "Holscher KS Gov Dem primary: 91% on $16K surge"
semantic_title: "Heavy trading backs Holscher as the Kansas Dem governor pick"
telemetry: "91% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-2F4PBBH7S6"
event_slug: "kansas-governor-democratic-primary-winner"
event_question: "Will a Democrat win the Kansas Governor Democratic Primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8bb083247bc0525ae99c364b72394f3cd8e8d15bd4ed7ce08bd71079bba2bda6"
  question_raw: "Will Cindy Holscher win the 2026 Kansas Governor Democratic primary election?"
  current_price: 0.91
  volume_24h_usd: 15764.137855
  volume_cumulative_usd: 38173.498488
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "At 91%, Polymarket prices Holscher as the strong frontrunner in the Kansas Democratic gubernatorial primary."
  - "24h volume of $15.7K is 41% of all-time, notable concentration for a state-level down-ballot contract."
  - "Elevated attention on a Kansas Democratic primary may reflect national party strategists tracking pickup opportunities."
  - "Resolves on the certified Kansas Democratic gubernatorial primary outcome."
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
      poly_vol_24h_usd: 15764.137855
sources:
  - label: "ClearMarket market record: Will a Democrat win the Kansas Governor Democratic Prim"
    url: "https://clearmarket.fyi/events/kansas-governor-democratic-primary-winner"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty-one percent of lifetime volume in one session on a Kansas Democratic primary suggests a desk-relevant signal: either primary day is imminent or new public polling has sharpened the field dramatically.
