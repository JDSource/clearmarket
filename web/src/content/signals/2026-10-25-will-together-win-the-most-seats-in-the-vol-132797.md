---
signal_id: "CMSIG20261025VS01"
signal_slug: "will-together-win-the-most-seats-in-the-vol-132797"
headline: "Together wins most Knesset seats: 1% on $132K"
semantic_title: "Together party stays a heavy underdog despite fresh Israeli election volume"
telemetry: "1% · $133K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T07:48:52+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4e9cff8a3aeac036225fedcc98af9b0d55284b3f430b599e7f61b059c1e177af"
  question_raw: "Will Together win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.014
  volume_24h_usd: 132797.819267
  volume_cumulative_usd: 495694.68614899996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket holds Together's odds at 1%, near-zero probability of topping the 2026 Israeli legislative seat count."
  - "24h volume of $132K represents 27% of all-time handle, indicating a notable but not dominant attention spike."
  - "Fresh volume may reflect positioning ahead of polling updates or coalition realignment news in Israeli political coverage."
  - "Contract resolves on official Knesset seat tallies from the 2026 Israeli legislative election."
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
      poly_vol_24h_usd: 132797.819267
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-25T07:48:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 1% price with meaningful inflow suggests traders are either stress-testing the floor or hedging against a low-probability coalition upset; desks should treat this as a tail-risk signal on Israeli political stability rather than a directional view.
