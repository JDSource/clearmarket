---
signal_id: "CMSIG20261031VS02"
signal_slug: "will-the-democrats-win-the-michigan-sena-vol-768993"
headline: "Michigan Senate Dems: 80% on $769K Polymarket flow"
semantic_title: "Democratic Michigan Senate odds stay near 80% under surge"
telemetry: "80% · $769K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-P8B8CLLCB5"
event_slug: "michigan-senate-election-winner"
event_question: "Will a Michigan Senate election winner be determined by the next election cycle?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbfeb6d4cf3eab6071e204219b0647c8224d63a12778df467311b5f2a4b3a5bd4"
  question_raw: "Will the Democrats win the Michigan Senate race in 2026?"
  current_price: 0.8
  volume_24h_usd: 768993.4363260001
  volume_cumulative_usd: 2753961.856707
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket marks Democratic Michigan Senate win at 80%, a heavy favorite read."
  - "$769K traded in 24h, 28% of all-time volume, running in lockstep with the GOP leg."
  - "Matching volume across both legs points to new entrants picking sides, not just arbitrage."
  - "Resolves on Michigan 2026 Senate result; late polling or endorsement news could shift the line."
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
      poly_vol_24h_usd: 768993.4363260001
sources:
  - label: "ClearMarket market record: Will a Michigan Senate election winner be determined by"
    url: "https://clearmarket.fyi/events/michigan-senate-election-winner"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 80% price holding while nearly a third of all-time volume prints suggests the line is absorbing fresh conviction on the Democratic side, a desk should watch for any late catalyst that could compress this spread.
