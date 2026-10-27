---
signal_id: "CMSIG2026102701"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-27"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate seen peaking near 4 percent after October meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "October 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 71.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound squarely in the 4.0-4.25% range: 84% chance above 4.0%, only 8% above 4.25%."
  - "Market read is consistent with the hold officials telegraphed; trading volume on this contract is up 27,299% day over day, signaling heavy fresh attention as the meeting arrives."
  - "The sharp drop from 84% to 8% at the 4.25% strike captures the market's view: a hold this week is near-certain, but a December hike is not fully priced."
  - "The 4.5% strike sits at only 4%, meaning the Kalshi distribution rules out two more hikes as a live scenario for this cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve policymakers are widely expected to hold the key interest rate unchanged at the October meeting, with investors watching for signals on a December hike."
    publisher: "Christopher Rugaber"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://apnews.com/article/federal-reserve-kevin-warsh-interest-rates-991eeb23f8acd1e84b11de9b35278681"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Christopher Rugaber"
        source_url: "https://apnews.com/article/federal-reserve-kevin-warsh-interest-rates-991eeb23f8acd1e84b11de9b35278681"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on Fed funds upper bound is the dominant rate market focus this week, with volume surging 274x day over day ahead of the Wednesday decision."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Christopher Rugaber: What to look for at the Federal Reserve's next meeting | AP News"
    url: "https://apnews.com/article/federal-reserve-kevin-warsh-interest-rates-991eeb23f8acd1e84b11de9b35278681"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
