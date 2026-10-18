---
signal_id: "CMSIG2026101703"
signal_slug: "oct-cpi-month-over-month-seen-at-0-2-0-3-kalshi-2026-10-17"
headline: "Oct CPI month-over-month seen at 0.2-0.3%: Kalshi"
semantic_title: "October CPI monthly gain priced in the 0.2-0.3% range"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-17T08:00:08.000Z"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "October 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.3"
  question_raw: "Will CPI rise more than 0.3% in October 2026?"
  current_price: 0.36
  volume_24h_usd: 233.72
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "Kalshi ladder implies October CPI month-over-month in the 0.2-0.3% range: 63% above 0.2%, 36% above 0.3%, and only 15% above 0.4%."
  - "September's hot 3.7% year-over-year headline print sets a high base; the market is not pricing an acceleration but is not pricing relief either."
  - "The November CPI ladder (CM-EVT-T57DHL6V48) shows a much softer implied range of 0.1-0.2%, with 68% above 0.1% but only 46% above 0.2%, suggesting the market sees some moderation ahead."
  - "Resolves via the BLS CPI release for October 2026; the October-to-November deceleration implied across both ladders would still leave core well above 2%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US earnings season and upcoming economic reports this week are expected to spotlight the ongoing toll of inflation on households and corporate margins."
    publisher: "Damian J. Troise"
    published_at: "2026-10-17T08:00:08.000Z"
    source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Damian J. Troise"
        source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
        retrieved_at: "2026-10-18T07:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both the October and November CPI month-over-month ladders; the two distributions together suggest the market expects a modest sequential softening but no breakout disinflation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Damian J. Troise: US earnings and economic reports this week to spotlight inflation’s to"
    url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    published_at: "2026-10-17T08:00:08.000Z"
    retrieved_at: "2026-10-18T07:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
