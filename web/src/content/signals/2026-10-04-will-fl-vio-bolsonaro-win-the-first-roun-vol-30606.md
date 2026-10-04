---
signal_id: "CMSIG20261004VS07"
signal_slug: "will-fl-vio-bolsonaro-win-the-first-roun-vol-30606"
headline: "F. Bolsonaro outright win: 0% on $31K flow"
semantic_title: "Bolsonaro first-round win effectively dead money at 0%"
telemetry: "0% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x277dfee905afb258ea2a73842a7ea9a8cba4e3d52597d33f69bc7d159c52f3da"
  question_raw: "Will Flávio Bolsonaro win the first round of the 2026 Brazilian presidential election by at least 10%?"
  current_price: 0.002
  volume_24h_usd: 30606.308929
  volume_cumulative_usd: 79593.84453900001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices this Flávio Bolsonaro first-round majority contract at 0%, with the market deeming it impossible under current resolution terms."
  - "$30,606 in 24h is 38% of all-time volume, striking activity for a zero-priced contract."
  - "Volume at 0% almost certainly reflects final position settlement, contract clarification trading, or eligibility-related resolution approaching."
  - "Resolves YES only on a first-round outright majority, an outcome the market has fully dismissed."
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
      poly_vol_24h_usd: 30606.308929
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Non-trivial volume on a zero-priced contract is an operational signal, not a directional one, desks should confirm whether this contract is approaching forced resolution or has a spec change pending.
