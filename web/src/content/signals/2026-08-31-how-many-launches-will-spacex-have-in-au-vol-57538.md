---
signal_id: "CMSIG20260831VS01"
signal_slug: "how-many-launches-will-spacex-have-in-au-vol-57538"
headline: "SpaceX Aug launches: 99% as month closes"
semantic_title: "SpaceX August launch count trades near certainty on Kalshi"
telemetry: "99% · $58K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-31T15:48:06+00:00"
event_id: "CM-EVT-44DGF8Z1F9"
event_slug: "kxspacexcount-26aug"
event_question: "SpaceX launches, August 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSPACEXCOUNT-26AUG-12"
  question_raw: "How many launches will SpaceX have in Aug 2026?"
  current_price: 0.99
  volume_24h_usd: 57538.66
  volume_cumulative_usd: 180206.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-07T14:00:00Z"
bullets:
  - "Kalshi prices the August launch target at 99%, near-certain resolution in the affirmative."
  - "24h volume of $57.5K is 32% of all-time, with the contract expiring today, August 31."
  - "Same-day resolution is pulling in settlement traders locking in the final tick."
  - "Resolves tonight based on confirmed SpaceX launch count for August 2026."
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
      kalshi_vol_24h_usd: 57538.66
sources:
  - label: "ClearMarket market record: SpaceX launches, August 2026"
    url: "https://clearmarket.fyi/events/kxspacexcount-26aug"
    retrieved_at: "2026-08-31T15:48:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

End-of-month settlement compression is the driver, the volume surge is mechanical rather than informational, but confirms market consensus that the launch count is already met.
