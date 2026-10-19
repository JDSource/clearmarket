---
signal_id: "CMSIG2026101904"
signal_slug: "core-cpi-year-end-seen-2-8-2-9-kalshi-ladder-2026-10-19"
headline: "Core CPI year-end seen 2.8-2.9%: Kalshi ladder"
semantic_title: "Annual core CPI seen settling near 2.8 to 2.9 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T06:58:15.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Annual core CPI rate for year ending 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.3
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder implies annual core CPI settling near 2.8-2.9%: 57% above 2.8% but only 30% above 2.9%, with a sharp drop to 17% above 3.0%."
  - "The distribution confirms what the news describes: persistent inflation above the Fed's 2% target, but markets do not price a return to 3%-plus territory as likely."
  - "A companion Kalshi binary (CM-EVT-K0L95NMQ77) puts only 8% probability on core CPI falling below 2.2% this year, reinforcing the ladder's central tendency."
  - "Resolves via Bureau of Labor Statistics Employment Situation / CPI release; the ladder settles against the named annual figure, not a monthly print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Investing.com flags hot inflation meeting a critical corporate earnings week, with core price pressures remaining above the Fed's 2% target."
    publisher: "investing.com"
    published_at: "2026-10-19T06:58:15.000Z"
    source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
        retrieved_at: "2026-10-19T07:47:26+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution clusters tightly around 2.8-2.9%, showing the market prices stubborn disinflation stall rather than either a return to target or a re-acceleration above 3%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Economic Week Ahead: Hot Inflation Meets a Critical Week for Corporate"
    url: "https://www.investing.com/analysis/economic-week-ahead-hot-inflation-meets-a-critical-week-for-corporate-earnings-200689787"
    published_at: "2026-10-19T06:58:15.000Z"
    retrieved_at: "2026-10-19T07:47:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
