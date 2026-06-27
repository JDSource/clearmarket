---
signal_id: "CMSIG2026062602"
signal_slug: "fed-funds-upper-bound-after-next-meeting-kalshi-3-75-4-0-2026-06-26"
headline: "Fed funds upper bound after next meeting: Kalshi 3.75-4.0%"
semantic_title: "Fed funds upper bound anchors at 3.75 to 4 percent post-hike talk"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 37.75
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.75-4.0% range: 56% chance above 3.75%, only 8% above 4.0%."
  - "Sticky 4.1% PCE aligns with the market pricing a July pause but leaving the door open for a September hike."
  - "Companion Kalshi ladder for a later meeting (CM-EVT-PHWX2H6DM5) shows upper bound implied near 3.50-3.75%, suggesting the market sees rate pressure as temporary, not a sustained hiking cycle."
  - "Resolves via the Federal Reserve's official post-meeting rate announcement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Sticky PCE inflation at a 3-year high keeps a potential September Fed rate hike in market discussion despite a near-certain July pause."
    publisher: "Anupam Nagar"
    published_at: "2026-06-26T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-sticky-inflation-keeps-september-fed-rate-hike-on-table-despite-july-pause-expectations/articleshow/132006583.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anupam Nagar"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-sticky-inflation-keeps-september-fed-rate-hike-on-table-despite-july-pause-expectations/articleshow/132006583.cms"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder distribution shows consensus clustered just below 4.0%, with the PCE print consistent with but not accelerating the hike narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anupam Nagar: US Stock Market: Sticky inflation keeps September Fed rate hike on tab"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-sticky-inflation-keeps-september-fed-rate-hike-on-table-despite-july-pause-expectations/articleshow/132006583.cms"
    published_at: "2026-06-26T00:00:00.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
