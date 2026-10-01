---
signal_id: "CMSIG2026093002"
signal_slug: "sept-jobs-added-seen-90k-100k-prediction-market-ladder-2026-09-30"
headline: "Sept jobs added seen 90K-100K: prediction market ladder"
semantic_title: "September private payrolls odds slip around the 90K-100K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 jobs added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.47
  volume_24h_usd: 2997.77
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Prediction market ladder implies 90K-100K for September jobs added: 57% above 90K, dropping to 47% above 100K."
  - "ADP's 90,000 print lands squarely in the market's modal range, making the news broadly consistent with prevailing odds."
  - "The sharp drop from 57% to 31% between the 90K and 125K strikes signals little confidence in an upside surprise from Friday's official nonfarm payroll report."
  - "The 96% probability above -25K confirms no meaningful recession-level job-loss risk is priced; the debate is purely about the upside."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ADP reported private-sector employment rose 90,000 in September 2026, with base pay up 3.2% and gross pay up 4.7%."
    publisher: "mediacenter.adp.com"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://mediacenter.adp.com/2026-09-30-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-90,000-Jobs-in-September"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "mediacenter.adp.com"
        source_url: "https://mediacenter.adp.com/2026-09-30-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-90,000-Jobs-in-September"
        retrieved_at: "2026-10-01T15:03:15+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via the named resolution source; ADP is a leading private-sector indicator ahead of the official BLS nonfarm payroll release due Friday."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "mediacenter.adp.com: ADP National Employment Report: Private-Sector Employment Increased by"
    url: "https://mediacenter.adp.com/2026-09-30-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-90,000-Jobs-in-September"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-01T15:03:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
