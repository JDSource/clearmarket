---
signal_id: "CMSIG20261020VS00"
signal_slug: "kim-jong-un-out-as-supreme-leader-of-nor-vol-225010"
headline: "Kim Jong Un out by Dec 31: 6% on $225K surge"
semantic_title: "Traders pile into Kim Jong Un exit bet at long-shot 6%"
telemetry: "6% · $225K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T13:16:06+00:00"
event_id: "CM-EVT-HR6HRVY940"
event_slug: "kim-jong-un-out-as-supreme-leader-of-north-korea-before-2027"
event_question: "Will Kim Jong Un no longer be the Supreme Leader of North Korea by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9ed2a24391123c685db5c48ea043ee9bd714a144be4a9a0c48d146d521cf9f93"
  question_raw: "Kim Jong Un out as Supreme Leader of North Korea by December 31, 2026?"
  current_price: 0.059
  volume_24h_usd: 225010.49773200002
  volume_cumulative_usd: 435788.49047500006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices only a 6% chance Kim Jong Un loses power by year-end, a deep long-shot read."
  - "24h volume of $225K equals 52% of all-time handle, signaling a sharp spike in fresh attention."
  - "Surge likely driven by external intelligence reports or regional signals prompting speculative positioning."
  - "Resolves December 31, 2026; low price means most capital is landing on the 'No' side."
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
      poly_vol_24h_usd: 225010.49773200002
sources:
  - label: "ClearMarket market record: Will Kim Jong Un no longer be the Supreme Leader of Nor"
    url: "https://clearmarket.fyi/events/kim-jong-un-out-as-supreme-leader-of-north-korea-before-2027"
    retrieved_at: "2026-10-20T13:16:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single-session volume burst equal to half the contract's lifetime handle flags elevated desk interest in tail-risk North Korea leadership scenarios, worth monitoring for accompanying intelligence or diplomatic signals.
