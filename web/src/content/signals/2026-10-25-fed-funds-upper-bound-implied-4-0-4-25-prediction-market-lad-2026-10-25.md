---
signal_id: "CMSIG2026102501"
signal_slug: "fed-funds-upper-bound-implied-4-0-4-25-prediction-market-lad-2026-10-25"
headline: "Fed funds upper bound implied 4.0-4.25%: prediction market ladder"
semantic_title: "Fed funds upper bound stays near 4 percent ahead of October meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound, October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 1.3
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Prediction market ladder pins the Fed funds upper bound in the 4.0-4.25% range: 78% above 4.0% but only 10% above 4.25%."
  - "With U.S. inflation at 3.7% and consensus firmly for a hold, the ladder is consistent with the near-unanimous economist view of no change this week."
  - "The sharp drop from 78% at 4.0% to 10% at 4.25% signals the market sees 4.0-4.25% as the ceiling, with tails above essentially closed."
  - "The 96% probability above 3.75% and near-zero above 4.5% suggest the market has fully priced a hold, with any hike beyond 4.25% treated as negligible risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. inflation hit 3.7% ahead of the Fed's October meeting, with a Reuters survey showing 94 of 100 economists expecting no change this week."
    publisher: "Miriam Hart"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
        retrieved_at: "2026-10-26T07:47:50+00:00"
  - type: "pm_response"
    notes: "Ladder contract (unspecified venue); distribution is tight around the 4.0-4.25% band, consistent with broad hold consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: U.S. Inflation Reaches 3.7% Ahead of Fed’s October Meeting | EconoTime"
    url: "https://econotimes.com/U-S-Inflation-Reaches-3-7-Ahead-of-Fed-s-October-Meeting-1762943"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-26T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
