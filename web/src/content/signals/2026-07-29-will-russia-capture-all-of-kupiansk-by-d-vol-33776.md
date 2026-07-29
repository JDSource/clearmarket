---
signal_id: "CMSIG20260729VS01"
signal_slug: "will-russia-capture-all-of-kupiansk-by-d-vol-33776"
headline: "Russia Kupiansk by Dec 31: 10% on $34K"
semantic_title: "Odds hold low on Russia taking all of Kupiansk by Dec 31"
telemetry: "10% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-FYD8DLYRM3"
event_slug: "will-russia-capture-all-of-kupiansk-by"
event_question: "Will Russia capture all of Kupiansk by the end of 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa72d5a239c10ac6cb67f109b05513ae3a23db39ab7c5d4e2afa93719f20471ba"
  question_raw: "Will Russia capture all of Kupiansk by December 31?"
  current_price: 0.098
  volume_24h_usd: 33776.950407
  volume_cumulative_usd: 67755.887654
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket holds Russia full capture of Kupiansk at 10%, market discounts the scenario heavily."
  - "50% of all-time volume landed in the last 24h, signaling a sudden doubling of attention."
  - "Front-line activity or battlefield reporting near Kupiansk likely drove traders to test the line."
  - "Resolves December 31, 2026; five months of combat remaining against current 10% pricing."
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
      poly_vol_24h_usd: 33776.950407
sources:
  - label: "ClearMarket market record: Will Russia capture all of Kupiansk by the end of 2025?"
    url: "https://clearmarket.fyi/events/will-russia-capture-all-of-kupiansk-by"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all lifetime volume arriving in one session suggests a specific tactical development near Kupiansk is prompting desks to re-examine the year-end capture probability.
