---
signal_id: "CMSIG20261103VS00"
signal_slug: "will-the-republican-party-win-the-govern-vol-1493796"
headline: "Florida GOP governor: 62% on $1.5M surge"
semantic_title: "Florida governor stays a Republican hold at 62%"
telemetry: "62% · $1.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T07:49:22+00:00"
event_id: "CM-EVT-4HX1NKV2L1"
event_slug: "govpartyfl-26"
event_question: "Florida Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYFL-26-R"
  question_raw: "Will the Republican party win the governorship in Florida"
  current_price: 0.62
  volume_24h_usd: 1493796.01
  volume_cumulative_usd: 5013339.03
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices Republican retention at 62%, a solid but not certain hold."
  - "24h volume of $1.5M is 30% of all-time, the single largest single-day draw on this contract."
  - "Election Day activity on 2026 midterm ballots driving concentrated end-of-line positioning."
  - "Resolves on certified Florida gubernatorial results."
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
      kalshi_vol_24h_usd: 1493796.01
sources:
  - label: "ClearMarket market record: Florida Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyfl-26"
    retrieved_at: "2026-11-03T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy terminal-day volume at a 62% hold price signals desks are treating Florida as a live contest requiring active hedging rather than a foregone conclusion.
