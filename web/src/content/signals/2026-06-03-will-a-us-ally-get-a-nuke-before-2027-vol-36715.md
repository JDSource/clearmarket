---
signal_id: "CMSIG20260603VS09"
signal_slug: "will-a-us-ally-get-a-nuke-before-2027-vol-36715"
headline: "US ally acquires nuke before 2027: 10% on $37K"
semantic_title: "Flows price a US ally acquiring a nuke before 2027 as remote"
telemetry: "10% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-P394L6GV45"
event_slug: "will-a-us-ally-get-a-nuke-before-2027"
event_question: "Will a U.S. ally acquire nuclear weapons by 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x17ba5a7a08bd3f7f87487285c5713e305b8fc98ec4849d5a05ecdf111856c428"
  question_raw: "Will a US ally get a nuke before 2027?"
  current_price: 0.101
  volume_24h_usd: 36715.85
  volume_cumulative_usd: 43559.30296799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket at 10%, one-in-ten probability a US ally achieves nuclear capability before year-end."
  - "$37K in 24h is 84% of all-time volume; contract essentially debuted this session."
  - "South Korea and Saudi Arabia most likely candidates given ongoing nuclear program discussions."
  - "Resolves end of 2026; contract captures tail risk around accelerated proliferation timelines."
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
      poly_vol_24h_usd: 36715.85
sources:
  - label: "ClearMarket market record: Will a U.S. ally acquire nuclear weapons by 2027?"
    url: "https://clearmarket.fyi/events/will-a-us-ally-get-a-nuke-before-2027"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

84% of lifetime volume on day one at 10% signals fresh market attention to near-term proliferation risk, defense and geopolitical desks should note this as a live monitoring contract tied to allied nuclear posture developments.
