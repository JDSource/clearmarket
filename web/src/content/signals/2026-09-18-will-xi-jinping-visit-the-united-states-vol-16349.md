---
signal_id: "CMSIG20260918VS06"
signal_slug: "will-xi-jinping-visit-the-united-states-vol-16349"
headline: "Xi US visit by Nov 1: 96% on $16K surge"
semantic_title: "Xi US visit before Nov 1 trades near certainty on fresh volume"
telemetry: "96% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-VD0FYJK2D7"
event_slug: "kxxiusa-26jul07"
event_question: "Will Xi Jinping visit the United States?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXXIUSA-26JUL07-NOV01"
  question_raw: "Will Xi Jinping visit the United States of America before Nov 1, 2026?"
  current_price: 0.96
  volume_24h_usd: 16349.88
  volume_cumulative_usd: 38431.5
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-08T15:00:00Z"
bullets:
  - "96% price signals the market treats a Xi visit to the US before November 1, 2026 as nearly confirmed."
  - "43% of all-time volume in 24 hours implies a concrete scheduling development or official confirmation is circulating."
  - "At this price, remaining volume likely represents final settlement positioning rather than directional trade."
  - "Resolves if Xi Jinping sets foot on US soil before November 1, 2026."
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
      kalshi_vol_24h_usd: 16349.88
sources:
  - label: "ClearMarket market record: Will Xi Jinping visit the United States?"
    url: "https://clearmarket.fyi/events/kxxiusa-26jul07"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 96% print consuming 43% of lifetime volume tells a desk the geopolitical event is effectively scheduled and attention should shift to agenda and bilateral outcome monitoring.
