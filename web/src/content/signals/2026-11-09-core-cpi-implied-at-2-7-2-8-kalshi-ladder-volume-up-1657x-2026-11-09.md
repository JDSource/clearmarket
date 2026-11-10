---
signal_id: "CMSIG2026110902"
signal_slug: "core-cpi-implied-at-2-7-2-8-kalshi-ladder-volume-up-1657x-2026-11-09"
headline: "Core CPI implied at 2.7-2.8%: Kalshi ladder, volume up 1657x"
semantic_title: "Core CPI seen near 2.7-2.8 percent, stays above target"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T19:00:54.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.8"
  question_raw: "Will the rate of core CPI inflation be above 2.8% for the year ending in November 2026?"
  current_price: 0.32
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder for core CPI year-over-year implies a range of 2.7-2.8%: 63% chance above 2.7%, dropping to 32% above 2.8%."
  - "Trading volume on this Kalshi contract surged 1,657x day-over-day, a strong signal of intense fresh positioning around the October CPI release."
  - "The distribution shows only 5% probability above 3.0%, meaning the market does not fully align with the 'persistent inflation' narrative from analyst commentary."
  - "The companion month-over-month CPI ladder (CM-EVT-T57DHL6V48) implies a reading near -0.1 to 0.0%, with 56% at -0.1%, a cross-market signal worth watching for internal consistency."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October CPI data was released Tuesday with headline and core prices firming, drawing massive prediction-market attention ahead of the print."
    publisher: "investing.com"
    published_at: "2026-11-09T19:00:54.000Z"
    source_url: "https://www.investing.com/news/stock-market-news/cpi-data-and-fed-speakers-highlight-tuesdays-economic-calendar-93CH-5013020"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/stock-market-news/cpi-data-and-fed-speakers-highlight-tuesdays-economic-calendar-93CH-5013020"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Bureau of Labor Statistics CPI release; volume spike confirms this is the focal prediction-market event of the day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: CPI data and Fed speakers highlight Tuesday’s economic calendar By Inv"
    url: "https://www.investing.com/news/stock-market-news/cpi-data-and-fed-speakers-highlight-tuesdays-economic-calendar-93CH-5013020"
    published_at: "2026-11-09T19:00:54.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
