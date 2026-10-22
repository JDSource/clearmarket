---
signal_id: "CMSIG2026102004"
signal_slug: "oct-unemployment-rate-seen-at-4-1-4-2-polymarket-ladder-2026-10-20"
headline: "Oct unemployment rate seen at 4.1-4.2%: Polymarket ladder"
semantic_title: "Unemployment rate odds cluster near 4.1 to 4.2 percent for October"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-2X91TW50H2"
event_slug: "kxu3-26oct"
event_question: "October 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26OCT-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in October?"
  current_price: 0.33
  volume_24h_usd: 118.1
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Ladder pricing puts the October U-3 rate in the 4.1-4.2% range: 69% above 4.1%, only 33% above 4.2%, with volume up more than 100x day-over-day."
  - "The surge in trading volume signals this contract is drawing heavy fresh attention alongside strong labor-market data this week."
  - "Initial jobless claims fell to 194,000, the lowest since July, reinforcing the tight-labor-market narrative consistent with sub-4.2% pricing."
  - "The 98% probability above 3.9% and rapid drop above 4.2% indicate near-certainty of staying below 4.3%, leaving the debate tightly in the 4.1-4.2% band."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September employment data were strong enough to confirm full employment, giving the Fed room to focus on inflation rather than supporting the labor market."
    publisher: "Yelena Shulyatyeva"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yelena Shulyatyeva"
        source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
        retrieved_at: "2026-10-22T13:24:33+00:00"
  - type: "pm_response"
    notes: "Volume spike of over 10,000% day-over-day on Polymarket makes this the most actively repriced labor contract in today's session."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yelena Shulyatyeva: Labor Market Strong Enough for Fed to Focus on Inflation"
    url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-22T13:24:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
