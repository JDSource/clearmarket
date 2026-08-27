---
signal_id: "CMSIG2026082602"
signal_slug: "fed-funds-upper-bound-post-meeting-kalshi-ladder-3-5-3-75-2026-08-26"
headline: "Fed funds upper bound post-meeting: Kalshi ladder 3.5-3.75%"
semantic_title: "Fed funds near 3.5 percent after next meeting, market holds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-26T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound following next Fed meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.32
  volume_24h_usd: 245.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 99% odds the upper bound stays above 3.5%, but only 32% above 3.75%, implying consensus at 3.5-3.75%."
  - "Unchanged July PCE inflation at 3.7% and unrevised Q2 GDP of 1.5% support the market's hold-rate pricing."
  - "A companion Kalshi ladder for a later meeting (CM-EVT-MR57HVWJT3) prices 53% above 3.75% and 17% above 4.0%, signaling modest tightening risk in the outer months."
  - "Resolves via the Federal Reserve's official federal funds rate announcement following the relevant FOMC meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "July U.S. inflation held steady at 3.7% annually and Q2 GDP growth was unrevised at a sluggish 1.5%, keeping the Fed on hold."
    publisher: "Reuters Connect"
    published_at: "2026-08-26T00:00:00.000Z"
    source_url: "https://thedailyrecord.com/2026/08/26/us-inflation-steady-july-q2-gdp-growth-unrevised/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters Connect"
        source_url: "https://thedailyrecord.com/2026/08/26/us-inflation-steady-july-q2-gdp-growth-unrevised/"
        retrieved_at: "2026-08-27T18:46:25+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladders together show the market pricing near-term hold at 3.5-3.75% with a small but rising probability of a hike further out."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters Connect: Inflation remains sticky in July; Q2 GDP growth unrevised at 1.5% - Ma"
    url: "https://thedailyrecord.com/2026/08/26/us-inflation-steady-july-q2-gdp-growth-unrevised/"
    published_at: "2026-08-26T00:00:00.000Z"
    retrieved_at: "2026-08-27T18:46:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
