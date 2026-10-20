---
signal_id: "CMSIG20261020VS02"
signal_slug: "will-likud-win-25-29-seats-in-the-2026-i-vol-47854"
headline: "Likud 25-29 seats 2026 election: 22% on $48K volume"
semantic_title: "Likud landing 25-29 seats picks up heavy volume at 22%"
telemetry: "22% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd63e1e2db811ba09972cbac9810edcca72ffdc1d195c03547ac0be2fb7a3c3d7"
  question_raw: "Will Likud win 25-29 seats in the 2026 Israeli legislative election?"
  current_price: 0.22
  volume_24h_usd: 47854.321202
  volume_cumulative_usd: 167985.240636
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices 22% on Likud winning 25-29 seats in the 2026 Israeli legislative election, below-median band outcome."
  - "$48K in 24h is 28% of all-time volume, a meaningful but not dominant share, suggesting steady fresh interest rather than panic."
  - "Simultaneous volume spikes across multiple Likud seat-band contracts suggest active cross-market positioning on election outcome distribution."
  - "Resolution depends on official 2026 Israeli election results; 22% implies traders see higher-seat bands as more likely."
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
      poly_vol_24h_usd: 47854.321202
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume across three Likud seat-band markets signals desks are actively mapping the seat distribution curve, not just directional election exposure.
