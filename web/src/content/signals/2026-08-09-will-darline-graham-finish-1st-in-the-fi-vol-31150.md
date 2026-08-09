---
signal_id: "CMSIG20260809VS04"
signal_slug: "will-darline-graham-finish-1st-in-the-fi-vol-31150"
headline: "Graham SC Rep round 1: 62% on $31K inflow"
semantic_title: "Darline Graham leads SC-Rep first round at 62%"
telemetry: "62% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-34WPGXDWQ8"
event_slug: "kxprimaryplace-scrsens26-1"
event_question: "Will the candidate receiving the most votes win first place in the first round of the South Carolina Republican Senate special primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SCRSENS26-1-DGRA"
  question_raw: "Will Darline Graham finish 1st in the first round of the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.62
  volume_24h_usd: 31150.9
  volume_cumulative_usd: 67864.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Kalshi prices Darline Graham finishing first in the South Carolina Republican primary's first round at 62%, a meaningful but not commanding lead."
  - "24h volume of $31K is 46% of all-time handle, reflecting a sharp spike in primary-race attention."
  - "A 62% reading implies live uncertainty, a split field or late entrant could shift the calculus before election day."
  - "Contract resolves on the certified first-round result of the South Carolina Republican primary."
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
      kalshi_vol_24h_usd: 31150.9
sources:
  - label: "ClearMarket market record: Will the candidate receiving the most votes win first p"
    url: "https://clearmarket.fyi/events/kxprimaryplace-scrsens26-1"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering at a 62% price in a down-ballot primary tells a desk that this race has attracted meaningful capital on Graham's lead, worth flagging as a contested outcome with non-trivial upset risk.
