---
signal_id: "CMSIG20260923VS04"
signal_slug: "will-the-republican-party-win-the-ca-42-vol-12606"
headline: "CA-42 GOP seat: 3% as 52% all-time vol hits"
semantic_title: "CA-42 Republican bid trades at 3% on half its lifetime volume"
telemetry: "3% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-QNPZ7LYHZ2"
event_slug: "ca-42-house-election-winner"
event_question: "CA-42 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa31d5d95f8c7c96de1194e7023c028380b5d4a00b6faef2fdaf62bc6f71af4f6"
  question_raw: "Will the Republican Party win the CA-42 House seat?"
  current_price: 0.034
  volume_24h_usd: 12606.82
  volume_cumulative_usd: 24426.921465999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at just 3% in CA-42, a near-zero probability in a heavily Democratic California district."
  - "52% of all-time volume landed in the last 24 hours, the single largest daily share of any contract in this batch."
  - "A majority-of-lifetime volume day on a 3% contract is unusual; it may reflect a coordinated position or odds arbitrage attempt."
  - "Resolves on the November 2026 CA-42 House general election result."
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
      poly_vol_24h_usd: 12606.82
sources:
  - label: "ClearMarket market record: CA-42 House Election Winner"
    url: "https://clearmarket.fyi/events/ca-42-house-election-winner"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When more than half a contract's lifetime volume arrives in one session at a 3% price, a desk should investigate whether a structural mispricing is being pressed or whether this is noise, either way, the signal-to-noise ratio is low but the anomaly is notable.
