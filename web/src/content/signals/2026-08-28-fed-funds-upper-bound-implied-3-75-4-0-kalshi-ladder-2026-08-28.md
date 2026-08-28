---
signal_id: "CMSIG2026082803"
signal_slug: "fed-funds-upper-bound-implied-3-75-4-0-kalshi-ladder-2026-08-28"
headline: "Fed funds upper bound implied 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound post-next decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 102.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.0% range: 50% above 3.75% but only 1% above 4.0%."
  - "Warsh's focus on inflation over employment suggests the market-implied rate near 3.75-4.0% could shift higher if price data stays elevated."
  - "The sharp drop from 50% at 3.75% to 1% at 4.0% shows the market treats 4.0% as a tail outcome despite Warsh's hawkish rhetoric."
  - "Combined with the 68% Polymarket hike probability, the ladder implies the expected hike would land the rate in the 3.75-4.0% zone, not above."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh emphasized price stability as the Fed's priority after the US economy shed more jobs than previously estimated."
    publisher: "newsweek.com"
    published_at: "2026-08-28T00:00:00.000Z"
    source_url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsweek.com"
        source_url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
        retrieved_at: "2026-08-28T19:51:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder distribution shows a tightly clustered consensus around 3.75-4.0%, with the 4.0% level acting as a hard ceiling in current pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsweek.com: Fed chair focuses on prices after US economy sheds more jobs than thou"
    url: "https://www.newsweek.com/fed-chair-focuses-on-prices-after-us-economy-sheds-more-jobs-than-thought-12380513"
    published_at: "2026-08-28T00:00:00.000Z"
    retrieved_at: "2026-08-28T19:51:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
