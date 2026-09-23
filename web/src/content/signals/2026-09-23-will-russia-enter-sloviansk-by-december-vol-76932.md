---
signal_id: "CMSIG20260923VS01"
signal_slug: "will-russia-enter-sloviansk-by-december-vol-76932"
headline: "Russia Sloviansk by Dec 31: 12% on $77K burst"
semantic_title: "Russia taking Sloviansk by year-end stays a long shot at 12%"
telemetry: "12% · $77K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T07:48:28+00:00"
event_id: "CM-EVT-7G3FWY0RL4"
event_slug: "which-cities-will-russia-enter-by-december-31"
event_question: "Will Russia enter any additional cities by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4aa5c6bd2a179244d98ba714dba4441e4bf5f99f27a657b8d967f8f67cfe041"
  question_raw: "Will Russia enter Sloviansk by December 31, 2026?"
  current_price: 0.12
  volume_24h_usd: 76932.598371
  volume_cumulative_usd: 164180.27902899997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 12%, Polymarket prices a Russian capture of Sloviansk before year-end as unlikely but not negligible."
  - "24h volume of $77K is 47% of all-time, nearly half the contract's lifetime liquidity traded in one day."
  - "A near-half-life volume burst on a low-probability geopolitical contract often signals fresh battlefield reporting or intelligence assessments."
  - "Contract resolves December 31, 2026, tied to confirmed Russian control of Sloviansk."
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
      poly_vol_24h_usd: 76932.598371
sources:
  - label: "ClearMarket market record: Will Russia enter any additional cities by December 31?"
    url: "https://clearmarket.fyi/events/which-cities-will-russia-enter-by-december-31"
    retrieved_at: "2026-09-23T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag this as a geopolitical risk monitor, a 47% single-session volume share on a 12% contract implies traders are stress-testing downside scenarios, likely prompted by front-line movement reports.
