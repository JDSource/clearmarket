---
signal_id: "CMSIG20261020VS06"
signal_slug: "will-the-republican-party-win-the-tx-04-vol-12936"
headline: "GOP wins TX-04 House seat: 96% on $13K surge"
semantic_title: "Republicans hold TX-04 at 96% odds through a volume surge"
telemetry: "96% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T13:16:06+00:00"
event_id: "CM-EVT-1P68WDW7C0"
event_slug: "tx-04-house-election-winner"
event_question: "TX-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa59f274d0f22e979d42de45c512fc1065f0672221f28d0f0e715fe208f7404bd"
  question_raw: "Will the Republican Party win the TX-04 House seat?"
  current_price: 0.965
  volume_24h_usd: 12936.023369
  volume_cumulative_usd: 34788.228179
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Market prices a 96% chance Republicans retain TX-04, effectively a locked outcome with minimal upset risk."
  - "24h volume of $13K is 37% of all-time handle, suggesting a round of final positioning as the race approaches resolution."
  - "TX-04 is a deeply Republican district; volume surge likely reflects traders closing out or establishing end-of-cycle positions."
  - "Resolves at the TX-04 election result; 4% residual reflects standard tail-risk rather than any genuine competitive signal."
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
      poly_vol_24h_usd: 12936.023369
sources:
  - label: "ClearMarket market record: TX-04 House Election Winner"
    url: "https://clearmarket.fyi/events/tx-04-house-election-winner"
    retrieved_at: "2026-10-20T13:16:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certainty pricing with a meaningful volume burst is consistent with position cleanup ahead of resolution, no competitive signal here, but the contract can serve as a benchmark for House majority seat-count models.
