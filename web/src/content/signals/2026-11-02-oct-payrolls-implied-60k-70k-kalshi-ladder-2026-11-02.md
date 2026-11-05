---
signal_id: "CMSIG2026110201"
signal_slug: "oct-payrolls-implied-60k-70k-kalshi-ladder-2026-11-02"
headline: "Oct payrolls implied 60K-70K: Kalshi ladder"
semantic_title: "October payrolls seen near 60K-70K, job growth stays odds-on"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:17:35.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T70000"
  question_raw: "Will above 70000 jobs be added in October 2026?"
  current_price: 0.47
  volume_24h_usd: 371.61
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder puts the implied October payrolls range at 60K-70K: 92% above zero, 57% above 50K, only 31% above 100K."
  - "Trading volume on this contract surged 22,979% day-over-day, signaling sharp fresh attention ahead of Friday's release."
  - "The sharp drop in probability between 50K (57%) and 70K (47%) marks where the distribution thins, market sees modest but positive job growth as the central case."
  - "The Bureau of Labor Statistics Employment Situation report settles this contract; hurricane or survey-week distortions could move the print outside the consensus band."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed held rates and jobs data is the week's focal point, with payrolls and unemployment reports due Friday."
    publisher: "investing.com"
    published_at: "2026-11-02T17:17:35.000Z"
    source_url: "https://www.investing.com/news/stock-market-news/weekly-economic-outlook-payrolls-and-fed-speakers-in-focus-93CH-4992504"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/stock-market-news/weekly-economic-outlook-payrolls-and-fed-speakers-in-focus-93CH-4992504"
        retrieved_at: "2026-11-05T07:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder, volume up 230x day-over-day, reflects pre-report positioning around a consensus of modest October job gains."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Weekly economic outlook: payrolls and Fed speakers in focus By Investi"
    url: "https://www.investing.com/news/stock-market-news/weekly-economic-outlook-payrolls-and-fed-speakers-in-focus-93CH-4992504"
    published_at: "2026-11-02T17:17:35.000Z"
    retrieved_at: "2026-11-05T07:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
