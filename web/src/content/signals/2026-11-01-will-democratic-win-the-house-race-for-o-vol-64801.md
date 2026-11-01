---
signal_id: "CMSIG20261101VS02"
signal_slug: "will-democratic-win-the-house-race-for-o-vol-64801"
headline: "OH-9 Dem win: 82% on $65K surge"
semantic_title: "Buyers back the Democratic hold in OH-9 at heavy odds"
telemetry: "82% · $65K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-TC43SYMZM4"
event_slug: "houseoh9-26"
event_question: "Will the Republican candidate win the Ohio's 9th congressional district House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEOH9-26-D"
  question_raw: "Will Democratic win the House race for OH-9?"
  current_price: 0.82
  volume_24h_usd: 64801.68
  volume_cumulative_usd: 149967.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 82% on Kalshi, the market prices a solid but not certain Democratic retention of Ohio's 9th district."
  - "$65K in 24h represents 43% of all-time contract volume, a meaningful Election Day compression of activity."
  - "OH-9 has been a targeted Republican pickup; 82% implies the market has not fully dismissed that threat."
  - "Resolves on the certified 2026 OH-9 House race result."
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
      kalshi_vol_24h_usd: 64801.68
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the Ohio's 9th congre"
    url: "https://clearmarket.fyi/events/houseoh9-26"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy Election Day flow at 82%, not 95%+, tells a desk the OH-9 race remains a credible watch item rather than a foregone conclusion.
