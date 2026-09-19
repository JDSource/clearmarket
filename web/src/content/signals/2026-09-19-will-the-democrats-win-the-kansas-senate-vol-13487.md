---
signal_id: "CMSIG20260919VS06"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-13487"
headline: "Democrat wins Kansas Senate: 27% on $13K"
semantic_title: "Democrats' long-shot Kansas Senate bid stays under 25%"
telemetry: "27% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.27
  volume_24h_usd: 13487.825084999999
  volume_cumulative_usd: 46047.704725999996
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Democratic Kansas Senate win in 2026 at 27%, solidly minority probability in a deep-red state."
  - "24h volume of $13K is 29% of all-time, a meaningful refresh for a race most write off early."
  - "Fresh interest near 25% suggests a candidate development, filing news, or recruiting story is prompting re-evaluation."
  - "Resolves on 2026 Kansas Senate general election results."
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
      poly_vol_24h_usd: 13487.825084999999
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume returning to a 27% longshot in Kansas signals desks are monitoring for a credible Democratic recruit or Republican vulnerability story that could shift this from novelty to tradeable.
