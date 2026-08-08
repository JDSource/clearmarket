---
signal_id: "CMSIG20260808VS04"
signal_slug: "will-bill-cassidy-vote-for-todd-blanche-vol-26556"
headline: "Cassidy votes Blanche: 99% on $27K surge"
semantic_title: "Betting piles into Cassidy voting yes on Todd Blanche"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-J66NJ3ZHH7"
event_slug: "kxvoteblanche-27"
event_question: "Will Todd Blanche receive votes from specific Senators?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEBLANCHE-27-BCAS"
  question_raw: "Will Bill Cassidy vote for Todd Blanche?"
  current_price: 0.99
  volume_24h_usd: 26556.38
  volume_cumulative_usd: 47850.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices Cassidy voting for Todd Blanche at 99%, near-unanimous market conviction."
  - "24h volume of $27K is 55% of all-time, meaning more than half of lifetime activity hit in one day."
  - "The concentrated single-day volume spike suggests a news catalyst, likely a public statement or vote signal."
  - "Resolves on the recorded Senate confirmation vote."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 26556.38
sources:
  - label: "ClearMarket market record: Will Todd Blanche receive votes from specific Senators?"
    url: "https://clearmarket.fyi/events/kxvoteblanche-27"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Over half of all-time volume printing in 24 hours at 99% tells a desk that a Cassidy commitment has likely been confirmed publicly and the market is closing out the residual risk.
