---
signal_id: "CMSIG20260727VS05"
signal_slug: "will-average-gas-prices-be-above-4-vol-26772"
headline: "US gas above $4.00: 99% on $27K volume"
semantic_title: "Buyers back the gas-above-$4.00 contract at near-certainty"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.00"
  question_raw: "Will average **gas prices** be above $4.00?"
  current_price: 0.99
  volume_24h_usd: 26772.0
  volume_cumulative_usd: 81008.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average US gas above $4.00 at 99%, the round-number floor treated as no contest."
  - "24h volume $27K is 33% of all-time; lower concentration suggests this contract has older, deeper liquidity."
  - "The $4.00 level is the widest psychological threshold in the ladder and garners the most historical trading."
  - "99% across $4.00, $4.02, and $4.04 strikes paints a consistent picture of elevated pump prices."
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
      kalshi_vol_24h_usd: 26772.0
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Persistent 99% pricing across the entire gas ladder tells desks that retail fuel cost pressures remain entrenched, the $4.06 contract at 90% is the first point of real market uncertainty worth monitoring.
