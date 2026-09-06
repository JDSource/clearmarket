---
signal_id: "CMSIG2026090304"
signal_slug: "fed-raises-rates-in-2026-polymarket-71-2026-09-03"
headline: "Fed raises rates in 2026: Polymarket 71%"
semantic_title: "Fed hike in 2026 builds toward 75% on strong jobs data"
telemetry: "Polymarket 71%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-03T00:00:00.000Z"
event_id: "CM-EVT-87QV1G78C4"
event_slug: "fed-rate-hike-in-2026"
event_question: "Will the Federal Reserve raise its benchmark interest rate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x80b3af88cb991980e8da1ce86b9794a0957f96ec98c29319dd7ba65e9744d82b"
  question_raw: "Fed rate hike in 2026?"
  current_price: 0.71
  volume_24h_usd: 4861.095019
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket prices 71% on the Fed raising its benchmark rate at some point in 2026, resolving via UMA oracle."
  - "Waller's pre-jobs-report hedging is at mild odds with the 71% market reading, suggesting prediction markets are pricing the data more than the rhetoric."
  - "Rate-level ladder (CM-EVT-4ZQLQPNH91) puts only 2% on the fed funds upper bound exceeding 4.0%, implying markets expect a hike but a shallow one."
  - "Kalshi's multi-deadline series (CM-EVT-P1KKDFWZ42) is at 74%, nearly matching Polymarket's 71%, a tight cross-venue alignment with no meaningful gap to exploit."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Fed Governor Christopher Waller signaled ambiguity on a September rate hike even before the August payroll beat, with inflation data now the key remaining hurdle."
    publisher: "CHRISTOPHER RUGABER Associated Press Associated Press"
    published_at: "2026-09-03T00:00:00.000Z"
    source_url: "https://www.local10.com/business/2026/09/03/will-federal-reserve-hike-rates-later-this-month-waller-muddies-the-outlook/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CHRISTOPHER RUGABER Associated Press Associated Press"
        source_url: "https://www.local10.com/business/2026/09/03/will-federal-reserve-hike-rates-later-this-month-waller-muddies-the-outlook/"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on any Fed rate increase in calendar 2026; cross-venue alignment with Kalshi at 74% is unusually tight."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CHRISTOPHER RUGABER Associated Press Associated Press: Will Federal Reserve hike rates later this month? Waller muddies the o"
    url: "https://www.local10.com/business/2026/09/03/will-federal-reserve-hike-rates-later-this-month-waller-muddies-the-outlook/"
    published_at: "2026-09-03T00:00:00.000Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
