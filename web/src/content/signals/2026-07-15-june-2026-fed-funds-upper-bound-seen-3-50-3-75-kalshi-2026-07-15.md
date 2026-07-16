---
signal_id: "CMSIG2026071505"
signal_slug: "june-2026-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-15"
headline: "June 2026 Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound anchors in 3.50-3.75 percent band"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-15T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.31
  volume_24h_usd: 99.26
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.50-3.75% range: 92% above 3.50% but only 31% above 3.75%."
  - "The Beige Book's picture of rising activity and only marginal inflation easing is consistent with the market's central scenario of a hold near current levels."
  - "A separate ladder for a later meeting shows 86% above 3.50% but only 34% above 3.75%, nearly identical to this one, suggesting markets see no imminent move."
  - "Producer prices fell by the largest amount since the pandemic per Story 6, which argues against rate hikes, consistent with the low probability above 3.75%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed Beige Book showed broadly rising economic activity and employment growth with inflation easing only slightly, providing context for the next FOMC meeting in two weeks."
    publisher: "AOL"
    published_at: "2026-07-15T00:00:00.000Z"
    source_url: "https://www.aol.com/articles/economic-activity-rise-inflation-may-181529000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/economic-activity-rise-inflation-may-181529000.html"
        retrieved_at: "2026-07-16T10:04:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official rate announcement; the tight clustering between the two meeting ladders signals a consensus hold scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Economic activity rising and inflation easing slightly, Fed survey sho"
    url: "https://www.aol.com/articles/economic-activity-rise-inflation-may-181529000.html"
    published_at: "2026-07-15T00:00:00.000Z"
    retrieved_at: "2026-07-16T10:04:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
