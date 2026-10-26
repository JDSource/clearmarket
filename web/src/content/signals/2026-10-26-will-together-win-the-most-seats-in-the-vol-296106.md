---
signal_id: "CMSIG20261026VS01"
signal_slug: "will-together-win-the-most-seats-in-the-vol-296106"
headline: "Together top seat: 0% on $296K inflow"
semantic_title: "Heavy trading tests Together's collapsed odds in Israel's 2026 race"
telemetry: "0% · $296K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.005
  volume_24h_usd: 296106.811836
  volume_cumulative_usd: 776741.1079850001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Market prices Together at effectively 0%, the contract is near-fully discounting the party."
  - "38% of all-time volume arrived in 24 hours, an extraordinary concentration of activity."
  - "Volume at zero odds implies either settlement anticipation or aggressive liquidity-taking against residual bids."
  - "Resolves on certified Israeli legislative seat totals."
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
      poly_vol_24h_usd: 296106.811836
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Massive flow into a near-zero contract suggests traders are either closing positions or forcing a terminal price, a desk should treat this as a near-resolution signal rather than a directional reopen.
