---
signal_id: "CMSIG20261028VS05"
signal_slug: "will-a-democrat-win-the-house-race-for-w-vol-70023"
headline: "Dem wins WI-3 House: 84% on $70K surge"
semantic_title: "Democrats hold an 84% edge in WI-3 through a volume surge"
telemetry: "84% · $70K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T14:50:28+00:00"
event_id: "CM-EVT-6C7CNWJ6R7"
event_slug: "housewi3-26"
event_question: "WI-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI3-26-D"
  question_raw: "Will a Democrat win the House race for WI-3?"
  current_price: 0.84
  volume_24h_usd: 70023.02
  volume_cumulative_usd: 171877.6
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democrat winning WI-3 at 84%, a strong but not locked-in favorite read."
  - "41% of all-time contract volume traded in a single day, a notable acceleration ahead of November."
  - "Fresh volume at high odds suggests traders are either defending the current price or taking profits on long Democratic positions."
  - "Resolves on the certified WI-3 House race outcome."
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
      kalshi_vol_24h_usd: 70023.02
sources:
  - label: "ClearMarket market record: WI-03 House winner?"
    url: "https://clearmarket.fyi/events/housewi3-26"
    retrieved_at: "2026-10-28T14:50:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-conviction Democratic pricing holding through a volume surge signals the district is seen as largely settled, but the activity level still warrants watching for any late shift.
