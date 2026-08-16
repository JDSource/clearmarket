---
signal_id: "CMSIG2026081401"
signal_slug: "sept-fed-funds-upper-bound-kalshi-3-50-3-75-implied-2026-08-14"
headline: "Sept Fed funds upper bound: Kalshi 3.50-3.75% implied"
semantic_title: "Fed funds upper bound seen holding at 3.50-3.75%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T17:59:28.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound following next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.26
  volume_24h_usd: 657.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the post-decision Fed funds upper bound in the 3.50-3.75% range: 98% chance above 3.50%, only 26% above 3.75%."
  - "News reports hawks may resist a pause at Jackson Hole, but the distribution shows no meaningful probability above 4.00%, consistent with a market holding firmly to a hold."
  - "Separately, the Kalshi contract on whether the Fed raises rates at all (multi-deadline series, 2026-2028) sits at 48%, suggesting rate-hike risk is fully priced into a longer horizon, not September."
  - "Resolution tracks the actual upper bound target set by the Federal Reserve following its next policy decision."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Markets are pricing a September Fed pause as cooling inflation and soft spending data dominate ahead of Jackson Hole, though Fed hawks may resist."
    publisher: "uk.finance.yahoo.com"
    published_at: "2026-08-14T17:59:28.000Z"
    source_url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "uk.finance.yahoo.com"
        source_url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covering the post-decision Fed funds upper bound shows a tightly clustered consensus around 3.50-3.75%, with the tail above 3.75% priced at just 26%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "uk.finance.yahoo.com: Markets bet on a pause for September, but Fed hawks may not be swayed"
    url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
    published_at: "2026-08-14T17:59:28.000Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
