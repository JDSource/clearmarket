---
signal_id: "CMSIG2026092802"
signal_slug: "sept-payrolls-implied-90k-100k-kalshi-ladder-2026-09-28"
headline: "Sept payrolls implied 90K-100K: Kalshi ladder"
semantic_title: "September payrolls seen near 90K-100K, odds slip below 50% above that"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.44
  volume_24h_usd: 86.97
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder implies September payrolls in the 90,000-100,000 range: 53% above 90K, 44% above 100K, collapsing to 30% above 125K."
  - "Wall Street's consensus near 100K aligns with the ladder's 44% probability, meaning the market is not pricing a repeat of August's 162K upside surprise."
  - "The hawkish Fed backdrop and dollar strength reported today are consistent with a labor market that is cooling but not collapsing."
  - "Resolution is via the Bureau of Labor Statistics Employment Situation report; benchmark revisions can shift the headline after initial release."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street forecasts roughly 100,000 September nonfarm payrolls after August's blowout 162,000 print, with the Fed's rate-hike cycle seen weighing on hiring momentum."
    publisher: "gate.com"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.gate.com/news/detail/us-september-jobs-report-expectations-rise-after-augusts-162k-gain-24599302"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "gate.com"
        source_url: "https://www.gate.com/news/detail/us-september-jobs-report-expectations-rise-after-augusts-162k-gain-24599302"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers a wide payroll range; the implied median near 90K-100K reflects consensus, not a tail bet."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "gate.com: US September Jobs Report Expectations Rise After August's 162K Gain |"
    url: "https://www.gate.com/news/detail/us-september-jobs-report-expectations-rise-after-augusts-162k-gain-24599302"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
