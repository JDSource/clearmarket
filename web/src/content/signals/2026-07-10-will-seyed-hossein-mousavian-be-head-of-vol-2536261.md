---
signal_id: "CMSIG20260710VS00"
signal_slug: "will-seyed-hossein-mousavian-be-head-of-vol-2536261"
headline: "Mousavian Iran head of state: 0% on $2.5M surge"
semantic_title: "Traders write off Mousavian as Iran's next head of state"
telemetry: "0% · $2.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x821f357da390a32347e4df0c3fb0aa4a8eadf4af72730c8dc7a7f1ab58798a02"
  question_raw: "Will Seyed Hossein Mousavian be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 2536261.383333
  volume_cumulative_usd: 3647904.711215
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices Mousavian at 0%, capital unanimously rules out his ascent by end-2026."
  - "24h volume $2.54M equals 70% of all-time handle, signaling an extraordinary single-session conviction flush."
  - "Surge likely follows a succession or political development in Iran drawing fresh attention to realistic candidate set."
  - "Resolves end of 2026; current price leaves no residual probability for any surprise Mousavian scenario."
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
      poly_vol_24h_usd: 2536261.383333
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total all-time volume print at 0% indicates desks are definitively closing out any tail exposure on Mousavian, likely in response to a clarifying Iran political event.
