---
signal_id: "CMSIG2026090701"
signal_slug: "fed-funds-upper-bound-seen-at-3-75-4-0-ladder-pricing-2026-09-07"
headline: "Fed funds upper bound seen at 3.75-4.0%: ladder pricing"
semantic_title: "Fed funds rate above 4 percent stays a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 19.2
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Prediction market ladder prices the Fed funds upper bound in the 3.75-4.0% range: 76% above 3.75%, but only 36% above 4.0%."
  - "UBS calls for two hikes in 2026, but markets price just a single hike as the most likely terminal destination, not two."
  - "The 4.25% strike sits at only 7%, suggesting the market firmly fades the most aggressive analyst forecasts."
  - "The Polymarket contract on any Fed rate hike in 2026 sits at 70%, consistent with one hike being priced as the base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "UBS forecasts two Fed rate hikes in 2026 following a stronger-than-expected August jobs report showing 162,000 payrolls added."
    publisher: "reuters.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/ubs-forecasts-two-us-fed-rate-hikes-2026-after-strong-jobs-report-2026-09-07/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "reuters.com"
        source_url: "https://www.reuters.com/business/ubs-forecasts-two-us-fed-rate-hikes-2026-after-strong-jobs-report-2026-09-07/"
        retrieved_at: "2026-09-08T12:33:52+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder distribution shows the market partially agrees with UBS on direction but stops well short of endorsing a two-hike path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "reuters.com: UBS forecasts two US Fed rate hikes in 2026 after strong jobs report |"
    url: "https://www.reuters.com/business/ubs-forecasts-two-us-fed-rate-hikes-2026-after-strong-jobs-report-2026-09-07/"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-08T12:33:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
