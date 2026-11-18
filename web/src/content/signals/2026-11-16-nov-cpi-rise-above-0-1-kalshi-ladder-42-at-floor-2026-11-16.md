---
signal_id: "CMSIG2026111603"
signal_slug: "nov-cpi-rise-above-0-1-kalshi-ladder-42-at-floor-2026-11-16"
headline: "Nov CPI rise above -0.1%: Kalshi ladder 42% at floor"
semantic_title: "November CPI below negative 0.1 percent stays unlikely"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-11-16T15:15:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in November 2026?"
  current_price: 0.42
  volume_24h_usd: 1590.19
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "The Kalshi ladder implies only 42% probability that November CPI rises more than -0.1% month-over-month, with cumulative mass collapsing sharply above 0.0% at 13%."
  - "October CPI printed 0.4% month-over-month headline; a sharp deceleration to below 0.0% in November would be a major reversal that the ladder treats as the modal outcome."
  - "The implied distribution centering below zero contrasts sharply with the recent run of hot monthly readings, suggesting markets may be pricing seasonal base effects or energy giveback."
  - "Resolution depends on the Bureau of Labor Statistics November CPI release; the ladder will be live until that print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "JP Morgan Asset Management's weekly update highlights Q3 GDP growth of 3.4% and persistent inflation pressures heading into the November data cycle."
    publisher: "Contributor Author"
    published_at: "2026-11-16T15:15:00.000Z"
    source_url: "https://www.interactivebrokers.com/campus/traders-insight/securities/macro/economic-update-week-of-november-16-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Contributor Author"
        source_url: "https://www.interactivebrokers.com/campus/traders-insight/securities/macro/economic-update-week-of-november-16-2026/"
        retrieved_at: "2026-11-18T07:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on November 2026 CPI shows a heavily left-skewed distribution, with cumulative probability collapsing above 0.0%; the market is not aligned with the recent inflation trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Contributor Author: Economic Update: Week of November 16, 2026"
    url: "https://www.interactivebrokers.com/campus/traders-insight/securities/macro/economic-update-week-of-november-16-2026/"
    published_at: "2026-11-16T15:15:00.000Z"
    retrieved_at: "2026-11-18T07:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
