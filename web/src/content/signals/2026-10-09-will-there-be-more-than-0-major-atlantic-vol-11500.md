---
signal_id: "CMSIG20261009VS03"
signal_slug: "will-there-be-more-than-0-major-atlantic-vol-11500"
headline: "2026 major Atlantic hurricane: 99% on $12K"
semantic_title: "Atlantic major hurricane odds stay at 99% through surge"
telemetry: "99% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T14:56:08+00:00"
event_id: "CM-EVT-J6RMPSZY42"
event_slug: "kxhurctotmaj-26dec01"
event_question: "Atlantic major hurricanes, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHURCTOTMAJ-26DEC01-T0"
  question_raw: "Will there be more than 0 major Atlantic hurricanes in 2026?"
  current_price: 0.99
  volume_24h_usd: 11500.21
  volume_cumulative_usd: 41809.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-12-02T15:00:00Z"
bullets:
  - "Kalshi prices at least one major Atlantic hurricane in 2026 at 99%, near-certainty by market consensus."
  - "28% of all-time volume arrived in 24h; modest share but notable given the one-sided price leaves little edge to trade."
  - "Fresh volume at a 99% price implies either late hedging on weather-exposed positions or arbitrage-driven liquidity provision."
  - "Resolves if any 2026 Atlantic storm reaches major hurricane status (Category 3+) before season close."
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
      kalshi_vol_24h_usd: 11500.21
sources:
  - label: "ClearMarket market record: Atlantic major hurricanes, 2026"
    url: "https://clearmarket.fyi/events/kxhurctotmaj-26dec01"
    retrieved_at: "2026-10-09T14:56:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume returning to a 99% contract is unusual and most likely reflects weather-linked book hedging or basis trading by desks with Atlantic storm exposure rather than directional speculation.
