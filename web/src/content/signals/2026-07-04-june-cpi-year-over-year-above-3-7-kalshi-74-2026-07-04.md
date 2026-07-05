---
signal_id: "CMSIG2026070408"
signal_slug: "june-cpi-year-over-year-above-3-7-kalshi-74-2026-07-04"
headline: "June CPI year-over-year above 3.7%: Kalshi 74%"
semantic_title: "Year-over-year CPI for June seen near 3.7-3.8% in market pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T11:20:00.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "June 2026 CPI year-over-year inflation rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.22
  volume_24h_usd: 774.41
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi ladder implies June 2026 year-over-year CPI in the 3.7-3.8% range: 74% above 3.7% but only 22% above 3.8%, a sharp inflection at 3.8%."
  - "The weak June NFP print of 57,000 jobs and Bitcoin's rate-cut-driven rally are consistent with a market that expects inflation to remain elevated even as growth slows."
  - "A CPI print above 3.7% year over year would confirm the stagflationary backdrop flagged by multiple news sources this week, consistent with the low probability (9%) of an outsized Fed cut (CM-EVT-RWRZ1R3SD6)."
  - "The monthly CPI ladder (CM-EVT-KJ2LGV0M57) implies June monthly CPI near -0.3% to -0.2%, meaning base effects are holding the year-over-year figure elevated even as recent monthly readings soften."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin touched $62,295 on July 5 as weak US payrolls data boosted rate-cut hopes, with the 200-week simple moving average capping the rally."
    publisher: "Ifeanyi Egede"
    published_at: "2026-07-04T11:20:00.000Z"
    source_url: "https://coinnews.com/news/bitcoin-200-week-sma-resistance-jobs-data-rally/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ifeanyi Egede"
        source_url: "https://coinnews.com/news/bitcoin-200-week-sma-resistance-jobs-data-rally/"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the sharp drop in probability above 3.8% defines the market's ceiling for this inflation print, consistent with the broader macro picture this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ifeanyi Egede: Bitcoin Hits 9-Day High but 200-Week SMA Holds as Ceiling"
    url: "https://coinnews.com/news/bitcoin-200-week-sma-resistance-jobs-data-rally/"
    published_at: "2026-07-04T11:20:00.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
