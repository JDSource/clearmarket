---
signal_id: "CMSIG2026102603"
signal_slug: "democrats-win-us-house-kalshi-90-2026-10-26"
headline: "Democrats win US House: Kalshi 90%"
semantic_title: "Democrats heavily favored to win the US House in 2026 midterms"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.903
  volume_24h_usd: 444489.88
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts Democrats winning the US House at 90%, a strong consensus lean one week before Election Day."
  - "News analysis describing a Democratic wave environment is consistent with the 90% Kalshi read; no price move can be confirmed from available data."
  - "A companion Polymarket contract (CM-EVT-M9WJY06T90) prices Democratic Senate control at 66%, suggesting the market sees the House as a safer flip than the Senate."
  - "Resolution via Library of Congress; the House contract resolves on certified seat counts, not election-night calls, which can add a lag if results are contested."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Washington Post analysis previews the November 3 midterm elections, noting that control of Congress could swing to Democrats in both chambers."
    publisher: "Amber Phillips"
    published_at: "2026-10-26T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amber Phillips"
        source_url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on House control resolves via Library of Congress and is trading at 90% in favor of Democrats, with the Senate contract on Polymarket showing a wider band of uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amber Phillips: What to expect in next week’s midterm elections - The Washington Post"
    url: "https://www.washingtonpost.com/politics/2026/10/26/what-expect-next-weeks-midterm-elections/"
    published_at: "2026-10-26T00:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
