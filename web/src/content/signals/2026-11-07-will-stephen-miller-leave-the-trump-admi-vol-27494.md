---
signal_id: "CMSIG20261107VS06"
signal_slug: "will-stephen-miller-leave-the-trump-admi-vol-27494"
headline: "Miller leaves admin entirely: 4% on $27K"
semantic_title: "Fresh volume returns to Miller full-exit odds, priced near zero"
telemetry: "4% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e2c840905e4089910b2797984e2331e23be0b0071ddcb67c466a120faf05b60"
  question_raw: "Will Stephen Miller leave the Trump administration before 2027?"
  current_price: 0.041
  volume_24h_usd: 27494.337106
  volume_cumulative_usd: 47867.309215999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Stephen Miller leaving the Trump administration entirely before 2027 at just 4%."
  - "$27K in 24h is 57% of all-time volume, the contract is newly active, almost certainly driven by the Deputy Chief spike (Spike 0)."
  - "The gap between 95% (Deputy role exit, Spike 0) and 4% (full admin exit) implies the market expects a role change, not a departure."
  - "Resolves end-2026."
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
      poly_vol_24h_usd: 27494.337106
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Reading Spikes 0 and 6 together, a desk should interpret the market as pricing a title/role shuffle for Miller rather than an outright White House exit, a nuanced personnel signal worth tracking.
