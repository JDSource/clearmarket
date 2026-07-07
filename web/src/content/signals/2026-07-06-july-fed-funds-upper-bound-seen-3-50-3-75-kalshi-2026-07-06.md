---
signal_id: "CMSIG2026070601"
signal_slug: "july-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-06"
headline: "July Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "July Fed hike pricing wavers below 4 percent upper bound"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-06T17:18:51.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the July 2026 Fed funds upper bound in the 3.50-3.75% range: 91% chance above 3.50%, only 29% above 3.75%."
  - "Waller's hawkish Rome remarks are consistent with the ladder's 3.50-3.75% modal read, but markets are not fully pricing a hike to 4% or above."
  - "The sharp drop from 91% to 29% between the 3.50% and 3.75% strikes signals meaningful uncertainty about whether the Fed actually pulls the trigger above current levels."
  - "A companion Kalshi contract puts only 10% on a rate cut greater than 25 basis points this year, reinforcing that the dominant scenario is hold or modest hike, not easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller told a Rome economics conference that inflation has replaced labor-market weakness as the central bank's primary risk, signaling openness to a July rate hike."
    publisher: "tradevae.com"
    published_at: "2026-07-06T17:18:51.000Z"
    source_url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradevae.com"
        source_url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the July 2026 FOMC decision; the 3.75% strike at 29% is the key threshold separating the base case from a full hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradevae.com: Waller Says Inflation Now the Primary Risk as U.S. Labor Market Stabil"
    url: "http://www.tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-us-labor-market-stabilizes/"
    published_at: "2026-07-06T17:18:51.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
