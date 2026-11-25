---
signal_id: "CMSIG2026112404"
signal_slug: "nov-cpi-above-0-1-kalshi-ladder-32-at-that-strike-2026-11-24"
headline: "Nov CPI above -0.1%: Kalshi ladder 32% at that strike"
semantic_title: "November CPI below negative 0.1 percent builds as base case"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-24T03:25:00.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in November 2026?"
  current_price: 0.32
  volume_24h_usd: 1028.79
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "The Kalshi ladder implies November CPI is most likely to come in below -0.1%, with only 32% odds at the -0.1% strike and near-zero odds above 0.0%."
  - "Trading volume on this contract rose roughly 13,228x day-over-day, an extraordinary spike signaling intense fresh attention ahead of the upcoming CPI print."
  - "A sub-zero monthly CPI reading would be notable given Williams's recent hawkish commentary, suggesting the market may be pricing in a one-month energy or goods-driven dip rather than a trend shift."
  - "The core CPI annual ladder (CM-EVT-BXDL61HVR9) still prices 99% odds above 2.0% for the year, so a negative monthly print alone would not resolve the inflation debate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A broad U.S. economy analysis highlighted labor market cooling, GDP trends, and Fed policy crosscurrents ahead of key data releases including PCE."
    publisher: "seekingalpha.com"
    published_at: "2026-11-24T03:25:00.000Z"
    source_url: "https://seekingalpha.com/market-outlook/us-economy"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "seekingalpha.com"
        source_url: "https://seekingalpha.com/market-outlook/us-economy"
        retrieved_at: "2026-11-25T07:47:45+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on November 2026 monthly CPI change; the extreme volume spike flags this as a heavily watched near-term resolution event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "seekingalpha.com: U.S. Economy Analysis: Inflation, Jobs, GDP and the Fed | Seeking Alph"
    url: "https://seekingalpha.com/market-outlook/us-economy"
    published_at: "2026-11-24T03:25:00.000Z"
    retrieved_at: "2026-11-25T07:47:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
