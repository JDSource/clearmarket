---
signal_id: "CMSIG20261005VS07"
signal_slug: "will-the-democratic-party-win-the-mn-02-vol-12788"
headline: "MN-02 Dem seat: 91% on $13K vol spike"
semantic_title: "MN-02 Democratic hold commands near-certain odds at 91%"
telemetry: "91% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-Y9F1K0F3B5"
event_slug: "mn-02-house-election-winner"
event_question: "Will the Minnesota 2nd Congressional District House Election result in a Republican winner in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7319fceb8b5a315eae707028bd654463e48acec082565ef1abd3cc18b424ff6f"
  question_raw: "Will the Democratic Party win the MN-02 House seat?"
  current_price: 0.912
  volume_24h_usd: 12788.845441000001
  volume_cumulative_usd: 28180.721944000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Democrats retaining MN-02 at 91%, the market treats this as close to settled."
  - "45% of all-time volume landed in 24 hours, the second-highest all-time concentration share in this batch."
  - "A spike on a 91% contract may reflect late hedgers covering a small Republican-upset tail risk."
  - "Resolves on the MN-02 House general election result."
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
      poly_vol_24h_usd: 12788.845441000001
sources:
  - label: "ClearMarket market record: Will the Minnesota 2nd Congressional District House Ele"
    url: "https://clearmarket.fyi/events/mn-02-house-election-winner"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High all-time volume share on a near-certain contract points to tail-risk hedging activity rather than directional conviction, a desk is buying insurance on a low-probability but high-impact upset scenario.
