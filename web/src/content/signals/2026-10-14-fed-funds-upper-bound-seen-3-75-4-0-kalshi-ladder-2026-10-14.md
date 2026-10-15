---
signal_id: "CMSIG2026101404"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-10-14"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound near 3.75-4.0 percent, hike beyond heavily discounted"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 3602.26
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound at 99% above 3.75% but only 29% above 4.0%, pinning the market-implied peak at 3.75-4.0%."
  - "Volume surged 86.5x day-over-day on this ladder, confirming the hot CPI print is driving direct repricing activity in rate markets."
  - "The sharp collapse from 99% at 3.75% to 29% at 4.0% shows the market sees a hike to 4.0%+ as unlikely despite hawkish news flow."
  - "The companion Kalshi contract on a Fed cut before 2027 (CM-EVT-X2TT2M9D02) sits at 3%, consistent with a hold-at-peak rather than hike-then-cut regime."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Hot CPI and rising Fed rate hike expectations drove the dollar to an 18-month high, with traders watching for timing signals on the next rate move."
    publisher: "Reuters"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
        retrieved_at: "2026-10-15T13:02:56+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder with 86.5x volume surge; resolves via unspecified source tracking Fed policy decisions; distribution implies peak at current or one-step-higher level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Dollar hits fresh 18-month high as hot inflation boosts Fed hike expec"
    url: "https://www.cnbc.com/2026/10/14/dollar-languishes-as-focus-turns-to-cpi-fed-speakers.html"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-15T13:02:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
