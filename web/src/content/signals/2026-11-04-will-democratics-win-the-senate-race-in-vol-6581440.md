---
signal_id: "CMSIG20261104VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-6581440"
headline: "MS Senate Dem: 77% on $6.6M election-eve surge"
semantic_title: "Traders pile into Democrats winning Mississippi Senate"
telemetry: "77% · $6.6M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-04T07:48:42+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-D"
  question_raw: "Will Democratics win the Senate race in Mississippi?"
  current_price: 0.77
  volume_24h_usd: 6581440.79
  volume_cumulative_usd: 7555221.12
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 77%, a decisive favorite going into results."
  - "24h volume of $6.6M equals 87% of all-time handle, signaling near-peak engagement."
  - "Mississippi Senate race draws rare capital for a deep-red state; odds reflect a surprising contest."
  - "Resolves on certified 2026 midterm outcome."
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
      kalshi_vol_24h_usd: 6581440.79
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-04T07:48:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 87% all-time volume flush on election eve suggests desks are aggressively squaring positions on an unexpected Mississippi Senate competitive race.
