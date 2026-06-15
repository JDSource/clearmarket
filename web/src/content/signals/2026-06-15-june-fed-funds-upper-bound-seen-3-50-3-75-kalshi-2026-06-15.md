---
signal_id: "CMSIG2026061505"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-15"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound seen at 3.5 to 3.75 percent after June meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-15T10:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder prices the June 2026 Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 36% above 3.75%."
  - "A rate hold at the June meeting is consistent with this distribution, as the implied rate sits below the current 4.25-4.50% bound cited in the news, reflecting prior cuts already priced."
  - "The dissent contract on Kalshi at 67% suggests markets see the June decision as contentious even if the rate level itself is not in dispute."
  - "The longer-horizon ladder showing only 8% above 4.25% confirms markets have fully priced out a return to the prior rate regime through this cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed is expected to hold rates steady at its June meeting as May CPI spiked to 4.2% and rate hike talk intensifies."
    publisher: "Jennifer Schonberger     ·  Senior Reporter     Mon 15 June 2026 at 8:00 pm GMT+10   6 min read"
    published_at: "2026-06-15T10:00:00.000Z"
    source_url: "https://uk.finance.yahoo.com/news/fed-expected-to-hold-rates-steady-this-week-as-rate-hike-talks-heat-up-and-us-strikes-a-deal-with-iran-100000734.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jennifer Schonberger     ·  Senior Reporter     Mon 15 June 2026 at 8:00 pm GMT+10   6 min read"
        source_url: "https://uk.finance.yahoo.com/news/fed-expected-to-hold-rates-steady-this-week-as-rate-hike-talks-heat-up-and-us-strikes-a-deal-with-iran-100000734.html"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution reflects a market that has already priced substantial prior easing; the June hold narrative is consistent with but does not shift the implied rate range."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jennifer Schonberger     ·  Senior Reporter     Mon 15 June 2026 at 8:00 pm GMT+10   6 min read: Fed expected to hold rates steady this week as rate hike talks heat up"
    url: "https://uk.finance.yahoo.com/news/fed-expected-to-hold-rates-steady-this-week-as-rate-hike-talks-heat-up-and-us-strikes-a-deal-with-iran-100000734.html"
    published_at: "2026-06-15T10:00:00.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
