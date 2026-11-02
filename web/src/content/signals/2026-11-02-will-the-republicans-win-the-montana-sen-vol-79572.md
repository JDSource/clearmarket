---
signal_id: "CMSIG20261102VS07"
signal_slug: "will-the-republicans-win-the-montana-sen-vol-79572"
headline: "Montana Senate GOP: 91% on $80K volume surge"
semantic_title: "Montana GOP Senate odds stay near the top on fresh volume"
telemetry: "91% · $80K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-QLN52WYLT6"
event_slug: "montana-senate-election-winner"
event_question: "Montana Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd103195d48bf6183e28c4140bd374dd3e907e8f8d411374cb4d2d124ec4c216d"
  question_raw: "Will the Republicans win the Montana Senate race in 2026?"
  current_price: 0.91
  volume_24h_usd: 79572.006104
  volume_cumulative_usd: 316174.0584049999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 91% in Montana, the market has priced this as a near-certain GOP hold or pickup."
  - "24h volume of $80K equals 25% of all-time flow, consistent with a midterm-eve repricing wave across Senate contracts."
  - "Montana's partisan shift toward Republicans in recent cycles makes 91% reflect both polling and structural fundamentals."
  - "Resolves on the 2026 Montana Senate general election result."
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
      poly_vol_24h_usd: 79572.006104
sources:
  - label: "ClearMarket market record: Montana Senate Election Winner"
    url: "https://clearmarket.fyi/events/montana-senate-election-winner"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-confidence volume at 91% in Montana indicates desks are finalizing Senate map totals and treating this seat as a reliable GOP column in seat-count modeling.
