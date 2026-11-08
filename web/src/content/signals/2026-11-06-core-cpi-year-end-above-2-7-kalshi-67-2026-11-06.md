---
signal_id: "CMSIG2026110601"
signal_slug: "core-cpi-year-end-above-2-7-kalshi-67-2026-11-06"
headline: "Core CPI year-end above 2.7%: Kalshi 67%"
semantic_title: "Core CPI above 2.7 percent stays near 50-50 odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T20:48:24.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.8"
  question_raw: "Will the rate of core CPI inflation be above 2.8% for the year ending in November 2026?"
  current_price: 0.25
  volume_24h_usd: 160.75
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder pins core CPI in the 2.7-2.8% range: 67% above 2.7%, only 25% above 2.8%."
  - "Volume surged 162x day-over-day on this contract, signaling the blowout jobs print is drawing fresh attention to the inflation outlook."
  - "The 2.8% strike at 25% suggests markets are not fully pricing a renewed inflation surge despite the strong labor data."
  - "A companion Kalshi ladder on November 2026 monthly CPI change implies a range near 0.0-0.1%, consistent with a gradual, not runaway, path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October payrolls surged to 165,000, well above the 65,000 consensus, lifting the dollar and reinforcing hawkish Fed expectations."
    publisher: "Rich Asplund"
    published_at: "2026-11-06T20:48:24.000Z"
    source_url: "https://finance.yahoo.com/economy/policy/articles/dollar-gains-us-economic-strength-204824839.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rich Asplund"
        source_url: "https://finance.yahoo.com/economy/policy/articles/dollar-gains-us-economic-strength-204824839.html"
        retrieved_at: "2026-11-08T14:44:20+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on core CPI year-over-year rate saw 162x volume spike, the strongest signal in today's data set that the jobs print is repricing the inflation distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rich Asplund: Dollar Gains on US Economic Strength and Hawkish Fed"
    url: "https://finance.yahoo.com/economy/policy/articles/dollar-gains-us-economic-strength-204824839.html"
    published_at: "2026-11-06T20:48:24.000Z"
    retrieved_at: "2026-11-08T14:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
