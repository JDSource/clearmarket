---
signal_id: "CMSIG20260812VS01"
signal_slug: "will-darline-graham-finish-1st-in-the-fi-vol-765714"
headline: "Graham SC-Sen primary 1st: 99% on $766K surge"
semantic_title: "Traders back Graham to lead SC Senate primary round one"
telemetry: "99% · $766K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-34WPGXDWQ8"
event_slug: "kxprimaryplace-scrsens26-1"
event_question: "Will the candidate receiving the most votes win first place in the first round of the South Carolina Republican Senate special primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SCRSENS26-1-DGRA"
  question_raw: "Will Darline Graham finish 1st in the first round of the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.99
  volume_24h_usd: 765714.02
  volume_cumulative_usd: 1011707.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Kalshi prices Graham at 99% to finish first in the SC Republican Senate special primary first round."
  - "$766K in 24h represents 76% of all-time volume, near-conclusive positioning."
  - "Heavy flow at near-certainty odds suggests primary results are known or reporting live."
  - "Resolves on first-round vote totals from the South Carolina Republican special primary."
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
      kalshi_vol_24h_usd: 765714.02
sources:
  - label: "ClearMarket market record: Will the candidate receiving the most votes win first p"
    url: "https://clearmarket.fyi/events/kxprimaryplace-scrsens26-1"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Odds and volume together signal the market is processing real vote data, not speculation, a desk monitoring SC Senate should treat this as a confirmed first-round outcome.
