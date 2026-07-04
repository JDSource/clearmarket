---
signal_id: "CMSIG20260704VS02"
signal_slug: "will-a-us-ally-get-a-nuke-before-2027-vol-57158"
headline: "US-ally nuke by 2027: 6% on $57K inflow"
semantic_title: "Tail risk stacks in US-ally nuclear acquisition by 2027"
telemetry: "6% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-04T10:05:37+00:00"
event_id: "CM-EVT-P394L6GV45"
event_slug: "will-a-us-ally-get-a-nuke-before-2027"
event_question: "Will a U.S. ally acquire nuclear weapons by 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x17ba5a7a08bd3f7f87487285c5713e305b8fc98ec4849d5a05ecdf111856c428"
  question_raw: "Will a US ally get a nuke before 2027?"
  current_price: 0.065
  volume_24h_usd: 57158.62291300001
  volume_cumulative_usd: 110490.77772099999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 6%, a small but non-trivial tail probability assigned to a US ally acquiring nuclear weapons before 2027."
  - "24h volume $57K is 52% of all-time, suggesting renewed institutional attention to a previously thin contract."
  - "Context likely includes Middle East security architecture debates and reported Saudi-Israeli normalization contingencies."
  - "Contract resolves if any recognized US ally successfully tests or declares a nuclear device before Jan 1 2027."
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
      poly_vol_24h_usd: 57158.62291300001
sources:
  - label: "ClearMarket market record: Will a U.S. ally acquire nuclear weapons by 2027?"
    url: "https://clearmarket.fyi/events/will-a-us-ally-get-a-nuke-before-2027"
    retrieved_at: "2026-07-04T10:05:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume doubling the contract's lifetime activity in a single session at 6% signals that geopolitical desks are beginning to price a non-zero tail on near-term nuclear proliferation among US partners, warranting monitoring as a macro risk indicator.
