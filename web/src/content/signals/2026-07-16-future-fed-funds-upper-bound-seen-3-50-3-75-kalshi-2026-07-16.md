---
signal_id: "CMSIG2026071604"
signal_slug: "future-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-16"
headline: "Future Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Later-meeting Fed funds range anchors near 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Future Fed funds upper bound (post-June meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.28
  volume_24h_usd: 39.35
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 95% above 3.50% and only 28% above 3.75%, placing the market-implied Fed funds upper bound in the 3.50-3.75% range for this later horizon."
  - "Resilient ex-gas retail spending supports the view that the economy does not need emergency rate relief, consistent with the market holding above 3.50%."
  - "The 28% probability above 3.75% is notably wider than the near-term June contract (6% above 3.75%), suggesting some residual uncertainty about whether tightening resumes later."
  - "Comparing this ladder to the June meeting ladder (CM-EVT-PHWX2H6DM5, 6% above 3.75%) reveals a modest term-structure premium for the later horizon."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Lower gasoline prices restrained June retail sales to a 0.2% gain, but ex-gas spending was resilient, prompting economists to upgrade Q2 GDP estimates."
    publisher: "AOL"
    published_at: "2026-07-16T00:00:00.000Z"
    source_url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
        retrieved_at: "2026-07-19T09:48:56+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the distribution is broader than the June meeting contract, reflecting greater uncertainty at the longer horizon."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Lower gasoline prices restrain US retail sales, underlying momentum re"
    url: "https://www.aol.com/articles/us-retail-sales-rise-marginally-124340000.html"
    published_at: "2026-07-16T00:00:00.000Z"
    retrieved_at: "2026-07-19T09:48:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
