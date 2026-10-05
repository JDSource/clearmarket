---
signal_id: "CMSIG20261005VS05"
signal_slug: "will-the-republican-party-win-the-govern-vol-33470"
headline: "Iowa GOP governor: 13% Dem odds on $33K"
semantic_title: "Iowa governor stays a long shot for Democrats at 13%"
telemetry: "13% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-8D7ZTR8991"
event_slug: "govpartyia-26"
event_question: "Will the Iowa gubernatorial election result be determined by January 14, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIA-26-R"
  question_raw: "Will the Republican party win the governorship in Iowa"
  current_price: 0.13
  volume_24h_usd: 33470.4
  volume_cumulative_usd: 87005.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Republicans as overwhelming Iowa governor favorites, Democrats at just 13%."
  - "38% of all-time volume arrived in 24 hours, an outsized session for a lopsided contract."
  - "Fresh volume on a heavily skewed market may reflect hedging or a speculative bet on a surprise."
  - "Resolves on the Iowa gubernatorial election result."
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
      kalshi_vol_24h_usd: 33470.4
sources:
  - label: "ClearMarket market record: Will the Iowa gubernatorial election result be determin"
    url: "https://clearmarket.fyi/events/govpartyia-26"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Elevated volume on a deeply one-sided contract warrants attention, either a desk is hedging a broader Midwest political portfolio or new information is circulating that is not yet reflected in the price.
