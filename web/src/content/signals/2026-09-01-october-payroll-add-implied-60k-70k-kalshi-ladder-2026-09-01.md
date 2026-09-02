---
signal_id: "CMSIG2026090103"
signal_slug: "october-payroll-add-implied-60k-70k-kalshi-ladder-2026-09-01"
headline: "October payroll add implied 60K-70K: Kalshi ladder"
semantic_title: "August payroll addition seen near 60K to 70K by prediction markets"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-01T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "Nonfarm payroll jobs added, October 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T60000"
  question_raw: "Will above 60000 jobs be added in October 2026?"
  current_price: 0.48
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Ladder implies the market-weighted payroll add near 60K-70K: 54% above 50K, 48% above 60K, 50% above 70K, a notably flat distribution around that range."
  - "Wolfe Research's 65K August forecast lands squarely in the ladder's implied central range, suggesting the market is aligned with the soft-payroll consensus."
  - "Weak job growth would undercut the case for a September Fed hike, creating tension with the 72% Polymarket probability on a 2026 rate increase."
  - "The ladder covers October additions; August data prints Friday and will be the first live test of whether the sub-100K soft-landing narrative holds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wolfe Research forecasts August nonfarm payrolls rising only 65,000, well below trend, complicating the Fed's rate-hike calculus ahead of the September meeting."
    publisher: "weex.com"
    published_at: "2026-09-01T00:00:00.000Z"
    source_url: "https://www.weex.com/news/detail/latest-non-farm-payroll-forecast-job-growth-may-slow-fed-faces-complex-choices-aqdf6iicgz6zdf7w4ih5ee9j"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "weex.com"
        source_url: "https://www.weex.com/news/detail/latest-non-farm-payroll-forecast-job-growth-may-slow-fed-faces-complex-choices-aqdf6iicgz6zdf7w4ih5ee9j"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Ladder distribution is unusually flat between 60K and 70K strikes, with the 50% crossover landing inside that range, a sign of genuine two-way uncertainty on the payroll print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "weex.com: Latest Non-Farm Payroll Forecast: Job Growth May Slow, Fed Faces Compl"
    url: "https://www.weex.com/news/detail/latest-non-farm-payroll-forecast-job-growth-may-slow-fed-faces-complex-choices-aqdf6iicgz6zdf7w4ih5ee9j"
    published_at: "2026-09-01T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
