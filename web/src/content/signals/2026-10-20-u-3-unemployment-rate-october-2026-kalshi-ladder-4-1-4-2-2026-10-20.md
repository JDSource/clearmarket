---
signal_id: "CMSIG2026102003"
signal_slug: "u-3-unemployment-rate-october-2026-kalshi-ladder-4-1-4-2-2026-10-20"
headline: "U-3 unemployment rate, October 2026: Kalshi ladder 4.1-4.2%"
semantic_title: "October unemployment rate priced near 4.1-4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-2X91TW50H2"
event_slug: "kxu3-26oct"
event_question: "U-3 unemployment rate, October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26OCT-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in October?"
  current_price: 0.33
  volume_24h_usd: 27.31
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies the October U-3 unemployment rate in the 4.1-4.2% range: 91% probability above 4.0%, 68% above 4.1%, only 33% above 4.2%."
  - "Strong September jobs data is broadly consistent with the ladder's near-full-employment read; the market is not pricing any labor market deterioration."
  - "Volume on this contract surged 331.9 times day-over-day, indicating sharp new activity likely tied to the September employment and CPI data releases."
  - "Resolves via the Bureau of Labor Statistics monthly Employment Situation release; the tight 4.1-4.2% implied range leaves little room for a surprise in either direction."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September employment data showed the labor market remained strong enough for the Fed to focus on inflation, with full-employment conditions intact per analyst commentary."
    publisher: "Yelena Shulyatyeva"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yelena Shulyatyeva"
        source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
        retrieved_at: "2026-10-21T13:24:06+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder drew extraordinary volume, over 331 times prior-day levels, making it one of the most actively repriced contracts in the current macro cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yelena Shulyatyeva: Labor Market Strong Enough for Fed to Focus on Inflation"
    url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-21T13:24:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
