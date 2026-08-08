---
signal_id: "CMSIG2026080703"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-ladder-2026-08-07"
headline: "Fed funds upper bound seen 3.50-3.75%: ladder"
semantic_title: "Fed funds upper bound firmly priced at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T09:34:14.933Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 15635.07
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Ladder prices 98% above 3.50% but only 34% above 3.75%, implying the upper bound is firmly expected in the 3.50-3.75% range."
  - "Record equity close and fading rate-hike bets align with the ladder's sharp drop at the 3.75% strike."
  - "The 1% probability above 4.00% shows virtually no pricing for resumed hikes near-term, consistent with the weak July payroll data."
  - "Resolves via the Federal Reserve's published policy rate decision; next FOMC meeting outcome is the settlement trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The S&P 500 closed at a record high after the soft jobs report eased rate-hike concerns."
    publisher: "The Globe and Mail"
    published_at: "2026-08-07T09:34:14.933Z"
    source_url: "https://www.theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-stocks-dollar-stall-ahead-of-us-jobs-data-oil-gains-as-gulf/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Globe and Mail"
        source_url: "https://www.theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-stocks-dollar-stall-ahead-of-us-jobs-data-oil-gains-as-gulf/"
        retrieved_at: "2026-08-08T08:35:11+00:00"
  - type: "pm_response"
    notes: "Ladder distribution via ClearMarket reference layer; the sharp cliff at 3.75% is the key market read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Globe and Mail: TSX and S&P 500 close at record highs as Fed rate-hike bets ebb"
    url: "https://www.theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-stocks-dollar-stall-ahead-of-us-jobs-data-oil-gains-as-gulf/"
    published_at: "2026-08-07T09:34:14.933Z"
    retrieved_at: "2026-08-08T08:35:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
