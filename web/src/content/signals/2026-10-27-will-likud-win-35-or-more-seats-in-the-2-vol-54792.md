---
signal_id: "CMSIG20261027VS07"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-54792"
headline: "Likud 35+ seats: 2% on $55K volume"
semantic_title: "Likud hitting 35 seats seen as near-impossible at 2%"
telemetry: "2% · $55K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.017
  volume_24h_usd: 54792.40717499999
  volume_cumulative_usd: 172310.161438
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "2% price means the market has all but eliminated the scenario of Likud capturing 35 or more Knesset seats in 2026."
  - "$55K in 24h is 32% of all-time volume, notable activity for a contract sitting at the probability floor."
  - "Paired with the 30%-priced Likud plurality contract, traders see Likud as a competitive force but far short of a dominant showing."
  - "Resolves on official Knesset seat tallies following the 2026 Israeli legislative election."
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
      poly_vol_24h_usd: 54792.40717499999
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume into a 2%-priced contract alongside its companion plurality contract confirms traders are building a nuanced Israeli election book, desks should read this as a ceiling trade, capping Likud's upside scenario.
