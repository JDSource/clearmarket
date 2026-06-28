---
signal_id: "CMSIG2026062504"
signal_slug: "june-fed-funds-upper-bound-at-3-75-4-kalshi-ladder-2026-06-25"
headline: "June Fed funds upper bound at 3.75-4%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen at 3.75 to 4 percent after hike talk"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 3.75-4.0% range: 65% above 3.75% but only 36% above 4.0%."
  - "May PCE breaking above 4% keeps hike talk active; the distribution's sharp drop above 4.0% shows the market is skeptical of an actual move above current levels."
  - "Minneapolis Fed President Neel Kashkari penciled in one hike this year, yet the ladder's steep cliff above 4.0% shows the market fading that posture."
  - "A companion Kalshi ladder (CM-EVT-4ZQLQPNH91) similarly prices 54% above 3.75% but only 8% above 4.0%, corroborating the range read across contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US PCE inflation topped 4% for the first time in three years, keeping a potential Fed rate hike in play according to multiple reports."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-06-25T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-may-pce-inflation-rises-4-1-keeping-fed-hike-in-play/articleshow/131997380.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-may-pce-inflation-rises-4-1-keeping-fed-hike-in-play/articleshow/131997380.cms"
        retrieved_at: "2026-06-28T10:24:59+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder implies the market is consistent with a hold at current levels, discounting Fed officials' hike signals."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: US inflation tops 4% for first time in three years, keeping Fed hike i"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-may-pce-inflation-rises-4-1-keeping-fed-hike-in-play/articleshow/131997380.cms"
    published_at: "2026-06-25T00:00:00.000Z"
    retrieved_at: "2026-06-28T10:24:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
