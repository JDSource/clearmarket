---
signal_id: "CMSIG2026112302"
signal_slug: "core-cpi-above-2-8-year-over-year-kalshi-ladder-2026-11-23"
headline: "Core CPI above 2.8% year-over-year: Kalshi ladder"
semantic_title: "Core CPI above 2 percent holds near 75 percent odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T21:01:16.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.31
  volume_24h_usd: 826.71
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder puts the market-implied core CPI year-over-year rate near 2.8-2.9%, with 72% above 2.8% and 31% above 2.9%."
  - "Williams's remarks on persistent inflation are broadly consistent with the ladder's pricing, which keeps above-2.8% as the modal outcome, with trading volume up 1053x day over day, drawing significant fresh attention."
  - "The 5% probability above 3.0% shows markets are not pricing a re-acceleration to the levels that dominated 2022-2023 policy debates."
  - "Compare to the Kalshi binary contract (CM-EVT-K0L95NMQ77) pricing only 11% on core CPI falling below 2.2% in 2026, consistent with the ladder's upper-range skew."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams outlined the Fed's dual mandate challenges and signaled inflation remains elevated."
    publisher: "Julie Lasson"
    published_at: "2026-11-23T21:01:16.000Z"
    source_url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Julie Lasson"
        source_url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
        retrieved_at: "2026-11-24T07:47:50+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Bureau of Labor Statistics Employment Situation; volume surge signals the Williams speech drew substantial fresh positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Julie Lasson: Key Takeaways from President Williams’s Speech on the Economic Outlook"
    url: "https://tellerwindow.newyorkfed.org/2026/11/23/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-28/"
    published_at: "2026-11-23T21:01:16.000Z"
    retrieved_at: "2026-11-24T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
