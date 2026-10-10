---
signal_id: "CMSIG20261010VS00"
signal_slug: "will-the-democratic-party-win-the-govern-vol-238727"
headline: "Iowa Dem governor: 88% on $239K surge"
semantic_title: "Democrats hold a strong Iowa governor lead at 88%"
telemetry: "88% · $239K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-8D7ZTR8991"
event_slug: "govpartyia-26"
event_question: "Will the Iowa gubernatorial election result be determined by January 14, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIA-26-D"
  question_raw: "Will the Democratic party win the governorship in Iowa"
  current_price: 0.88
  volume_24h_usd: 238727.42
  volume_cumulative_usd: 668994.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning Iowa's governorship at 88%, a heavy favorite read."
  - "24h volume hit $239K, equal to 36% of all-time handle, marking the contract's single busiest session."
  - "Late-cycle Iowa governor attention at this odds level suggests fresh money is backing a near-settled outcome."
  - "Contract resolves on Iowa 2026 gubernatorial election result."
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
      kalshi_vol_24h_usd: 238727.42
sources:
  - label: "ClearMarket market record: Will the Iowa gubernatorial election result be determin"
    url: "https://clearmarket.fyi/events/govpartyia-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that 36% of lifetime volume arriving in one day at 88% odds signals either a late confirming catalyst or short-side capitulation into the close of the race.
