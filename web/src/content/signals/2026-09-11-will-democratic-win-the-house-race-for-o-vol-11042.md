---
signal_id: "CMSIG20260911VS03"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-11042"
headline: "Democrat OH-9 House: 71% on $11K surge"
semantic_title: "Democrats lead the OH-9 House race at 71%"
telemetry: "71% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-11T12:33:13+00:00"
event_id: "CM-EVT-TC43SYMZM4"
event_slug: "houseoh9-26"
event_question: "Will the Republican candidate win the Ohio's 9th congressional district House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEOH9-26-D"
  question_raw: "Will Democratic win the House race for OH-9?"
  current_price: 0.71
  volume_24h_usd: 11042.63
  volume_cumulative_usd: 16445.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 71% in OH-9, a clear lean that implies the seat is competitive but tilted blue."
  - "67% of all-time volume arrived in a single 24h window, the most concentrated activity this contract has seen."
  - "A volume burst of this proportion in a down-ballot race typically precedes or follows a local poll, candidate news, or early-vote data drop."
  - "Contract resolves on the OH-9 general election result."
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
      kalshi_vol_24h_usd: 11042.63
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the Ohio's 9th congre"
    url: "https://clearmarket.fyi/events/houseoh9-26"
    retrieved_at: "2026-09-11T12:33:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of all-time volume in one day in a single House race is an outsized signal, desks tracking House majority math should flag OH-9 as a newly watched seat where local information may have moved before it hit national outlets.
