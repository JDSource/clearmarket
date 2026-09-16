---
signal_id: "CMSIG20260916VS07"
signal_slug: "will-republicans-win-the-senate-race-in-vol-18171"
headline: "NH Senate GOP win: 19% on $18K volume surge"
semantic_title: "Republicans face long odds in New Hampshire Senate race at 19%"
telemetry: "19% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-NF2DF1TXH9"
event_slug: "senatenh-26"
event_question: "New Hampshire Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENH-26-R"
  question_raw: "Will Republicans win the Senate race in New Hampshire?"
  current_price: 0.19
  volume_24h_usd: 18171.83
  volume_cumulative_usd: 72648.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Senate win in New Hampshire at 19%, the mirror of the 82% Democratic contract."
  - "25% of all-time volume, $18.2K, hit in 24h, directly correlated with the larger Democratic-side spike."
  - "Simultaneous volume on both sides of the NH Senate market points to two-sided positioning, not one-directional conviction."
  - "The 19% Republican price represents the hedge and tail-risk entry point as the midterm cycle heats up."
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
      kalshi_vol_24h_usd: 18171.83
sources:
  - label: "ClearMarket market record: New Hampshire Senate winner?"
    url: "https://clearmarket.fyi/events/senatenh-26"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concurrent volume surges on both the Democratic and Republican NH Senate contracts indicate active two-sided positioning, desks should read the combined flow as a liquidity event rather than a directional signal.
