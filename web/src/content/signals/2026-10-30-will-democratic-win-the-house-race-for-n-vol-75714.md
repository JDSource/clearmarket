---
signal_id: "CMSIG20261030VS06"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-75714"
headline: "NC-11 Dems Kalshi: 84% on $76K inflow"
semantic_title: "Fresh money backs Democrats in NC-11 on Kalshi at 84%"
telemetry: "84% · $76K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-DEM"
  question_raw: "Will Democratic win the House race for NC-11?"
  current_price: 0.84
  volume_24h_usd: 75714.05
  volume_cumulative_usd: 261914.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi independently prices Democrats winning NC-11 at 84%, matching the Polymarket read."
  - "24h volume of $76K is 29% of all-time $262K, a meaningful single-day tranche on a larger pool."
  - "Cross-venue alignment at 84% with simultaneous spikes reinforces the Democratic-lean consensus."
  - "Resolution on NC-11 House race result; see Spikes 0 and 2 for Polymarket cross-reference."
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
      kalshi_vol_24h_usd: 75714.05
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Correlated NC-11 volume surges across Kalshi and Polymarket at the same 84% price confirm venue-independent consensus and reduce the likelihood of exploitable cross-market mispricing.
