---
signal_id: "CMSIG2026110406"
signal_slug: "fed-funds-above-4-0-next-meeting-kalshi-79-2026-11-04"
headline: "Fed funds above 4.0% next meeting: Kalshi 79%"
semantic_title: "Fed hold leaves rate path priced in 4 percent zone"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-04T09:04:26.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 196.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder places 79% on the Fed funds upper bound exceeding 4.0% at the next meeting, implying a December hike is the central case."
  - "The Fed's October hold is consistent with the ladder, 99% probability remains above 3.75%, confirming the market sees the hold as a pause, not a pivot."
  - "The cliff above 4.25% (only 3%) signals one additional hike is priced, not a cycle; the market is not pricing aggressive tightening beyond December."
  - "Resolution via the Federal Reserve's official announcement; Friday's October jobs report is the next major input before the December meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held rates at its October 28 meeting as inflation remained elevated, with the next hike expected in December."
    publisher: "Ibonomics Editorial"
    published_at: "2026-11-04T09:04:26.000Z"
    source_url: "https://www.ibonomics.org/briefs/weekly/the-fed-holds-as-inflation-stays-elevated-oct-28-nov-3-2026-08f27ee3"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ibonomics Editorial"
        source_url: "https://www.ibonomics.org/briefs/weekly/the-fed-holds-as-inflation-stays-elevated-oct-28-nov-3-2026-08f27ee3"
        retrieved_at: "2026-11-04T15:56:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder is the only priced candidate for this story; all other Fed rate events in this story have no price data available."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ibonomics Editorial: The Fed Holds as Inflation Stays Elevated, Oct 28, Nov 3, 2026 | IBonom"
    url: "https://www.ibonomics.org/briefs/weekly/the-fed-holds-as-inflation-stays-elevated-oct-28-nov-3-2026-08f27ee3"
    published_at: "2026-11-04T09:04:26.000Z"
    retrieved_at: "2026-11-04T15:56:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
