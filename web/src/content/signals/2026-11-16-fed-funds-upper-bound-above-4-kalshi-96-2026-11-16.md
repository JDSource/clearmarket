---
signal_id: "CMSIG2026111601"
signal_slug: "fed-funds-upper-bound-above-4-kalshi-96-2026-11-16"
headline: "Fed funds upper bound above 4%: Kalshi 96%"
semantic_title: "Fed funds above 4 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T00:53:15.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.05
  volume_24h_usd: 712.76
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound solidly in the 4.00-4.25% range: 96% above 4.00%, but only 5% above 4.25%."
  - "Fed Vice Chair Philip Jefferson's hawkish inflation remarks are consistent with the market pricing a hold well above 4%; trading volume on this contract rose 1,190x day over day, signaling sharp fresh attention."
  - "PCE at 3.6% and a 5.7% annualized three-month CPI pace through October underpin the market's near-certain read that rates stay above 4%."
  - "The sharp drop from 96% to 5% between the 4.00% and 4.25% strikes suggests the market sees the current level as a ceiling, not a floor, a hike to 4.25%+ remains a small-tail risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Vice Chair Philip Jefferson said inflation's path is the key signal for policy, citing PCE at 3.6% and warning higher energy prices risk a broader, persistent rise."
    publisher: "Eamonn Sheridan"
    published_at: "2026-11-16T00:53:15.000Z"
    source_url: "https://investinglive.com/central-banks/icymi-fed-s-jefferson-says-inflation-is-the-key-signal-for-rates-with-pce-still-at-3-6/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eamonn Sheridan"
        source_url: "https://investinglive.com/central-banks/icymi-fed-s-jefferson-says-inflation-is-the-key-signal-for-rates-with-pce-still-at-3-6/"
        retrieved_at: "2026-11-17T07:48:04+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on the federal funds upper bound resolves via the FOMC policy decision; volume surge of 1,190x day over day confirms this is the week's most actively repriced macro contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eamonn Sheridan: ICYMI: Fed’s Jefferson says inflation is the key signal for rates, wit"
    url: "https://investinglive.com/central-banks/icymi-fed-s-jefferson-says-inflation-is-the-key-signal-for-rates-with-pce-still-at-3-6/"
    published_at: "2026-11-16T00:53:15.000Z"
    retrieved_at: "2026-11-17T07:48:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
