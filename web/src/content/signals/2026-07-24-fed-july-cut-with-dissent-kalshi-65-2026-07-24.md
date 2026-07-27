---
signal_id: "CMSIG2026072403"
signal_slug: "fed-july-cut-with-dissent-kalshi-65-2026-07-24"
headline: "Fed July cut with dissent: Kalshi 65%"
semantic_title: "Fed July rate cut with dissent stays favored at 65 percent"
telemetry: "Kalshi 65%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-P6QJP9BW02"
event_slug: "kxfedcombo-26jul"
event_question: "Will the Federal Reserve in July 2026 cut rates and have at least one dissent?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUL-0-T0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be >0 for Jul 2026?"
  current_price: 0.65
  volume_24h_usd: 801.01
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-29T17:55:00Z"
bullets:
  - "The Kalshi contract puts 65% odds on the Fed cutting rates at the July 2026 meeting with at least one dissent, per Bureau of Labor Statistics resolution."
  - "Services-led growth at a 2.3% pace is consistent with a cut occurring but a dissent being likely, as hawkish members could object to easing into an accelerating economy."
  - "The manufacturing contraction gives dovish members cover to cut, explaining why a cut remains the base case despite strong headline activity."
  - "Companion ladder CM-EVT-MR57HVWJT3 puts only 48% odds on the upper bound exceeding 4.0% after the meeting, so the dominant scenario remains a cut to or hold near current levels, not a hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US private-sector activity accelerated to its fastest quarterly pace in months, driven by a services surge, even as manufacturing entered contraction ahead of the July 28-29 FOMC decision."
    publisher: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT"
        source_url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
        retrieved_at: "2026-07-27T11:15:45+00:00"
  - type: "pm_response"
    notes: "Kalshi at 65% resolves via Bureau of Labor Statistics and captures both the rate decision and the dissent, making it a compound binary sensitive to committee dynamics."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT: Services Surge Pushes US Growth to 2.3% Pace as Factories Enter Contra"
    url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-27T11:15:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
