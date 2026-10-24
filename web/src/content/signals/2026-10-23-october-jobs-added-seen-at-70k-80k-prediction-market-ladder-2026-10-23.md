---
signal_id: "CMSIG2026102302"
signal_slug: "october-jobs-added-seen-at-70k-80k-prediction-market-ladder-2026-10-23"
headline: "October jobs added seen at 70K-80K: prediction market ladder"
semantic_title: "October payrolls market-implied range stays well above actual print"
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
  - "The prediction market ladder implies an October payrolls range of 70,000-80,000: 51% above 70K, only 45% above 80K."
  - "The reported 29,000 print sits well below the ladder's modal range, meaning the market was significantly more optimistic than the actual outcome."
  - "The Kalshi rate-hike path (CM-EVT-MR57HVWJT3) still prices 96% above 3.75% for the upper bound, suggesting markets are not yet fully revising the Fed tightening outlook despite the weak jobs number."
  - "Resolution is via the Bureau of Labor Statistics Employment Situation report; benchmark revisions could shift the final settled figure above or below the initial 29K print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The October payrolls report showed just 29,000 jobs added and a rising unemployment rate, sharply below consensus expectations."
    publisher: "Amelia Northam"
    published_at: "2026-10-23T00:00:00.000Z"
    source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amelia Northam"
        source_url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
        retrieved_at: "2026-10-24T07:48:16+00:00"
  - type: "pm_response"
    notes: "The prediction market ladder was positioned far above the actual payrolls print, reflecting a significant miss that had not been priced ahead of the release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amelia Northam: Weak October US payrolls (+29,000) and rising unemployment reshape mar"
    url: "https://quantumnova.tech/news/us-job-growth-slowed-sharply-in-october-as-unemployment-ticked-up-weighing-on-markets-and-fed-outlook"
    published_at: "2026-10-23T00:00:00.000Z"
    retrieved_at: "2026-10-24T07:48:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
