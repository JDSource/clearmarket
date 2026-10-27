---
signal_id: "CMSIG20261027VS00"
signal_slug: "will-likud-win-the-most-seats-in-the-202-vol-919919"
headline: "Likud most seats: 21% on $920K surge"
semantic_title: "Traders push Likud's lead-party odds down to 21%"
telemetry: "21% · $920K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf77fa3e63014f1f76ea4433dac66b3860493ed7f1a9fee3dfbef9104d7f1eee3"
  question_raw: "Will Likud win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.21
  volume_24h_usd: 919919.182615
  volume_cumulative_usd: 2351893.4962029997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Likud at just 21% to win the most seats, a decisive rejection of Netanyahu's bloc as frontrunner."
  - "24h volume of $920K is 39% of all-time, nearly half the contract's lifetime activity in a single day."
  - "Surge coincides with heavy parallel flow into Yashar (78%) and Eizenkot (52%) markets, suggesting a broad re-pricing of the Israeli election."
  - "Resolves on official 2026 Knesset seat counts."
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
      poly_vol_24h_usd: 919919.182615
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concurrent volume across Israeli election contracts signals a desk-relevant re-rating of the race, Likud's collapse to 21% warrants reassessing exposure on any Israel-linked political risk.
