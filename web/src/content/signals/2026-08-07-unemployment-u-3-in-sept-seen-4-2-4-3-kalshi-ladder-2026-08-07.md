---
signal_id: "CMSIG2026080703"
signal_slug: "unemployment-u-3-in-sept-seen-4-2-4-3-kalshi-ladder-2026-08-07"
headline: "Unemployment U-3 in Sept seen 4.2-4.3%: Kalshi ladder"
semantic_title: "September unemployment rate priced in the 4.2-4.3 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "Unemployment rate U-3, September 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in September?"
  current_price: 0.4
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder implies September 2026 unemployment in the 4.2-4.3% range: 54% above 4.2%, 40% above 4.3%, only 17% above 4.4%."
  - "July's surprise job loss of 23,000 is consistent with the ladder's implied drift upward from recent readings near 4.1-4.2%."
  - "The October unemployment ladder (CM-EVT-2X91TW50H2) shows a nearly identical 4.2-4.3% central range, signaling no expected sharp deterioration beyond September."
  - "Resolves via the Bureau of Labor Statistics official U-3 unemployment release for September 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. economy unexpectedly lost 23,000 jobs in July, raising fresh concerns about the health of the labor market."
    publisher: "Rachel Siegel"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/08/07/economy/us-jobs-report-july-analysis"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rachel Siegel"
        source_url: "https://www.cnn.com/2026/08/07/economy/us-jobs-report-july-analysis"
        retrieved_at: "2026-08-09T08:36:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via BLS data; distribution consistent with a gradual labor market softening narrative, not a sharp breakdown."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rachel Siegel: What the jobs report can’t tell us about the confounding economic mome"
    url: "https://www.cnn.com/2026/08/07/economy/us-jobs-report-july-analysis"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-09T08:36:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
