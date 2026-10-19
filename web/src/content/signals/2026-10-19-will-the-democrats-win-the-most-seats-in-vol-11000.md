---
signal_id: "CMSIG20261019VS02"
signal_slug: "will-the-democrats-win-the-most-seats-in-vol-11000"
headline: "Israel Dems most seats: 0% on $11K spike"
semantic_title: "Democrats win most seats in Israeli vote: odds at zero"
telemetry: "0% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T07:48:06+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4a48f706471324eb289b2a77a368f7cfc3cdbf899ea320395e9afaa9191570e9"
  question_raw: "Will The Democrats win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.001
  volume_24h_usd: 11000.0
  volume_cumulative_usd: 22930.509563000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices the Israeli Democrats winning the most seats in the 2026 Knesset election at 0%."
  - "$11K traded in 24h represents 48% of all-time contract volume, nearly half the market's lifetime liquidity in one session."
  - "A near-majority of lifetime volume arriving at zero price suggests the contract is approaching formal resolution or final arbitrage."
  - "Resolves on official 2026 Israeli Knesset seat totals; current polling gives the Democrats no plausible path to first place."
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
      poly_vol_24h_usd: 11000.0
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-19T07:48:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concentration of almost half of lifetime volume in a single session at zero odds signals traders closing out positions ahead of a fully anticipated negative resolution.
