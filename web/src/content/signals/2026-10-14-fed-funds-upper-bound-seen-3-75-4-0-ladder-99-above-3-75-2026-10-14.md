---
signal_id: "CMSIG2026101403"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-ladder-99-above-3-75-2026-10-14"
headline: "Fed funds upper bound seen 3.75-4.0%: ladder 99% above 3.75%"
semantic_title: "Fed funds upper bound seen at 3.75-4.0% after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound (post-meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.22
  volume_24h_usd: 3411.77
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Prediction market ladder prices the federal funds upper bound in the 3.75-4.0% range, with 99% probability above 3.75% but only 22% above 4.0%."
  - "Dollar hitting an 18-month high on rate-hike expectations is directionally consistent with the ladder, though the market stops well short of pricing 4.25% or higher."
  - "Trading volume on this contract rose 86.5x day-over-day, reflecting sharp new positioning following the September CPI print of 3.7%."
  - "The Kalshi contract on Fed cuts before 2027 (CM-EVT-X2TT2M9D02) sitting at 6% reinforces the ladder: no relief priced, but aggressive further hikes also not the base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Hot September CPI and dollar strength boosted expectations for a Fed rate hike, with markets assessing the likely terminal rate."
    publisher: "Reuters"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
        retrieved_at: "2026-10-15T07:47:47+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder saw 86.5x normal daily volume after the CPI release, with the 4.0% strike as the clear inflection point in the distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Dollar hits fresh 18-month high as hot inflation boosts Fed hike expec"
    url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-15T07:47:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
