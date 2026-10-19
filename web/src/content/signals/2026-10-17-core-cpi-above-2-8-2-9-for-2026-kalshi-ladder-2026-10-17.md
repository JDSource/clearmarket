---
signal_id: "CMSIG2026101701"
signal_slug: "core-cpi-above-2-8-2-9-for-2026-kalshi-ladder-2026-10-17"
headline: "Core CPI above 2.8-2.9% for 2026: Kalshi ladder"
semantic_title: "Core CPI for 2026 stays above 2 percent near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T08:00:08.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "2026 annual core CPI rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.37
  volume_24h_usd: 17.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder pins 2026 annual core CPI in the 2.8-2.9% range: 57% above 2.8%, 37% above 2.9%, sharp drop to 23% above 3.0%."
  - "News flags slow progress toward the Fed's 2% target; Kalshi distribution is consistent, placing the modal outcome well above target."
  - "The 99% probability above 2.0% means markets treat a return to target in 2026 as essentially impossible."
  - "Separately, the Kalshi binary on core CPI falling below 2.2% in 2026 sits at just 8%, reinforcing the ladder's above-target read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US earnings season and upcoming economic reports are spotlighting inflation's persistent toll on consumers and corporate margins."
    publisher: "Damian J. Troise"
    published_at: "2026-10-17T08:00:08.000Z"
    source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Damian J. Troise"
        source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
        retrieved_at: "2026-10-19T15:14:32+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the full annual core CPI distribution; the 8% binary on sub-2.2% outcome is a clean cross-check on the same question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Damian J. Troise: US earnings and economic reports this week to spotlight inflation’s to"
    url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    published_at: "2026-10-17T08:00:08.000Z"
    retrieved_at: "2026-10-19T15:14:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
