---
signal_id: "CMSIG2026093003"
signal_slug: "sept-jobs-added-seen-90k-100k-prediction-market-ladder-2026-09-30"
headline: "Sept jobs added seen 90K-100K: prediction market ladder"
semantic_title: "September job additions seen in the 90K to 100K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm jobs added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.46
  volume_24h_usd: 1861.83
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "The ladder implies a market-consensus range of 90,000-100,000 jobs: 58% above 90K but only 46% above 100K, bracketing the ADP print precisely."
  - "ADP's 90,000 September figure lands right at the 58% threshold, meaning the market is neither surprised nor pushed to reprice the upper tail."
  - "The distribution still assigns 94% probability above negative 25,000, confirming markets see no serious risk of an outright job loss month."
  - "Friday's official BLS nonfarm payrolls print is the resolution event; ADP and BLS frequently diverge, keeping the 100K-plus tail genuinely uncertain."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported 90,000 private-sector jobs added in September, above the prior month's 36,000 and ahead of Wall Street expectations."
    publisher: "Jeff Cox"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/30/private-sector-jobs-rose-by-90000-in-september-better-than-expected-adp-reports.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/09/30/private-sector-jobs-rose-by-90000-in-september-better-than-expected-adp-reports.html"
        retrieved_at: "2026-09-30T14:32:59+00:00"
  - type: "pm_response"
    notes: "Ladder event carries no named venue; resolution source is unspecified but expected to track BLS nonfarm payroll data for September 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Private sector jobs rose by 90,000 in September, better than expected,"
    url: "https://www.cnbc.com/2026/09/30/private-sector-jobs-rose-by-90000-in-september-better-than-expected-adp-reports.html"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T14:32:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
