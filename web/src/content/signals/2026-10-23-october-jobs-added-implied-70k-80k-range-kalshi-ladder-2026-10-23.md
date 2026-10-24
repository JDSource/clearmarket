---
signal_id: "CMSIG2026102302"
signal_slug: "october-jobs-added-implied-70k-80k-range-kalshi-ladder-2026-10-23"
headline: "October jobs added, implied 70K-80K range: Kalshi ladder"
semantic_title: "October payrolls outlook stays well above actual print"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-23T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 4.5
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder market-implied range is 70,000-80,000 jobs for October, with 51% pricing above 70,000 and 45% above 80,000."
  - "The reported 29,000 print sits far below the ladder's modal range, indicating the market had not priced in such a sharp miss before the report."
  - "The 94% probability above -25,000 and 85% above zero are consistent with the positive print, but the distribution still badly overestimates actual job creation."
  - "The companion unemployment rate ladder (CM-EVT-2X91TW50H2) prices 68% above 4.1%, consistent with the report's noted uptick in unemployment."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The October payrolls report showed only 29,000 jobs added and a rising unemployment rate, sharply below consensus expectations."
    publisher: "Amelia Northam"
    published_at: "2026-10-23T00:00:00.000Z"
    source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amelia Northam"
        source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
        retrieved_at: "2026-10-24T12:26:12+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder resolves via the Bureau of Labor Statistics Employment Situation release; the wide gap between the market-implied median and the actual 29,000 print illustrates the ladder was positioned for a much stronger labor market outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amelia Northam: Weak October US payrolls (+29,000) and rising unemployment reshape mar"
    url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    published_at: "2026-10-23T00:00:00.000Z"
    retrieved_at: "2026-10-24T12:26:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
