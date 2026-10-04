---
signal_id: "CMSIG20261004VS06"
signal_slug: "will-fl-vio-bolsonaro-win-the-first-roun-vol-38823"
headline: "F. Bolsonaro outright win: 3% on $39K spike"
semantic_title: "Flávio Bolsonaro first-round win holds near zero at 3%"
telemetry: "3% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3a539f4052dc3340948b9f56119fbee92919f7bf9bb3cc73fd7feeb310d030d4"
  question_raw: "Will Flávio Bolsonaro win the first round of the 2026 Brazilian presidential election by 5–10%?"
  current_price: 0.034
  volume_24h_usd: 38823.015009000024
  volume_cumulative_usd: 119936.242842
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "This Polymarket contract prices a Flávio Bolsonaro first-round majority at 3%, near-zero probability, effectively ruling it out."
  - "$38,823 in 24h is 32% of all-time volume, a heavy flush despite the near-zero price."
  - "High volume on a nearly-dead contract typically signals traders locking in final short positions or closing residual exposure."
  - "The 3% vs. 36% spread across concurrent Polymarket contracts again flags differing resolution specs, verification is essential."
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
      poly_vol_24h_usd: 38823.015009000024
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume on a 3%-priced contract usually means professional clearing of residual positions, desks should treat this as a signal that sophisticated participants are finalizing a view rather than opening new directional bets.
