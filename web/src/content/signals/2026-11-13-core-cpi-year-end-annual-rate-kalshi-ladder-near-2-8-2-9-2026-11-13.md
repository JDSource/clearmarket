---
signal_id: "CMSIG2026111302"
signal_slug: "core-cpi-year-end-annual-rate-kalshi-ladder-near-2-8-2-9-2026-11-13"
headline: "Core CPI year-end annual rate: Kalshi ladder near 2.8-2.9%"
semantic_title: "Core CPI annual rate odds cluster near 2.8-2.9 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T17:55:00.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI annual rate (year-end)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.41
  volume_24h_usd: 2282.86
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder puts the core CPI annual rate near 2.8-2.9%: 66% above 2.8%, 41% above 2.9%, dropping to 19% above 3.0%."
  - "Trading volume surged approximately 35,000x day-over-day on this contract, signaling intense fresh attention after the hot October print."
  - "The market stops well short of a 3%-plus scenario despite hawkish Fed rhetoric, implying the market sees stickiness but not a runaway re-acceleration."
  - "Unemployment ladder (CM-EVT-RBY62SKLC0) prices only 3% odds of joblessness reaching 4.5%, suggesting the market sees inflation persistence alongside a resilient labor market."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October jobs report showed 165,000 new jobs and stubborn inflation, cementing expectations for a Fed December hike."
    publisher: "Arben Skivjani"
    published_at: "2026-11-13T17:55:00.000Z"
    source_url: "https://www.realpage.com/analytics/economy-express-episode-75/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Arben Skivjani"
        source_url: "https://www.realpage.com/analytics/economy-express-episode-75/"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics CPI release; volume surge of 34,999x is real day-over-day data from marks history."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Arben Skivjani: Economy Express Episode 75"
    url: "https://www.realpage.com/analytics/economy-express-episode-75/"
    published_at: "2026-11-13T17:55:00.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
