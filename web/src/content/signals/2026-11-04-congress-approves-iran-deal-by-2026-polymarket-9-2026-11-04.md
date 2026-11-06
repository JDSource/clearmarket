---
signal_id: "CMSIG2026110406"
signal_slug: "congress-approves-iran-deal-by-2026-polymarket-9-2026-11-04"
headline: "Congress approves Iran deal by 2026: Polymarket 9%"
semantic_title: "Congress approving an Iran deal by 2026 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-04T13:19:14.000Z"
event_id: "CM-EVT-PB2TWNBNL3"
event_slug: "congress-approves-iran-deal-in-2026-20260616005217959"
event_question: "Will Congress approve an Iran deal by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0665610d8a06655edb83376e45fd8d2dd78889d2b3a1b2668efe398514cf87ae"
  question_raw: "Congress approves Iran deal in 2026?"
  current_price: 0.09
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "Polymarket puts 9% on Congress approving an Iran deal by 2026, a low but non-trivial probability given the new political landscape."
  - "Democrats taking Congress on an anti-war platform adds modest pressure toward a deal, but the market still sees a congressional Iran deal this year as unlikely."
  - "Companion Polymarket contract CM-EVT-WD982793G1 prices a full U.S. invasion of Iran at 12%, suggesting the market sees continued conflict as more likely than a legislative resolution."
  - "Resolves via UMA oracle; the compressed year-end timeline is the main constraint keeping this probability in single digits."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Democrats have won control of Congress after an election largely shaped by the unpopular Iran war, raising questions about Trump's war authority."
    publisher: "The Associated Press"
    published_at: "2026-11-04T13:19:14.000Z"
    source_url: "https://apnews.com/article/midterm-elections-democrats-republicans-trump-b1d26390b7ed7968435089be6d3bf612"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://apnews.com/article/midterm-elections-democrats-republicans-trump-b1d26390b7ed7968435089be6d3bf612"
        retrieved_at: "2026-11-06T15:37:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 9%; market prices a congressional Iran deal as a long shot even as Democrats prepare to take power on a platform defined by the war."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: The Latest: Trump defends Iran war after voters give Democrats control"
    url: "https://apnews.com/article/midterm-elections-democrats-republicans-trump-b1d26390b7ed7968435089be6d3bf612"
    published_at: "2026-11-04T13:19:14.000Z"
    retrieved_at: "2026-11-06T15:37:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
