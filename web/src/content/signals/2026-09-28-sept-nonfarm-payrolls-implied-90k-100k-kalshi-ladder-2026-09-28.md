---
signal_id: "CMSIG2026092801"
signal_slug: "sept-nonfarm-payrolls-implied-90k-100k-kalshi-ladder-2026-09-28"
headline: "Sept nonfarm payrolls implied 90K-100K: Kalshi ladder"
semantic_title: "September payrolls odds stay near even at 90K-100K"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-09-28T04:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.44
  volume_24h_usd: 3168.25
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder prices the September 2026 payrolls print in the 90K-100K range, with 51% above 90K but only 44% above 100K."
  - "Market consensus from the FX Street story pegs analyst median at 84K, putting the Kalshi distribution slightly above the street estimate."
  - "Steep dropoff above 125K (32%) reflects genuine two-sided uncertainty given strong PMI data versus softening labor signals."
  - "Resolution via Bureau of Labor Statistics Employment Situation report; any government revision methodology change could shift the final figure used."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Jobs report and inflation data due this week will test the Fed rate path and gauge US economic strength."
    publisher: "Lewis KrauskopfReuters"
    published_at: "2026-09-28T04:00:00.000Z"
    source_url: "https://www.postandcourier.com/jobs-report-inflation-data-to-test-us-rate-path-economic-strength-this-week/article_4d2a7542-757e-42d2-87ba-37122414e7dc.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lewis KrauskopfReuters"
        source_url: "https://www.postandcourier.com/jobs-report-inflation-data-to-test-us-rate-path-economic-strength-this-week/article_4d2a7542-757e-42d2-87ba-37122414e7dc.html"
        retrieved_at: "2026-09-28T16:24:04+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on September 2026 payrolls shows a near-even split around 90K-100K, consistent with high pre-report uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lewis KrauskopfReuters: Jobs report, inflation data to test US rate path, economic strength th"
    url: "https://www.postandcourier.com/jobs-report-inflation-data-to-test-us-rate-path-economic-strength-this-week/article_4d2a7542-757e-42d2-87ba-37122414e7dc.html"
    published_at: "2026-09-28T04:00:00.000Z"
    retrieved_at: "2026-09-28T16:24:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
