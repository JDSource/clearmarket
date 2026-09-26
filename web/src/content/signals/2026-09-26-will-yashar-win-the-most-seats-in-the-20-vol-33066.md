---
signal_id: "CMSIG20260926VS01"
signal_slug: "will-yashar-win-the-most-seats-in-the-20-vol-33066"
headline: "Yashar most Knesset seats: 59% on $33K surge"
semantic_title: "Yashar leads Israeli Knesset race as volume picks up"
telemetry: "59% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd05da9807740aa0f5bc9e9232daabe87a21e5012c19e283abf414f1c1651118b"
  question_raw: "Will Yashar win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.59
  volume_24h_usd: 33066.813519999996
  volume_cumulative_usd: 125931.30840899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Yashar at 59%, a slim majority-conviction edge over rivals in the 2026 Israeli legislative election."
  - "$33.1K in 24h volume equals 26% of all-time, reflecting a meaningful re-engagement with this contract."
  - "Israeli coalition politics remain fluid; fresh volume near 60% suggests the market is digesting recent polling or coalition signals."
  - "Contract resolves on official seat counts following the next Knesset election."
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
      poly_vol_24h_usd: 33066.813519999996
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering just below a two-thirds threshold on a contested multi-party race tells desks that conviction is growing but not decisive, monitor Israeli coalition news for the catalyst.
