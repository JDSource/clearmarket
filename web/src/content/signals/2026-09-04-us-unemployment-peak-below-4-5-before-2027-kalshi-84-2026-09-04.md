---
signal_id: "CMSIG2026090402"
signal_slug: "us-unemployment-peak-below-4-5-before-2027-kalshi-84-2026-09-04"
headline: "US unemployment peak below 4.5% before 2027: Kalshi 84%"
semantic_title: "Peak unemployment below 4.5% stays heavily favored before 2027"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak US unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.16
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "Kalshi ladder prices 84% on unemployment peaking below 4.5% before 2027, with only 7% on above 4.8% and 2% on above 5.0%."
  - "August's blowout payroll print is consistent with the market's heavy skew toward a contained labor market through year-end."
  - "Tail risk pricing is minimal: combined probability above 5.5% is under 18%, suggesting the market sees a recession-level spike as a long shot."
  - "Companion September U-3 ladder (CM-EVT-720DZC17Y9) is pinned near 4.1%, reinforcing the view that the labor market is stable, not deteriorating."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US nonfarm payrolls surged 162,000 in August, nearly triple the consensus forecast, with unemployment steady at 4.1%."
    publisher: "Lucia Mutikani"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lucia Mutikani"
        source_url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves on BLS data; strike distribution shows almost no probability mass above 5%, despite tariff-era slowdown fears earlier in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lucia Mutikani: US nonfarm payrolls surge in August; unemployment rate steady at 4.1%"
    url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
