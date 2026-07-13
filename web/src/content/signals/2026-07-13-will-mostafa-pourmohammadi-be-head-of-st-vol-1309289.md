---
signal_id: "CMSIG20260713VS00"
signal_slug: "will-mostafa-pourmohammadi-be-head-of-st-vol-1309289"
headline: "Pourmohammadi Iran head of state: 0% on $1.3M surge"
semantic_title: "Traders write off Pourmohammadi as Iran head of state by year-end"
telemetry: "0% · $1.3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-13T10:56:44+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaa53ce562be767321e2f0cba9f7b3207fde7d2204dbb7f9b5d804996eba7de7c"
  question_raw: "Will Mostafa Pourmohammadi be head of state in Iran end of 2026?"
  current_price: 0.002
  volume_24h_usd: 1309289.132999999
  volume_cumulative_usd: 3318339.448454994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability Pourmohammadi leads Iran by end of 2026."
  - "24h volume $1.3M represents 39% of all-time handle, exceptional single-session conviction."
  - "Surge likely follows confirmation or credible reporting that Pourmohammadi is decisively out of contention."
  - "Contract resolves end of 2026; capital is firmly stacking the 'No' side."
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
      poly_vol_24h_usd: 1309289.132999999
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-13T10:56:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The overwhelming one-sided flow at zero price signals desks are treating this as a near-certain resolution event, likely catalyzed by a concrete political development in Iran this week.
