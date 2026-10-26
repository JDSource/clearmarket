---
signal_id: "CMSIG20261026VS00"
signal_slug: "will-likud-win-the-most-seats-in-the-202-vol-418111"
headline: "Likud top seat: 27% on $418K volume surge"
semantic_title: "Traders pile into Likud leading Israel's 2026 vote at long-shot odds"
telemetry: "27% · $418K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf77fa3e63014f1f76ea4433dac66b3860493ed7f1a9fee3dfbef9104d7f1eee3"
  question_raw: "Will Likud win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.27
  volume_24h_usd: 418111.0894999999
  volume_cumulative_usd: 1338513.9389439998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Market prices Likud at 27%, a clear underdog to lead the 2026 Knesset."
  - "24h volume of $418K represents 31% of all-time flow, a sharp single-session spike."
  - "Heavy fresh activity suggests traders are re-evaluating coalition dynamics ahead of the election."
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
      poly_vol_24h_usd: 418111.0894999999
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The surge in fresh capital at a 27% price signals active disagreement on Likud's electoral ceiling, a desk should watch for polling or coalition news driving the two-sided flow.
