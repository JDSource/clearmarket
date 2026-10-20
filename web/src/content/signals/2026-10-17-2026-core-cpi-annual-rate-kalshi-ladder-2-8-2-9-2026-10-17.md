---
signal_id: "CMSIG2026101702"
signal_slug: "2026-core-cpi-annual-rate-kalshi-ladder-2-8-2-9-2026-10-17"
headline: "2026 core CPI annual rate: Kalshi ladder 2.8-2.9%"
semantic_title: "Full-year core CPI seen landing near 2.8-2.9 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T08:00:08.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "2026 full-year core CPI rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.38
  volume_24h_usd: 383.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder implies the 2026 full-year core CPI rate in the 2.8-2.9% range: 57% above 2.8%, but only 38% above 2.9%."
  - "Trading volume on this contract rose 458x day over day, consistent with the week's inflation focus drawing heavy fresh positioning."
  - "A market-implied range of 2.8-2.9% means the market expects core CPI to stay well above the Fed's 2% target through year-end."
  - "The separate Kalshi binary (CM-EVT-K0L95NMQ77) puts only 8% odds on core CPI falling below 2.2% in 2026, confirming the ladder's above-target consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "AP notes US inflation data this week will test whether price pressures are sustainably retreating toward the Fed's target."
    publisher: "Damian J. Troise"
    published_at: "2026-10-17T08:00:08.000Z"
    source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Damian J. Troise"
        source_url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
        retrieved_at: "2026-10-20T07:47:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; 458x volume surge is the sharpest single-day activity signal in this data set, reflecting intense market focus on the annual core print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Damian J. Troise: US earnings and economic reports this week to spotlight inflation’s to"
    url: "https://apnews.com/article/earnings-inflation-technology-housing-employment-3982e18ed2061f793aa921b6addade05"
    published_at: "2026-10-17T08:00:08.000Z"
    retrieved_at: "2026-10-20T07:47:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
