---
signal_id: "CMSIG20260812VS02"
signal_slug: "who-will-win-the-2026-south-carolina-rep-vol-623063"
headline: "SC-Sen GOP special primary: 73% on $623K"
semantic_title: "Graham stays the favorite to win SC Republican Senate primary"
telemetry: "73% · $623K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-YGVX09RD56"
event_slug: "kxscrsens-26"
event_question: "Will a South Carolina Republican Senate special primary winner be determined by January 1, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSCRSENS-26-DNOR"
  question_raw: "Who will win the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.73
  volume_24h_usd: 623063.29
  volume_cumulative_usd: 2407788.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices the leading candidate at 73% to win the full South Carolina Republican Senate special primary."
  - "$623K in 24h is 26% of all-time volume, meaningful fresh flow, not a final flush."
  - "Contrast with the first-round contract at 99% suggests runoff risk is still live and being actively traded."
  - "Resolves on the certified winner of the SC Republican Senate special primary."
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
      kalshi_vol_24h_usd: 623063.29
sources:
  - label: "ClearMarket market record: Will a South Carolina Republican Senate special primary"
    url: "https://clearmarket.fyi/events/kxscrsens-26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The gap between the first-round (99%) and outright-win (73%) contracts tells desks a runoff scenario is not fully dismissed, the 26-point spread is where residual risk is being priced.
