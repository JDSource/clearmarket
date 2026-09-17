---
signal_id: "CMSIG20260917VS00"
signal_slug: "will-trump-publicly-criticize-kevin-wars-vol-146530"
headline: "Trump vs. Warsh criticism: 48% on $147K surge"
semantic_title: "Trump-Warsh public rift stays a coin-flip before Jan 2027"
telemetry: "48% · $147K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-P95C3C1H51"
event_slug: "kxdjtattackwarsh-27"
event_question: "Will Trump publicly criticize Kevin Warsh?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDJTATTACKWARSH-27-JAN"
  question_raw: "Will Trump publicly criticize Kevin Warsh before Jan 2027?"
  current_price: 0.48
  volume_24h_usd: 146530.69
  volume_cumulative_usd: 192344.33
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Market prices a near-even 48% chance Trump publicly attacks Warsh before year-end."
  - "$147K traded in 24h, 76% of all-time volume, signaling a major fresh-attention event."
  - "Warsh is a leading Fed chair contender; any Trump policy frustration could trigger public friction."
  - "Resolves by Jan 1, 2027, tight window concentrates risk."
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
      kalshi_vol_24h_usd: 146530.69
sources:
  - label: "ClearMarket market record: Will Trump publicly criticize Kevin Warsh?"
    url: "https://clearmarket.fyi/events/kxdjtattackwarsh-27"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds combined with a dominant all-time volume share suggest desks are positioning around an imminent Warsh Fed-nomination-related development or Trump public statement.
