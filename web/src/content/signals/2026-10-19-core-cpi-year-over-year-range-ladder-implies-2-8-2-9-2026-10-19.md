---
signal_id: "CMSIG2026101902"
signal_slug: "core-cpi-year-over-year-range-ladder-implies-2-8-2-9-2026-10-19"
headline: "Core CPI year-over-year range: ladder implies 2.8-2.9%"
semantic_title: "Core CPI inflation path seen near 2.8-2.9 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T06:58:15.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.41
  volume_24h_usd: 9.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "The Kalshi ladder prices 57% above 2.8% and 41% above 2.9%, implying consensus sits in the 2.8-2.9% range for the reference core CPI print."
  - "Trading volume on this ladder rose 187x day-over-day, a strong signal the September 3.7% headline CPI beat is drawing fresh positioning on the disinflation path."
  - "The 8% Kalshi contract on sub-2.2% core CPI (CM-EVT-K0L95NMQ77) and this 2.8-2.9% ladder are mutually consistent: both price a slow, incomplete disinflation trajectory."
  - "Resolution depends on the BLS CPI release; the ladder's implied 2.8-2.9% range is well below the current 3.7% headline, reflecting an expectation that energy-driven spikes are partly transient."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September CPI beat forecasts at 3.7% year-over-year as gasoline prices surged, raising questions about the pace of disinflation into year-end."
    publisher: "investing.com"
    published_at: "2026-10-19T06:58:15.000Z"
    source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
        retrieved_at: "2026-10-21T07:48:07+00:00"
  - type: "pm_response"
    notes: "Volume surge of 187x day-over-day on the Kalshi ladder confirms the September CPI beat is actively repricing the disinflation timeline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Economic Week Ahead: Hot Inflation Meets a Critical Week for Corporate"
    url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    published_at: "2026-10-19T06:58:15.000Z"
    retrieved_at: "2026-10-21T07:48:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
