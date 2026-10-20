---
signal_id: "CMSIG20261020VS04"
signal_slug: "will-likud-win-20-24-seats-in-the-2026-i-vol-21547"
headline: "Likud 20-24 seats 2026 election: 38% on $22K volume"
semantic_title: "Likud at 20-24 seats draws fresh volume with 38% odds"
telemetry: "38% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3135bdbe2e03604ff34296d209bccf73d7e90b47f634bf47becffaad852c064d"
  question_raw: "Will Likud win 20-24 seats in the 2026 Israeli legislative election?"
  current_price: 0.38
  volume_24h_usd: 21547.56216
  volume_cumulative_usd: 57926.285089
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices 38% on Likud winning 20-24 seats, the single most-likely individual seat band across the three contracts."
  - "$22K in 24h is 37% of all-time volume, part of a coordinated cross-contract move in Israeli election markets today."
  - "38% in this band against 22% in the 25-29 band implies the market favors a weaker Likud performance over a moderate one."
  - "Resolution tied to official 2026 Israeli election results; distribution across bands still leaves the seat count highly uncertain."
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
      poly_vol_24h_usd: 21547.56216
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 20-24 band pricing at 38% while the 25-29 band sits at 22% tells desks the market's modal call is a reduced-but-still-governing Likud, useful framing for Israeli political risk models.
