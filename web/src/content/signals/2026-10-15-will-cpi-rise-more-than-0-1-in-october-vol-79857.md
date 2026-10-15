---
signal_id: "CMSIG20261015VS02"
signal_slug: "will-cpi-rise-more-than-0-1-in-october-vol-79857"
headline: "October CPI >0.1%: 78% on $79.9K Kalshi volume"
semantic_title: "Traders back a modest October CPI read above 0.1%"
telemetry: "78% · $80K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.1"
  question_raw: "Will CPI rise more than 0.1% in October 2026?"
  current_price: 0.78
  volume_24h_usd: 79857.18
  volume_cumulative_usd: 133213.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "78% odds imply traders see a CPI print above 0.1% as the base case, not a tail risk."
  - "$79.9K in 24h is 60% of all-time, a decisive single-session concentration."
  - "Paired with Spike 0 at 51% for >0.2%, the spread reveals traders pricing the modal outcome between 0.1% and 0.2%."
  - "Resolves on official BLS October 2026 CPI release."
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
      kalshi_vol_24h_usd: 79857.18
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Reading Spikes 0 and 2 together, the market's implied modal CPI range of 0.1%, 0.2% is the most actionable signal for rates desks calibrating November Fed meeting positioning.
