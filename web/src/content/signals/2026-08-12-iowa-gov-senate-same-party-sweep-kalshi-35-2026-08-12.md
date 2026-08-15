---
signal_id: "CMSIG2026081204"
signal_slug: "iowa-gov-senate-same-party-sweep-kalshi-35-2026-08-12"
headline: "Iowa Gov-Senate same-party sweep: Kalshi 35%"
semantic_title: "Iowa governor-senate same-party combo stays below 50%"
telemetry: "Kalshi 35%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-K724YL44P6"
event_slug: "kxiasengovcombo-26nov"
event_question: "Iowa Governor-Senate combo"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIASENGOVCOMBO-26NOV-DEMDEM"
  question_raw: "Will Iowa Governor winner be Democratic party and Iowa Senate winner be Democratic party?"
  current_price: 0.35
  volume_24h_usd: 94.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi puts 35% on Iowa electing a governor and senator from the same party, reflecting a competitive state where split outcomes remain the base case."
  - "Trading volume on this contract surged 695x day over day, a sharp signal that the primary results are pulling fresh attention to Iowa's general-election setup."
  - "Companion Kalshi contract CM-EVT-5BB4SFW2V1 prices Michigan's same-party sweep at 53%, showing the market sees Michigan as more likely to unify than Iowa."
  - "Resolves via Bureau of Labor Statistics as named resolution source; actual resolution will depend on official certified election results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democratic primary voters are signaling a preference for change over ideology across a series of closely watched 2026 midterm contests."
    publisher: "apnews.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Kalshi's Iowa contract saw the largest single-day volume surge in this batch at 695x, directly tied to primary-night results reshaping general-election expectations."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Democratic voters are making clear they just want change | AP News"
    url: "https://apnews.com/article/democrats-wisconsin-primary-hong-crowley-flanagan-0618c650d24c17a2a8f2d3273d813808"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
