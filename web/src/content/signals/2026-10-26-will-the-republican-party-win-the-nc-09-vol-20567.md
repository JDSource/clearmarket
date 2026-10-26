---
signal_id: "CMSIG20261026VS05"
signal_slug: "will-the-republican-party-win-the-nc-09-vol-20567"
headline: "GOP NC-09 House seat: 66% on $20K surge"
semantic_title: "Republican NC-09 contract stays a 2-to-1 favorite through fresh volume"
telemetry: "66% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x31727e0e298757e552661f62733cc401c6066b80a7d2607d2ac56b729eb15a00"
  question_raw: "Will the Republican Party win the NC-09 House seat?"
  current_price: 0.66
  volume_24h_usd: 20567.161022999997
  volume_cumulative_usd: 55020.619039
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Republicans priced at 66% in NC-09, market holds a clear but not dominant favorite stance."
  - "37% of all-time volume arrived in 24 hours, echoing the heavier same-seat Democratic spike."
  - "Paired spikes on both NC-09 contracts suggest active two-sided repricing of the district."
  - "Resolves on the NC-09 general election result."
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
      poly_vol_24h_usd: 20567.161022999997
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume surges on both sides of NC-09 indicate a contested market view, a desk should read the Democrat/Republican price pair together as a live competitiveness gauge rather than two isolated signals.
