---
signal_id: "CMSIG20260704VS01"
signal_slug: "will-mahmoud-abbas-be-the-next-leader-ou-vol-609232"
headline: "Abbas next out: 0% on $609K volume spike"
semantic_title: "Abbas written off as next leader out, capital stacks at zero"
telemetry: "0% · $609K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-04T10:05:37+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaffa29d449f3b5a46d933bc412f7ae823e9f5216257c8c6e5bd695a9e2c0392b"
  question_raw: "Will Mahmoud Abbas be the next leader out before 2027?"
  current_price: 0.004
  volume_24h_usd: 609232.271332
  volume_cumulative_usd: 805942.2860289997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 0%, market firmly rejects Abbas as the next leader to exit before 2027."
  - "24h volume $609K represents 76% of all-time flow, the heaviest single-session concentration in this contract."
  - "Elevated attention may reflect spillover from Netanyahu contract activity and linked Middle East leadership positioning."
  - "Resolution requires Abbas to be the first named leader to depart office before Jan 1 2027."
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
      poly_vol_24h_usd: 609232.271332
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-04T10:05:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total all-time volume printing in one session at zero price indicates desks are closing residual exposure rather than initiating; the Abbas contract appears to be clearing as a companion trade to broader Mideast leadership book cleanup.
