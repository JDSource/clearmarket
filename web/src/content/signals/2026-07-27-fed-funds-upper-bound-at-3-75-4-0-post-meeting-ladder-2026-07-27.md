---
signal_id: "CMSIG2026072702"
signal_slug: "fed-funds-upper-bound-at-3-75-4-0-post-meeting-ladder-2026-07-27"
headline: "Fed funds upper bound at 3.75-4.0% post-meeting: ladder"
semantic_title: "September hike odds build as July hold nears consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Post-July-meeting Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.23
  volume_24h_usd: 8.05
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Ladder puts the post-meeting upper bound most likely in the 3.75-4.0% range: 74% above 3.75% but only 23% above 4.0%."
  - "Analyst commentary pointing to an Iran/oil-driven hold is consistent with the ladder centering near 3.75%, not a hike to 4.0% or above."
  - "The 23% probability above 4.0% reflects a residual hike tail, not a base case, despite hawkish analyst posturing."
  - "Kalshi contract CM-EVT-RWRZ1R3SD6 prices only 8% on a cut greater than 25 basis points this year, confirming the broader tightening-bias regime."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street analysts including Warsh watchers flagged oil prices and Iran tensions as reasons the FOMC may hold in July but signal a September hike."
    publisher: "Eleanor Pringle"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://fortune.com/2026/07/27/iran-oil-prices-fed-meeting-inflation-interest-rates-wall-street/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eleanor Pringle"
        source_url: "https://fortune.com/2026/07/27/iran-oil-prices-fed-meeting-inflation-interest-rates-wall-street/"
        retrieved_at: "2026-07-28T10:30:26+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via the Fed's post-meeting rate announcement; the sharp cliff from 74% to 23% between 3.75% and 4.0% is the key pricing signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eleanor Pringle: Wall Street analysts: Warsh and FOMC likely hold or hike due to oil pr"
    url: "https://fortune.com/2026/07/27/iran-oil-prices-fed-meeting-inflation-interest-rates-wall-street/"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-28T10:30:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
