---
signal_id: "CMSIG20261027VS06"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-117652"
headline: "Likud 35+ seats: 2% on $118K volume"
semantic_title: "Traders virtually rule out Likud at 35-plus seats"
telemetry: "2% · $118K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.025
  volume_24h_usd: 117652.21311599998
  volume_cumulative_usd: 244976.64799099998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Likud winning 35 or more seats at 2%, a near-total dismissal of a strong Likud performance."
  - "24h volume of $118K is 48% of all-time, meaning nearly half the contract's activity has arrived today."
  - "At 2%, this functions as a tail-risk contract; volume here may reflect cheap hedges against a surprise Likud surge."
  - "Resolves on official 2026 Knesset seat count for Likud."
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
      poly_vol_24h_usd: 117652.21311599998
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 35+ seat contract pricing at 2% with half its lifetime volume today confirms the market's strong directional view on Likud's decline, useful as a cheap hedge leg for any desk running Israeli scenario analysis.
