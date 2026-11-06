---
signal_id: "CMSIG2026110601"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-06"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds above 4 percent stays a long shot after jobs beat"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T13:53:25.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (post-year-end)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 198.43
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 4.00-4.25% range, with 78% pricing above 4.00% but only 2% above 4.25%."
  - "News calls a December hike 'in play,' but the ladder puts essentially zero odds above 4.25%, suggesting the market is not pricing an aggressive hiking path."
  - "Companion Kalshi contract CM-EVT-RWRZ1R3SD6 puts only 3% on a cut greater than 25 basis points this year, consistent with a Fed on hold rather than actively hiking."
  - "Resolution via Federal Reserve policy announcement; the sharp cutoff above 4.25% implies traders see one move as the ceiling, not a resumed hike cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A blowout October jobs report showing 165,000 payrolls added and unemployment at 4.1% has headlines flagging a December Fed rate hike as back in play."
    publisher: "Jennifer Schonberger"
    published_at: "2026-11-06T13:53:25.000Z"
    source_url: "https://finance.yahoo.com/economy/policy/article/blockbuster-october-jobs-report-keeps-fed-rate-hike-in-play-for-december-135325070.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jennifer Schonberger"
        source_url: "https://finance.yahoo.com/economy/policy/article/blockbuster-october-jobs-report-keeps-fed-rate-hike-in-play-for-december-135325070.html"
        retrieved_at: "2026-11-06T15:37:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data provided; market implies a ceiling near 4.25%, not validating the 'hike back in play' framing from headlines."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jennifer Schonberger: Blockbuster October jobs report keeps Fed rate hike in play for Decemb"
    url: "https://finance.yahoo.com/economy/policy/article/blockbuster-october-jobs-report-keeps-fed-rate-hike-in-play-for-december-135325070.html"
    published_at: "2026-11-06T13:53:25.000Z"
    retrieved_at: "2026-11-06T15:37:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
