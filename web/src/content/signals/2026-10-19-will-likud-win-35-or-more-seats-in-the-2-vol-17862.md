---
signal_id: "CMSIG20261019VS02"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-17862"
headline: "Likud 35+ seats 2026: 1% on $18K Polymarket spike"
semantic_title: "Heavy trading tests Likud's 35-seat threshold at long-shot odds"
telemetry: "1% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T15:15:12+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.008
  volume_24h_usd: 17862.894867
  volume_cumulative_usd: 48932.099807000006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "At 1%, the market prices Likud winning 35 or more seats in the 2026 Israeli election as a near-impossibility."
  - "Today's $18K is 37% of all-time volume, more than a third of all trading concentrated in one session."
  - "Fresh attention at this price may follow Israeli polling data or a party realignment story entering the news cycle."
  - "Contract resolves on official 2026 Knesset seat allocation for Likud."
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
      poly_vol_24h_usd: 17862.894867
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-19T15:15:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 37% single-day share of all-time volume on a 1% contract points to a specific news catalyst prompting traders to either take or close a speculative position on a Likud surge.
