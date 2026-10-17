---
signal_id: "CMSIG2026101701"
signal_slug: "nov-cpi-m-m-implied-0-1-0-2-kalshi-ladder-2026-10-17"
headline: "Nov CPI m/m implied 0.1-0.2%: Kalshi ladder"
semantic_title: "November CPI seen rising, odds cluster near 0.1-0.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T08:00:08.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T0.2"
  question_raw: "Will CPI rise more than 0.2% in November 2026?"
  current_price: 0.46
  volume_24h_usd: 24.08
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "Kalshi ladder pins November 2026 CPI month-over-month in the 0.1-0.2% range: 88% above -0.1%, 63% above 0.1%, only 46% above 0.2%."
  - "Trading volume on the Kalshi November CPI ladder surged roughly 1,984x day over day, signaling intense fresh attention as earnings week spotlights inflation."
  - "The sharp drop from 63% above 0.1% to only 22% above 0.3% shows the market prices a mild but positive print, not a hot overshoot."
  - "The October CPI Kalshi ladder (CM-EVT-N58KJP0K82) implies 0.2-0.3% with volume also up 217x, suggesting the market prices sequential mild acceleration into year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "AP reports US earnings and economic data this week will spotlight inflation's ongoing toll on consumers and businesses."
    publisher: "Damian J. Troise"
    published_at: "2026-10-17T08:00:08.000Z"
    source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Damian J. Troise"
        source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
        retrieved_at: "2026-10-17T11:57:10+00:00"
  - type: "pm_response"
    notes: "Kalshi carries both the October and November CPI month-over-month ladders; the November contract saw the largest volume spike in this data set at nearly 2,000x day-over-day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Damian J. Troise: US earnings and economic reports this week to spotlight inflation’s to"
    url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    published_at: "2026-10-17T08:00:08.000Z"
    retrieved_at: "2026-10-17T11:57:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
