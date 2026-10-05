---
signal_id: "CMSIG2026100507"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-20-2026-10-05"
headline: "Hormuz traffic normal by Dec 31: Polymarket 20%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.2
  volume_24h_usd: 44033.753841
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket assigns only 20% probability to Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Iran's seven-condition ultimatum for reopening the strait, reported alongside active US military strikes on Iranian targets, is consistent with the market's heavily skeptical pricing."
  - "Simultaneous reports of US-Iran ceasefire talks in Switzerland (Stories 25-26) have not moved the needle toward the optimistic scenario, per the 20% read."
  - "Resolution requires traffic to resume at pre-closure levels; any remaining Iranian blockade condition or continued military activity would sustain the NO outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran declared the Strait of Hormuz will remain closed until seven conditions are met, even as the US conducted heavy strikes on Iranian targets and high-level ceasefire talks opened in Switzerland."
    publisher: "news.theonlinecitizen.com"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://news.theonlinecitizen.com/2026/10/05/iran-says-strait-of-hormuz-will-stay-shut-until-its-seven-conditions-are-met"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "news.theonlinecitizen.com"
        source_url: "https://news.theonlinecitizen.com/2026/10/05/iran-says-strait-of-hormuz-will-stay-shut-until-its-seven-conditions-are-met"
        retrieved_at: "2026-10-05T07:47:16+00:00"
  - type: "pm_response"
    notes: "Polymarket at 20%; market prices the Hormuz reopening as a long shot despite concurrent diplomatic talks, reflecting the active-conflict backdrop."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "news.theonlinecitizen.com: Iran says Strait of Hormuz will stay shut until its seven conditions a"
    url: "https://news.theonlinecitizen.com/2026/10/05/iran-says-strait-of-hormuz-will-stay-shut-until-its-seven-conditions-are-met"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T07:47:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
