---
signal_id: "CMSIG2026091601"
signal_slug: "fed-funds-upper-bound-post-sep-kalshi-ladder-4-0-4-25-2026-09-16"
headline: "Fed funds upper bound post-Sep: Kalshi ladder 4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-16T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.25
  volume_24h_usd: 987.41
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the post-September federal funds upper bound squarely in the 4.00-4.25% range: 99% above 3.75%, 81% above 4.00%, but only 25% above 4.25%."
  - "The hike to 3.75%-4.00% is consistent with the 81% at-or-above 4.00% reading; the 25% at 4.25% captures the one additional hike the Fed signaled for year-end."
  - "The sharp drop from 81% to 25% between the 4.00% and 4.25% strikes shows the market is pricing one more hike as possible but not certain."
  - "The Kalshi contract on a rate cut greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) sits at just 1%, fully consistent with the tightening bias the ladder reflects."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve raised its benchmark rate 25 basis points to 3.75%-4.00% and signaled one more hike in 2026."
    publisher: "Bryan Mena"
    published_at: "2026-09-16T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/16/economy/fed-rate-decision-september"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bryan Mena"
        source_url: "https://www.cnn.com/2026/09/16/economy/fed-rate-decision-september"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve; the distribution tightly brackets the Fed's own dot-plot guidance of a 4.00%-4.25% terminal rate by year-end 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bryan Mena: The Fed raises interest rates for the first time since July 2023 | CNN"
    url: "https://www.cnn.com/2026/09/16/economy/fed-rate-decision-september"
    published_at: "2026-09-16T00:00:00.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
