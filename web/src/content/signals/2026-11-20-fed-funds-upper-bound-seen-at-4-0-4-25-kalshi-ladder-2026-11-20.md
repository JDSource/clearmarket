---
signal_id: "CMSIG2026112001"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-20"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4 percent after hike debate"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T20:12:42.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (post-current meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 144.58
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the Fed funds upper bound in the 4.0-4.25% range: 93% above 4.0% but only 4% above 4.25%."
  - "The Fed's internal hike-size debate is consistent with a market pinned just at 4.0-4.25%, not pricing a larger move."
  - "The 4.25% strike at just 4% suggests markets see very little chance the Fed overshoots with a jumbo hike."
  - "Resolution via the Fed's post-meeting statement; ambiguity in timing or interim emergency action could affect settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed spent the week of Nov. 16-20 debating the size of its next rate hike, with officials split on the path forward."
    publisher: "investing.com"
    published_at: "2026-11-20T20:12:42.000Z"
    source_url: "https://www.investing.com/news/stock-market-news/fed-signals-and-data-what-happened-the-week-of-nov-1620-2026-93CH-5042523"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/stock-market-news/fed-signals-and-data-what-happened-the-week-of-nov-1620-2026-93CH-5042523"
        retrieved_at: "2026-11-23T07:47:39+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data implies narrow consensus just below the 4.25% threshold, tracking the week's Fed signals closely."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed signals and data: what happened the week of Nov. 16, 20, 2026 By In"
    url: "https://www.investing.com/news/stock-market-news/fed-signals-and-data-what-happened-the-week-of-nov-1620-2026-93CH-5042523"
    published_at: "2026-11-20T20:12:42.000Z"
    retrieved_at: "2026-11-23T07:47:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
