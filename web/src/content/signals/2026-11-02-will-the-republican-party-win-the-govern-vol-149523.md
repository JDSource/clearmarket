---
signal_id: "CMSIG20261102VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-149523"
headline: "Vermont GOP governor: 69% on $150K volume spike"
semantic_title: "Vermont GOP governorship stays favored through a volume surge"
telemetry: "69% · $150K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.69
  volume_24h_usd: 149523.99
  volume_cumulative_usd: 426230.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 69%, a solid favorite in a state that has elected a GOP governor despite its deep-blue presidential lean."
  - "24h volume of $150K is 35% of the contract's entire all-time volume, an outsized one-day share."
  - "Vermont's incumbent Republican governor dynamic makes this a structurally unusual market; fresh volume may reflect attention from national Senate map traders."
  - "Resolves on the 2026 Vermont gubernatorial election."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 149523.99
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single day absorbing 35% of all-time volume on a 69% contract points to traders cross-referencing New England gubernatorial and Senate positioning simultaneously.
