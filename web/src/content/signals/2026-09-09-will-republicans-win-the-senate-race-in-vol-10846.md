---
signal_id: "CMSIG20260909VS07"
signal_slug: "will-republicans-win-the-senate-race-in-vol-10846"
headline: "SD Senate Republican: 95% on $11K fresh volume"
semantic_title: "South Dakota Senate stays deep red at 95%"
telemetry: "95% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-NVM4YFPJH3"
event_slug: "senatesd-26"
event_question: "Will the winner of the South Dakota Senate election be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATESD-26-R"
  question_raw: "Will Republicans win the Senate race in South Dakota?"
  current_price: 0.954
  volume_24h_usd: 10846.37
  volume_cumulative_usd: 30695.13
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Senate win in South Dakota at 95%, a near-foregone conclusion."
  - "35% of all-time volume cleared in 24h, a modest but steady increase as the fall campaign period opens."
  - "South Dakota has not sent a Democrat to the Senate in decades; volume here likely reflects portfolio hedging or arbitrage."
  - "Resolves on certified 2026 South Dakota Senate general election results."
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
      kalshi_vol_24h_usd: 10846.37
sources:
  - label: "ClearMarket market record: Will the winner of the South Dakota Senate election be "
    url: "https://clearmarket.fyi/events/senatesd-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The South Dakota Senate spike at 95% is a low-signal event for directional desks but may reflect systematic portfolio construction across a Senate sweep basket rather than any idiosyncratic state development.
