---
signal_id: "CMSIG20260919VS01"
signal_slug: "will-xi-jinping-visit-the-united-states-vol-73790"
headline: "Xi U.S. visit by Oct 1: 94% on $74K inflow"
semantic_title: "Xi U.S. visit before Oct 1 holds at 94% through a volume surge"
telemetry: "94% · $74K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T07:47:59+00:00"
event_id: "CM-EVT-VD0FYJK2D7"
event_slug: "kxxiusa-26jul07"
event_question: "Will Xi Jinping visit the United States?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXXIUSA-26JUL07-OCT01"
  question_raw: "Will Xi Jinping visit the United States of America before Oct 1, 2026?"
  current_price: 0.94
  volume_24h_usd: 73790.11
  volume_cumulative_usd: 285998.63
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-08T14:00:00Z"
bullets:
  - "Kalshi prices 94%, market treating a confirmed visit as all but certain with 12 days remaining."
  - "24h volume of $74K is 26% of all-time, a notable one-day share this close to resolution."
  - "Surge likely reflects late hedging or last-minute position-taking ahead of a scheduled diplomatic event."
  - "Resolves October 1, 2026; cancellation or postponement is the sole remaining downside scenario."
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
      kalshi_vol_24h_usd: 73790.11
sources:
  - label: "ClearMarket market record: Will Xi Jinping visit the United States?"
    url: "https://clearmarket.fyi/events/kxxiusa-26jul07"
    retrieved_at: "2026-09-19T07:47:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 94% print with the clock running out and a fresh volume tranche arriving tells a desk the trip is effectively confirmed in official channels, residual volume is almost entirely risk-management, not discovery.
