---
signal_id: "CMSIG20260813VS02"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-82623"
headline: "TX-15 Dem win: 45% on $83K volume spike"
semantic_title: "TX-15 House seat draws buyers below 50% on the Dem side"
telemetry: "45% · $83K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-F1CD0HM6W4"
event_slug: "housetx15-26"
event_question: "TX-15 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX15-26-D"
  question_raw: "Will Democratic win the House race for TX-15?"
  current_price: 0.45
  volume_24h_usd: 82623.95
  volume_cumulative_usd: 176146.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic TX-15 House win at 45%, Republicans hold a slim implied edge."
  - "47% of all-time contract volume hit in a single session, the largest single-day share of this batch."
  - "A near-even price with surging volume signals late-entry attention to a district shifting competitive."
  - "Resolves on the TX-15 2026 House general election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 82623.95
sources:
  - label: "ClearMarket market record: TX-15 House winner?"
    url: "https://clearmarket.fyi/events/housetx15-26"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of lifetime volume arriving at a sub-50% Democratic price suggests fresh money is stress-testing the Republican lean in TX-15, a district worth flagging in House-majority seat counts.
