---
signal_id: "CMSIG20261006VS03"
signal_slug: "will-above-30000-jobs-be-added-in-octobe-vol-10151"
headline: "Oct jobs above 30K: 70% on $10K; 83% all-time vol"
semantic_title: "October jobs above 30K holds at 70% through a volume surge"
telemetry: "70% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T14:43:21+00:00"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "Nonfarm payrolls, October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T30000"
  question_raw: "Will above 30000 jobs be added in October 2026?"
  current_price: 0.7
  volume_24h_usd: 10151.0
  volume_cumulative_usd: 12195.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi prices 30K+ October job adds at 70%, a moderately confident baseline for labor growth."
  - "83% of all-time volume landed in 24h, this contract is almost entirely a today story."
  - "Spike likely driven by early labor-market data releases or ADP/claims prints feeding positioning."
  - "Resolves on October 2026 nonfarm payrolls release; thin prior history makes this reading fragile."
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
      kalshi_vol_24h_usd: 10151.0
sources:
  - label: "ClearMarket market record: Nonfarm payrolls, October 2026"
    url: "https://clearmarket.fyi/events/kxpayrolls-26oct"
    retrieved_at: "2026-10-06T14:43:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 83% of lifetime volume appearing in a single session, this contract is essentially brand-new in practice, desks should treat the 70% price as an early-stage signal, not a settled consensus.
