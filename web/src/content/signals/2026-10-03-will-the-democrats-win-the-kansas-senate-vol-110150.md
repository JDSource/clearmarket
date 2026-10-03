---
signal_id: "CMSIG20261003VS01"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-110150"
headline: "Kansas Senate Dems: 38% on $110K inflow"
semantic_title: "Democrats pick up backing in Kansas Senate at 38%"
telemetry: "38% · $110K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.38
  volume_24h_usd: 110150.586666
  volume_cumulative_usd: 309612.805966
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 38%, an underdog read, but well above a longshot."
  - "36% of all-time volume printed in 24 hours, the highest all-time share across the Kansas pair."
  - "Coordinated surge alongside the GOP contract (Spike 0) implies new information or polling is driving two-sided re-pricing."
  - "Resolves on the 2026 Kansas Senate general election result."
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
      poly_vol_24h_usd: 110150.586666
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 38% Democratic price in Kansas combined with a 36% all-time volume share suggests a genuine competitiveness signal, desks should watch for polling or candidate news that prompted this unusual activity.
