---
signal_id: "CMSIG2026091803"
signal_slug: "republican-senate-control-in-2026-polymarket-61-2026-09-18"
headline: "Republican Senate control in 2026: Polymarket 61%"
semantic_title: "Republican Senate control holds above 50% as early voting starts"
telemetry: "Polymarket 61%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.61
  volume_24h_usd: 47364.73740499999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract prices Republican Senate control at 61%, a modest but clear lean toward the GOP with weeks remaining before November."
  - "Early voting has begun; the market is slightly above 50%, suggesting the race is genuinely competitive despite a Republican edge."
  - "The Kalshi contract on Republicans controlling at least one chamber of Congress sits at 59%, consistent with the Senate-specific Polymarket read."
  - "Resolves via uma_oracle based on official election results; redistricting complexity and the Trump/Fed rate controversy may be live variables into Election Day."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Early in-person midterm voting began September 18, 2026, with control of Congress at stake following an unprecedented wave of mid-decade redistricting."
    publisher: "The Associated Press Associated Press Associated Press"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.local10.com/news/2026/09/18/the-latest-early-midterm-voting-gets-underway-with-control-of-congress-at-stake/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press Associated Press Associated Press"
        source_url: "https://www.local10.com/news/2026/09/18/the-latest-early-midterm-voting-gets-underway-with-control-of-congress-at-stake/"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "Polymarket at 61% and Kalshi at 59% across two related contracts present a coherent picture of a modest but not decisive Republican advantage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press Associated Press Associated Press: The Latest: Early midterm voting gets underway with control of Congres"
    url: "https://www.local10.com/news/2026/09/18/the-latest-early-midterm-voting-gets-underway-with-control-of-congress-at-stake/"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
