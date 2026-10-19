---
signal_id: "CMSIG20261019VS03"
signal_slug: "will-the-democrats-win-the-most-seats-in-vol-11000"
headline: "Israel Democrats most seats 2026: 0% on $11K spike"
semantic_title: "Fresh volume returns to Democrats leading the 2026 Knesset race"
telemetry: "0% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T15:15:12+00:00"
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
  - "Price at 0% reflects market consensus that the Israeli Democrats will not finish first in seat count in 2026."
  - "Today's $11K represents 48% of all-time volume, nearly half of all trading occurred in this single session."
  - "A nearly 50% single-day concentration is a strong signal that a discrete news event triggered final position closing."
  - "Contract resolves on the official 2026 Israeli legislative election seat totals."
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
    retrieved_at: "2026-10-19T15:15:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume printing in one day on a zero-priced contract strongly implies a definitive political development, such as a polling collapse or coalition announcement, has prompted traders to close the book on this scenario.
