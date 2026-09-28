---
signal_id: "CMSIG20260928VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-45735"
headline: "Fed July 2027 hold: 84% on $45K late push"
semantic_title: "Fed pause bets hold firm through a volume surge"
telemetry: "84% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-28T16:24:28+00:00"
event_id: "CM-EVT-S64CMSWWK9"
event_slug: "kxfeddecision-27jul"
event_question: "Will the Federal Reserve make a decision in July 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-27JUL-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their July 2027 meeting?"
  current_price: 0.84
  volume_24h_usd: 45735.25
  volume_cumulative_usd: 52548.94
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-07-28T18:05:00Z"
bullets:
  - "Kalshi prices an 0bps July 2027 Fed hold at 84%, market treats a pause as the strong base case."
  - "$45K in 24h volume equals 87% of all-time flow, signaling near-exhaustive positioning in a single session."
  - "Surge arrives as rate-path debates sharpen into 2027; heavy one-sided flow suggests traders are locking in conviction rather than hedging."
  - "Resolves at the July 2027 FOMC decision."
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
      kalshi_vol_24h_usd: 45735.25
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in July 2027?"
    url: "https://clearmarket.fyi/events/kxfeddecision-27jul"
    retrieved_at: "2026-09-28T16:24:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that 87% of lifetime volume printing in one session on an 84% hold price reflects strong directional conviction on a Fed pause, any hawkish datapoint before July 2027 would reprice this contract sharply.
