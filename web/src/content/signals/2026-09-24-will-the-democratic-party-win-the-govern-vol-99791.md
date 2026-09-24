---
signal_id: "CMSIG20260924VS02"
signal_slug: "will-the-democratic-party-win-the-govern-vol-99791"
headline: "Georgia governor Dems: 54% on $100K Kalshi spike"
semantic_title: "Democrats hold a narrow 54% edge in Georgia governor race"
telemetry: "54% · $100K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-RHX55RJPT1"
event_slug: "govpartyga-26"
event_question: "Georgia Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYGA-26-D"
  question_raw: "Will the Democratic party win the governorship in Georgia"
  current_price: 0.54
  volume_24h_usd: 99791.75
  volume_cumulative_usd: 277212.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "54% odds place Democrats as slim favorites for the Georgia governorship, near a coin flip."
  - "$100K in 24h equals 36% of all-time Kalshi volume, a rare single-session concentration."
  - "Near-50% pricing with surging volume suggests the race is competitively contested and attracting fresh capital."
  - "Resolves on Georgia gubernatorial election result."
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
      kalshi_vol_24h_usd: 99791.75
sources:
  - label: "ClearMarket market record: Georgia Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyga-26"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With odds barely above 50% and over a third of all-time volume printing today, this Georgia contract signals a genuinely contested race that political-risk desks cannot ignore heading into the election cycle.
