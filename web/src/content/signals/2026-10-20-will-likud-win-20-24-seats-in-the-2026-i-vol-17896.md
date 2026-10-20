---
signal_id: "CMSIG20261020VS05"
signal_slug: "will-likud-win-20-24-seats-in-the-2026-i-vol-17896"
headline: "Likud 20-24 seats 2026 election: 37% on $18K surge"
semantic_title: "Fresh volume returns to Likud landing in the 20-24 seat range"
telemetry: "37% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T13:16:06+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3135bdbe2e03604ff34296d209bccf73d7e90b47f634bf47becffaad852c064d"
  question_raw: "Will Likud win 20-24 seats in the 2026 Israeli legislative election?"
  current_price: 0.37
  volume_24h_usd: 17896.356476999998
  volume_cumulative_usd: 58338.221477
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "At 37%, the 20-24 seat bracket is the single most credible Likud outcome range the market is currently pricing."
  - "24h volume of $18K equals 31% of all-time handle, and should be read alongside the concurrent 0% price on the 35+ bracket."
  - "Capital rotating out of higher seat-count brackets is likely landing here as polling narrows the expected Likud result."
  - "Resolves at the 2026 Israeli election; 37% makes this a contested outcome, not a consensus call."
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
      poly_vol_24h_usd: 17896.356476999998
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-20T13:16:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Read together with the 35+ bracket going to zero, fresh volume here suggests the market is actively redistribution Likud seat expectations into a tighter, lower range, a useful input for Israeli political-risk analysis.
