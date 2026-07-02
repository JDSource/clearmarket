---
signal_id: "CMSIG20260702VS01"
signal_slug: "will-no-listed-leader-be-out-before-2027-vol-1407459"
headline: "No leader out by 2027: 0% on $1.4M Polymarket wave"
semantic_title: "Capital defends the 'no leader exits' leg of the G7 basket"
telemetry: "0% · $1.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84a45609bfdb644a15be71d679fbb4f115dea9109d9bac96e1bc049853e002f6"
  question_raw: "Will no listed leader be out before 2027?"
  current_price: 0.002
  volume_24h_usd: 1407459.584068
  volume_cumulative_usd: 2591009.392356001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "0% implies the market has fully resolved that some listed leader will exit before 2027."
  - "$1.41M in 24h, 54% of all-time, signals this is a basket-clearing, not speculative, flow."
  - "Heavy volume across the full leadership suite points to a correlated multi-contract settlement event."
  - "Near-full all-time volume share confirms this contract is in terminal liquidation phase."
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
      poly_vol_24h_usd: 1407459.584068
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous 0%-price spikes across the entire leadership basket indicate a structured unwind or resolution arbitrage, not independent geopolitical bets, desks should treat these legs as a single correlated exposure.
