---
signal_id: "CMSIG20261102VS07"
signal_slug: "will-republicans-win-the-senate-race-in-vol-35635"
headline: "Louisiana Senate GOP: 85% on $36K inflow"
semantic_title: "Republicans are heavy favorites in the Louisiana Senate race"
telemetry: "85% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-862GRMT4M0"
event_slug: "kxsenatela-26nov"
event_question: "Will there be a Louisiana Senate winner by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATELA-26NOV-R"
  question_raw: "Will Republicans win the Senate race in Louisiana?"
  current_price: 0.85
  volume_24h_usd: 35635.58
  volume_cumulative_usd: 122653.19
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 85% in Louisiana's Senate race, a strong favorite consistent with the state's partisan profile."
  - "$35.6K in 24h is 29% of all-time volume, a pre-election positioning bump on a largely settled race."
  - "Volume arriving near election day on an 85% contract suggests participants are closing positions or locking in cheap exposure."
  - "Resolves on Louisiana Senate election result."
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
      kalshi_vol_24h_usd: 35635.58
sources:
  - label: "ClearMarket market record: Will there be a Louisiana Senate winner by January 4, 2"
    url: "https://clearmarket.fyi/events/kxsenatela-26nov"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Pre-election volume on a high-confidence Republican Louisiana Senate contract points to housekeeping activity, desks closing hedges rather than expressing new uncertainty.
