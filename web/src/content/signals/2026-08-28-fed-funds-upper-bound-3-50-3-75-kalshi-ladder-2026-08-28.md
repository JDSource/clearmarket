---
signal_id: "CMSIG2026082801"
signal_slug: "fed-funds-upper-bound-3-50-3-75-kalshi-ladder-2026-08-28"
headline: "Fed funds upper bound 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 3.75% after Jackson Hole"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.47
  volume_24h_usd: 24761.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 3.50-3.75% range: 98% above 3.50%, but only 47% above 3.75%, with trading volume up over 1,100x day over day."
  - "Warsh's price-first messaging at Jackson Hole is consistent with the ladder's sharp break above 3.75%, where probability collapses to 2%."
  - "The volume surge signals Warsh's speech is drawing intense fresh attention to the near-term rate path."
  - "The Kalshi contract resolves via Federal Reserve official rate decisions; any September hike would shift the upper bound and reprice the full ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh emphasized price stability as the Fed's top priority at Jackson Hole, signaling potential rate hikes amid persistent inflation."
    publisher: "newsweek.com"
    published_at: "2026-08-28T00:00:00.000Z"
    source_url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsweek.com"
        source_url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
        retrieved_at: "2026-08-29T13:34:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the federal funds upper bound saw trading volume rise over 1,100x day over day, the dominant rate-path signal post-Jackson Hole."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsweek.com: Fed chair focuses on prices after US economy sheds more jobs than thou"
    url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
    published_at: "2026-08-28T00:00:00.000Z"
    retrieved_at: "2026-08-29T13:34:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
