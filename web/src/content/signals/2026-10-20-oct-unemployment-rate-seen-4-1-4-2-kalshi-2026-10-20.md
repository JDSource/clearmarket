---
signal_id: "CMSIG2026102002"
signal_slug: "oct-unemployment-rate-seen-4-1-4-2-kalshi-2026-10-20"
headline: "Oct unemployment rate seen 4.1-4.2%: Kalshi"
semantic_title: "October unemployment rate holds near 4.1 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-2X91TW50H2"
event_slug: "kxu3-26oct"
event_question: "October 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26OCT-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in October?"
  current_price: 0.34
  volume_24h_usd: 115.46
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies October unemployment in the 4.1-4.2% range: 68% above 4.1% but only 34% above 4.2%."
  - "Strong September payrolls narrative is consistent with Kalshi pricing unemployment anchored just above 4.1%, with no sign of labor market deterioration."
  - "Companion Kalshi ladder (CM-EVT-6CSLHX0K76) puts October payroll additions at 70K-80K implied midpoint, reinforcing a steady-but-not-hot jobs picture."
  - "Resolves via Bureau of Labor Statistics Employment Situation release; revisions to prior months could shift the implied range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September employment data were strong enough for Fed to conclude full employment, per BNY analysis dated October 20."
    publisher: "Yelena Shulyatyeva"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yelena Shulyatyeva"
        source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
        retrieved_at: "2026-10-23T07:48:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows tight consensus around 4.1-4.2%, with tails below 3.9% and above 4.3% each priced below 10%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yelena Shulyatyeva: Labor Market Strong Enough for Fed to Focus on Inflation"
    url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-23T07:48:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
