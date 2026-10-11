---
signal_id: "CMSIG2026100902"
signal_slug: "sept-unemployment-implied-4-1-4-2-kalshi-ladder-2026-10-09"
headline: "Sept unemployment implied 4.1-4.2%: Kalshi ladder"
semantic_title: "Unemployment rate odds cluster near 4.1 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-2X91TW50H2"
event_slug: "kxu3-26oct"
event_question: "Unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26OCT-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in October?"
  current_price: 0.27
  volume_24h_usd: 16.74
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder implies unemployment in the 4.1-4.2% range: 72% above 4.1%, only 27% above 4.2%."
  - "Reported September unemployment of 4.2% sits at the upper edge of the market's modal range, consistent with the weak 29,000 payroll print."
  - "October 14 CPI is now the swing factor: a hot print could push the Fed to hike again even with a softening jobs backdrop."
  - "The 72%-to-27% drop from 4.1% to 4.2% thresholds shows the market is nearly fully priced on 4.1% as a floor, with 4.2% as a live tail."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September payrolls rose just 29,000 while the unemployment rate held at 4.2%, pointing to a cooling but not collapsing labor market ahead of October 14 CPI."
    publisher: "Sarah Chen"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sarah Chen"
        source_url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
        retrieved_at: "2026-10-11T14:35:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Bureau of Labor Statistics Employment Situation report; the 4.2% reported figure sits right at the contested upper strike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sarah Chen: September Payrolls Rose 29K: October 14 CPI Is the Fed Test | MarketIn"
    url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-11T14:35:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
