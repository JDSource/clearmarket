---
signal_id: "CMSIG2026070602"
signal_slug: "year-end-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-06"
headline: "Year-end Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Year-end Fed funds consensus anchors in 3.50-3.75 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-06T17:18:51.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound, end-2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.31
  volume_24h_usd: 31.33
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 91% above 3.50 percent but only 31% above 3.75 percent, implying the market-implied upper bound sits in the 3.50-3.75 percent range."
  - "Waller's inflation-first framing aligns with this distribution: the market is not pricing a return to restrictive territory above 4 percent, nor rapid cuts below 3.50 percent."
  - "A companion Kalshi ladder for a nearer horizon shows 98% above 3.50 percent and only 19% above 3.75 percent, suggesting the term structure is nearly flat and the market sees little change between now and year-end."
  - "Resolves via Federal Reserve official rate announcements through the final 2026 FOMC meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller said inflation is now the primary risk, reinforcing a slow-easing path for the federal funds rate."
    publisher: "tradevae.com"
    published_at: "2026-07-06T17:18:51.000Z"
    source_url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradevae.com"
        source_url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
        retrieved_at: "2026-07-08T10:13:38+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the tight 3.50-3.75 percent band reflects broad consensus among prediction market participants despite conflicting Fed signals."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradevae.com: Waller Says Inflation Now the Primary Risk as U.S. Labor Market Stabil"
    url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
    published_at: "2026-07-06T17:18:51.000Z"
    retrieved_at: "2026-07-08T10:13:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
