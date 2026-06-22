---
signal_id: "CMSIG2026062204"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-22"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound at 3.50 to 3.75 anchors firmly"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T09:17:30.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound following June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 36% above 3.75%, implying the modal outcome is exactly 3.75%."
  - "BofA's call for no cuts until 2028 and market commentary calling any hike a gesture are both absorbed into this distribution without pushing above 4.0%, which prices at only 16%."
  - "The distribution effectively rules out a return to 4.0% or higher, with the 4.25% strike at just 8%, signaling the hawkish shift is already priced as a plateau rather than a new hiking cycle."
  - "Resolves via Federal Reserve policy announcement; the settlement level is the official upper bound of the target range, not market rates."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A market brief argues that any additional Fed rate hike would be largely symbolic, while BofA now sees no cuts until 2028 and the New York Fed DSGE model published its June 2026 forecast."
    publisher: "investing.com"
    published_at: "2026-06-22T09:17:30.000Z"
    source_url: "https://www.investing.com/analysis/market-brief-1-more-rate-hike-just-a-gesture-200682535"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/market-brief-1-more-rate-hike-just-a-gesture-200682535"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder shows the market is absorbing hawkish commentary from BofA and Fed communications cuts without repricing a meaningful probability of renewed hikes above 4.0%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Market Brief: 1 More Rate Hike, Just a Gesture | Investing.com"
    url: "https://www.investing.com/analysis/market-brief-1-more-rate-hike-just-a-gesture-200682535"
    published_at: "2026-06-22T09:17:30.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
