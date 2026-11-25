---
signal_id: "CMSIG2026112302"
signal_slug: "core-cpi-above-2-for-2026-kalshi-ladder-99-2026-11-23"
headline: "Core CPI above 2% for 2026: Kalshi ladder 99%"
semantic_title: "Core CPI above 2 percent holds near full pricing for 2026"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T21:01:16.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate (2026 annual)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.3
  volume_24h_usd: 46.42
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder prices 99% odds that core CPI stays above 2.0% for the year ending in 2026, with the market-implied range near 2.8-2.9%."
  - "Williams acknowledged slow disinflation progress; the ladder distribution is consistent with that narrative, showing only 5% odds inflation falls to 3.0% or above on the high side."
  - "The 2.9% strike carries just 30% odds, meaning markets see the most likely landing zone as 2.7-2.8%, above the Fed's 2% target but not re-accelerating sharply."
  - "The Kalshi contract resolves via Bureau of Labor Statistics CPI data; the annual reading aggregates monthly prints, so a single surprise month can shift the implied range materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams discussed the Fed's dual mandate, noting inflation progress remains incomplete and AI is reshaping the economic outlook."
    publisher: "Julie Lasson"
    published_at: "2026-11-23T21:01:16.000Z"
    source_url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Julie Lasson"
        source_url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
        retrieved_at: "2026-11-25T07:47:45+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on core CPI year-over-year; distribution tightly clusters around 2.7-2.9%, consistent with Williams's characterization of stubbornly above-target inflation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Julie Lasson: Key Takeaways from President Williams’s Speech on the Economic Outlook"
    url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
    published_at: "2026-11-23T21:01:16.000Z"
    retrieved_at: "2026-11-25T07:47:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
