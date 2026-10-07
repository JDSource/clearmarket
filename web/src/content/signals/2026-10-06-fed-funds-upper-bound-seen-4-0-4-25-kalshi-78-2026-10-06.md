---
signal_id: "CMSIG2026100601"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-78-2026-10-06"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi 78%"
semantic_title: "Fed funds above 4 percent stays near full pricing post-hike collapse"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-06T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 151.41
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 78% above 4.0%, only 19% above 4.25%."
  - "October hike odds fell from 70% to 25% per fed funds futures after Jefferson and Williams signaled pause; Kalshi distribution is consistent with one more hike but not imminent."
  - "The companion Kalshi ladder (CM-EVT-6BS28TS762) prices 99% above 3.75% but only 18% above 4.0%, implying an earlier meeting already priced a hold near 4.0%."
  - "Resolves via Federal Reserve official rate announcement; any dissent or hawkish surprise at the Oct. 27-28 meeting would shift the 4.25% strike sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October Fed hike odds collapsed from 70% to 25% after Vice Chair Philip Jefferson and New York Fed President John Williams signaled a pause."
    publisher: "The Macro, Rates Desk"
    published_at: "2026-10-06T00:00:00.000Z"
    source_url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Macro, Rates Desk"
        source_url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
        retrieved_at: "2026-10-07T15:02:04+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing is consistent with a one-and-done posture: the market agrees with the pause signal from Fed officials but has not fully priced out a final hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Macro, Rates Desk: October Hike Odds Fall to 25% After Fed Deputies Show Pause | Gokhshte"
    url: "https://gokhshtein.com/news/2026-10-06-october-hike-odds-collapse-to-25-as-fed-deputies-show-pause"
    published_at: "2026-10-06T00:00:00.000Z"
    retrieved_at: "2026-10-07T15:02:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
