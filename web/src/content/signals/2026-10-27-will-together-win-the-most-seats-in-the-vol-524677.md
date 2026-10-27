---
signal_id: "CMSIG20261027VS02"
signal_slug: "will-together-win-the-most-seats-in-the-vol-524677"
headline: "Together most seats: 0% on $525K inflow"
semantic_title: "Together party's lead-seat bid effectively ruled out at 0%"
telemetry: "0% · $525K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.003
  volume_24h_usd: 524677.5592119999
  volume_cumulative_usd: 1376775.760816
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Together at 0% to win the most Knesset seats, the market has fully closed out this outcome."
  - "24h volume of $525K is 38% of all-time, an unusually large flush on a contract already priced at the floor."
  - "Volume at zero price typically reflects final settlement positioning or late arbitrage cleanup ahead of resolution."
  - "Resolves on official 2026 Israeli legislative seat counts."
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
      poly_vol_24h_usd: 524677.5592119999
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 0% contract is a resolution-mechanics signal, desks should note this as likely cleanup flow rather than a genuine directional trade.
