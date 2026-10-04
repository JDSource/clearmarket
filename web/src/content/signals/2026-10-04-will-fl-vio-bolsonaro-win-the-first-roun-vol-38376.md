---
signal_id: "CMSIG20261004VS07"
signal_slug: "will-fl-vio-bolsonaro-win-the-first-roun-vol-38376"
headline: "Flávio Bolsonaro 1st round alt: 3% on $38K"
semantic_title: "Separate Flávio Bolsonaro first-round contract slips to 3%"
telemetry: "3% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3a539f4052dc3340948b9f56119fbee92919f7bf9bb3cc73fd7feeb310d030d4"
  question_raw: "Will Flávio Bolsonaro win the first round of the 2026 Brazilian presidential election by 5–10%?"
  current_price: 0.029
  volume_24h_usd: 38376.19331400001
  volume_cumulative_usd: 118160.32114700001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "A second Polymarket contract on Flávio Bolsonaro winning round one prices it at just 3%, near-impossible."
  - "32% of all-time volume transacted in 24h on this near-zero contract."
  - "The 32-point gap versus Spike 6 again points to differing resolution thresholds or candidate scope across contracts."
  - "Resolves on Brazil's official 2026 first-round election results."
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
      poly_vol_24h_usd: 38376.19331400001
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two contracts on the same candidate with a 32-point pricing gap demand a desk review the resolution rules, one likely covers a stricter threshold or different candidate grouping, and the spread could be actionable.
