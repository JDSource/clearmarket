---
signal_id: "CMSIG2026101901"
signal_slug: "core-cpi-above-2-in-2026-kalshi-ladder-99-2026-10-19"
headline: "Core CPI above 2% in 2026: Kalshi ladder 99%"
semantic_title: "Core CPI above 2 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T06:58:15.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate, 2026"
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
  - "Kalshi ladder prices core CPI above 2.0% at 99%, with the market-implied central range at 2.8-2.9% for the year."
  - "September CPI printed 3.7% headline year-over-year, well above 2%; ladder is fully consistent with the hot inflation news, showing no daylight between the print and the contract."
  - "Trading volume on this ladder surged 187.7 times day-over-day, signaling a sharp influx of fresh attention following the inflation surprise."
  - "A separate Kalshi contract puts only 8% on core CPI falling below 2.2% in 2026, reinforcing that the market sees virtually no path to rapid disinflation this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US September CPI rose 0.6% month-over-month and 3.7% year-over-year, beating consensus, as hot inflation dominates the macro agenda alongside a critical corporate earnings week."
    publisher: "investing.com"
    published_at: "2026-10-19T06:58:15.000Z"
    source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
        retrieved_at: "2026-10-21T13:24:06+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder resolves via Bureau of Labor Statistics Employment Situation reports; the 99% floor at 2.0% leaves essentially zero probability on a sub-2% outcome for full-year 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Economic Week Ahead: Hot Inflation Meets a Critical Week for Corporate"
    url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    published_at: "2026-10-19T06:58:15.000Z"
    retrieved_at: "2026-10-21T13:24:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
