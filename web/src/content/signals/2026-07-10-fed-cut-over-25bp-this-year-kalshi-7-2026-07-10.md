---
signal_id: "CMSIG2026071002"
signal_slug: "fed-cut-over-25bp-this-year-kalshi-7-2026-07-10"
headline: "Fed cut over 25bp this year: Kalshi 7%"
semantic_title: "Deep cut probability anchors near zero despite inflation alarm"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T19:06:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.07
  volume_24h_usd: 89.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract puts only 7% probability on the Fed delivering a cut larger than 25 basis points at any point in 2026."
  - "The Fed report's explicit inflation warnings from three simultaneous supply and demand shocks are consistent with the market's near-dismissal of aggressive easing."
  - "Read alongside the Kalshi ladder implying the upper bound stays in the 3.50-3.75% range, the market is pricing a prolonged freeze, not a pivot."
  - "Resolves via Federal Reserve announcement; any single meeting with a cut exceeding 25bp triggers resolution, making this sensitive to emergency-action scenarios the market currently prices at just 7%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed's Monetary Policy Report cited stepped-up inflation from tariffs, the Iran war, and AI investment as compounding pressures on the rate outlook."
    publisher: "KitcoNewsNOW"
    published_at: "2026-07-10T19:06:00.000Z"
    source_url: "https://uk.headtopics.com/news/fed-report-cites-stepped-up-inflation-due-to-tariffs-85459584"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "KitcoNewsNOW"
        source_url: "https://uk.headtopics.com/news/fed-report-cites-stepped-up-inflation-due-to-tariffs-85459584"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the Federal Reserve; the 7% price is the market's direct response to the cumulative inflation signals in this reporting cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "KitcoNewsNOW: Fed report cites 'stepped-up' inflation due to tariffs, Iran war, AI b"
    url: "https://uk.headtopics.com/news/fed-report-cites-stepped-up-inflation-due-to-tariffs-85459584"
    published_at: "2026-07-10T19:06:00.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
