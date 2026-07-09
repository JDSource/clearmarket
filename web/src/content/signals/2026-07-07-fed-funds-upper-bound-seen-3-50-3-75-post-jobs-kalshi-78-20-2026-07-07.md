---
signal_id: "CMSIG2026070703"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-post-jobs-kalshi-78-20-2026-07-07"
headline: "Fed funds upper bound seen 3.50-3.75% post-jobs: Kalshi 78%/20%"
semantic_title: "Rate path consensus fractures as jobs shock hits pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-07T20:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound (mid-2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.2
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder prices 78% above 3.50% but only 20% above 3.75%, implying the market's modal rate path sits in the 3.50-3.75% range."
  - "A 57,000-job print is consistent with rate-cut pressure, yet the market is not pricing aggressive easing; the 78% above 3.50% shows no collapse in the rate floor."
  - "The weak labor market competes with persistent tariff-driven inflation concerns from the Fed minutes, creating the divided distribution seen in the Kalshi ladder."
  - "Resolves via the Federal Reserve's official rate announcement at the relevant 2026 FOMC meeting; labor data is a key input but Fed reaction function remains uncertain given divided minutes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The June jobs report showed only 57,000 nonfarm payrolls added, far below consensus, with downward revisions cutting 74,000 jobs from prior months."
    publisher: "Maryann Pugh"
    published_at: "2026-07-07T20:00:00.000Z"
    source_url: "https://www.mychesco.com/a/news/national/us-job-growth-misses-forecasts-as-hiring-momentum-slows/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Maryann Pugh"
        source_url: "https://www.mychesco.com/a/news/national/us-job-growth-misses-forecasts-as-hiring-momentum-slows/"
        retrieved_at: "2026-07-09T10:56:21+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; the bifurcated distribution reflects the tension between soft labor data and elevated inflation concerns flagged in Fed minutes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Maryann Pugh: US Job Growth Misses Forecasts as Hiring Momentum Slows - MyChesCo"
    url: "https://www.mychesco.com/a/news/national/us-job-growth-misses-forecasts-as-hiring-momentum-slows/"
    published_at: "2026-07-07T20:00:00.000Z"
    retrieved_at: "2026-07-09T10:56:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
