---
signal_id: "CMSIG20261027VS05"
signal_slug: "will-likud-win-30-34-seats-in-the-2026-i-vol-326586"
headline: "Likud 30-34 seats: 5% on $327K flow"
semantic_title: "Likud landing 30-34 seats seen as a long shot at 5%"
telemetry: "5% · $327K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc855714184ac46005a7897c68f274147f0abf1fde791421541edb065fa65a1e4"
  question_raw: "Will Likud win 30-34 seats in the 2026 Israeli legislative election?"
  current_price: 0.049
  volume_24h_usd: 326586.043465
  volume_cumulative_usd: 883667.797321
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices a 30-34 seat outcome for Likud at just 5%, the market sees this range as highly unlikely."
  - "24h volume of $327K is 37% of all-time, showing sustained interest in granular Likud seat-band positioning."
  - "Read alongside the 2% on 35+ seats, traders are overwhelmingly betting Likud finishes well below 30 seats."
  - "Resolves on official 2026 Knesset seat count for Likud."
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
      poly_vol_24h_usd: 326586.043465
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The seat-band contracts collectively tell a coherent story of Likud collapse, desks should cross-reference the 21% lead-party price with the sub-30-seat implied probability to frame downside scenarios.
