---
signal_id: "CMSIG20261004VS05"
signal_slug: "will-fl-vio-bolsonaro-win-the-first-roun-vol-42245"
headline: "F. Bolsonaro outright win: 36% on $42K flow"
semantic_title: "Traders back Flávio Bolsonaro first-round win at 36%"
telemetry: "36% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x25966b196ffc1682fc77df0298784831a60aea8abe03b9aa4fc219d1422feb9f"
  question_raw: "Will Flávio Bolsonaro win the first round of the 2026 Brazilian presidential election by less than 5%?"
  current_price: 0.36
  volume_24h_usd: 42245.28623600001
  volume_cumulative_usd: 138900.076077
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Flávio Bolsonaro winning the first round outright at 36%, a material but not dominant probability."
  - "$42,245 in 24h represents 30% of all-time volume, showing sustained conviction on this specific outcome."
  - "36% for a first-round majority reflects optimism among the Bolsonaro camp but acknowledges Lula's competitive base."
  - "Resolves YES only if Bolsonaro surpasses 50% of valid first-round votes."
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
      poly_vol_24h_usd: 42245.28623600001
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 36% first-round outright price with fresh volume suggests some traders are positioning for a scenario where Lula's coalition fragments, desks should monitor Brazilian right-wing consolidation signals.
