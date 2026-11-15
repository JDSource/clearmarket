---
signal_id: "CMSIG2026111405"
signal_slug: "trump-calls-for-thune-exit-kalshi-7-2026-11-14"
headline: "Trump calls for Thune exit: Kalshi 7%"
semantic_title: "Trump publicly backing Thune ouster stays a long shot at 7%"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-14T12:40:26.000Z"
event_id: "CM-EVT-57VMK4QRS7"
event_slug: "kxtrumpthuneout-27jan01"
event_question: "Will Trump publicly call for John Thune to step down as Senate Majority Leader?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPTHUNEOUT-27JAN01"
  question_raw: "Will Donald Trump issue a statement about explicitly calling for John Thune to resign, step down, be replaced, or be removed from his position as Senate Majority Leader before Jan 1, 2027?"
  current_price: 0.07
  volume_24h_usd: 11.83
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "The Kalshi contract on Trump publicly calling for Senate Majority Leader John Thune to step down sits at 7%."
  - "Democrat leadership turmoil from the Van Hollen challenge dominates the story, while the market sees Trump intervening in Republican Senate leadership as a long shot."
  - "The 7% read suggests the market treats intra-GOP Senate friction as low probability despite the broader midterm upheaval narrative."
  - "Resolves via The Washington Post reporting a public Trump call; ambiguity around what constitutes 'publicly' could matter at the margin."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "NPR reports a Senate leadership battle as Chris Van Hollen challenges Chuck Schumer for top Democrat, reflecting strong midterm turnout by younger and independent voters."
    publisher: "Scott Simon"
    published_at: "2026-11-14T12:40:26.000Z"
    source_url: "https://www.npr.org/2026/11/14/nx-s1-6040156/week-in-politics-battle-for-senate-leader-young-and-independent-midterm-turnout"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott Simon"
        source_url: "https://www.npr.org/2026/11/14/nx-s1-6040156/week-in-politics-battle-for-senate-leader-young-and-independent-midterm-turnout"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 7%; resolves via Washington Post; no intraday move claimed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott Simon: Week in Politics: Battle for Senate leader; young and independent midt"
    url: "https://www.npr.org/2026/11/14/nx-s1-6040156/week-in-politics-battle-for-senate-leader-young-and-independent-midterm-turnout"
    published_at: "2026-11-14T12:40:26.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
