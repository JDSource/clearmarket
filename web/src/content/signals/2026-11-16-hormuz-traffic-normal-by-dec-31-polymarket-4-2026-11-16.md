---
signal_id: "CMSIG2026111606"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-4-2026-11-16"
headline: "Hormuz traffic normal by Dec 31: Polymarket 4%"
semantic_title: "Strait of Hormuz back to normal by year-end stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.04
  volume_24h_usd: 11865.85
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 4% odds on Strait of Hormuz traffic returning to normal by December 31, 2026, via UMA oracle."
  - "Fresh mine strikes on tankers and a third US carrier deployment directly reinforce the market's near-zero probability of a rapid normalization."
  - "At 4%, the Polymarket contract treats full Hormuz recovery by year-end as a deep tail risk, not a plausible near-term scenario given active hostilities."
  - "Iran nuclear test by 2027 (CM-EVT-YQ6BFV3GX1) prices at 3% and Iran nuclear weapon by 2027 (CM-EVT-RV9Z73GLB0) at 2%, consistent with a market that sees escalation risk but not an imminent strategic breakout."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's IRGC said mines struck two oil tankers in the Strait of Hormuz while a third US carrier arrived in the region."
    publisher: "Usaid Siddiqui, Barbara Angopa"
    published_at: "2026-11-16T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/liveblog/2026/11/16/iran-war-live-tehran-warns-it-may-strike-first-before-another-us-attack"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Usaid Siddiqui, Barbara Angopa"
        source_url: "https://www.aljazeera.com/news/liveblog/2026/11/16/iran-war-live-tehran-warns-it-may-strike-first-before-another-us-attack"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle at December 31, 2026; normalization requires cessation of active IRGC mining operations and US carrier drawdown."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Usaid Siddiqui, Barbara Angopa: Iran war live: Third US carrier arrives, Iran says oil tankers hit min"
    url: "https://www.aljazeera.com/news/liveblog/2026/11/16/iran-war-live-tehran-warns-it-may-strike-first-before-another-us-attack"
    published_at: "2026-11-16T00:00:00.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
