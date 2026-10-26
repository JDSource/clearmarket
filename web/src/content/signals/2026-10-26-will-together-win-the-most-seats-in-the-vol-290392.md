---
signal_id: "CMSIG20261026VS01"
signal_slug: "will-together-win-the-most-seats-in-the-vol-290392"
headline: "Together most seats: 0% on $290K Knesset rush"
semantic_title: "Together's Knesset plurality bid trades at zero on record flow"
telemetry: "0% · $290K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.002
  volume_24h_usd: 290392.35944800003
  volume_cumulative_usd: 880533.4323170001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Price at 0%, the market has fully ruled out Together winning the most seats."
  - "33% of all-time volume arrived in 24 hours, an unusually decisive flush."
  - "Flow at a zero-priced contract implies traders closing or arbitraging residual positions."
  - "Resolves on official 2026 Israeli legislative election seat totals."
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
      poly_vol_24h_usd: 290392.35944800003
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 0% contract signals a mass position close or arbitrage clear-out, desks should treat this as a liquidity event rather than a genuine probability debate.
