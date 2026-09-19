---
signal_id: "CMSIG20260919VS04"
signal_slug: "will-united-russia-win-between-340-and-3-vol-40579"
headline: "United Russia 340-354 seats: 32% on $41K inflow"
semantic_title: "United Russia hitting 340-354 seats trades at 32% on fresh volume"
telemetry: "32% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T07:47:59+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5ee38949a4ba69f716052e5139b03953e2ecf79e8130d583f92acd87e3c1ca68"
  question_raw: "Will United Russia win between 340 and 354 seats in the next Russian State Duma election?"
  current_price: 0.32
  volume_24h_usd: 40579.29975300001
  volume_cumulative_usd: 148262.814527
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices this seat-band at 32%, a live but below-even probability for the specific range."
  - "27% of all-time volume in 24 hours suggests traders are repositioning ahead of Russian parliamentary election results or forecasts."
  - "At 32%, the market sees the 340-354 bracket as one of several competitive outcome bins, not the consensus landing zone."
  - "Resolution tied to official Russian State Duma seat allocation following the next parliamentary election."
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
      poly_vol_24h_usd: 40579.29975300001
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-19T07:47:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at 32% on a specific seat-band means desks are actively distributing probability across Duma outcome scenarios, useful as a read on how international traders are pricing Kremlin electoral management capability.
