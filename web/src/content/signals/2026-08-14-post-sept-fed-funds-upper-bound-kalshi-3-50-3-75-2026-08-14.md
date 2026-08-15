---
signal_id: "CMSIG2026081401"
signal_slug: "post-sept-fed-funds-upper-bound-kalshi-3-50-3-75-2026-08-14"
headline: "Post-Sept Fed funds upper bound: Kalshi 3.50-3.75%"
semantic_title: "Fed funds rate seen holding near 3.50-3.75% after September"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T17:59:28.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Post-September 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.26
  volume_24h_usd: 3042.14
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the post-September Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50%, only 26% above 3.75%."
  - "News reports a market consensus for a September pause; the Kalshi distribution is consistent, showing near-zero probability of rates at 4.0% or above."
  - "Jackson Hole in two weeks is the next catalyst; the sharp drop from 98% to 26% between the 3.50% and 3.75% strikes signals the market sees the current range as the likely landing zone."
  - "Companion Kalshi contract CM-EVT-P1KKDFWZ42 puts only 50% on any Fed rate hike across the full 2026-2028 series, reflecting deep uncertainty beyond the near-term hold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Markets are betting on a Fed pause in September ahead of Jackson Hole, even as hawk officials resist cutting amid sticky inflation."
    publisher: "uk.finance.yahoo.com"
    published_at: "2026-08-14T17:59:28.000Z"
    source_url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "uk.finance.yahoo.com"
        source_url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing is consistent with the reported pause consensus and leaves virtually no probability mass above 4.0%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "uk.finance.yahoo.com: Markets bet on a pause for September, but Fed hawks may not be swayed"
    url: "https://uk.finance.yahoo.com/news/markets-bet-on-a-pause-for-september-but-fed-hawks-may-not-be-swayed-ahead-of-jackson-hole-175928197.html"
    published_at: "2026-08-14T17:59:28.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
