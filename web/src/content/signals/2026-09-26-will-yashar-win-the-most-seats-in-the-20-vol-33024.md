---
signal_id: "CMSIG20260926VS01"
signal_slug: "will-yashar-win-the-most-seats-in-the-20-vol-33024"
headline: "Yashar Israel seats lead: 59% on $33K surge"
semantic_title: "Yashar Israeli election odds hold at 59% through heavy trading"
telemetry: "59% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T07:47:58+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd05da9807740aa0f5bc9e9232daabe87a21e5012c19e283abf414f1c1651118b"
  question_raw: "Will Yashar win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.59
  volume_24h_usd: 33024.440638
  volume_cumulative_usd: 125888.935527
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "59% on Polymarket puts Yashar as the narrow but meaningful favorite for most Knesset seats in 2026."
  - "24h volume of $33K is 26% of all-time, a meaningful single-day share for an international legislative race."
  - "Renewed trading attention typically precedes a polling release, coalition shift, or campaign event in Israel."
  - "Resolves on final certified seat counts from the 2026 Israeli legislative election."
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
      poly_vol_24h_usd: 33024.440638
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-09-26T07:47:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-coin-flip priced contract drawing a quarter of its lifetime volume in one session signals active disagreement, a desk should watch for new Israeli polling or coalition news that could swing the line.
