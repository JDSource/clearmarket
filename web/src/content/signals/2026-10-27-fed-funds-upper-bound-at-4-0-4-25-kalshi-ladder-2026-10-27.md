---
signal_id: "CMSIG2026102703"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-27"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound holds near 4 percent as inflation climbs"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (current meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 155.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder shows 85% above 4.0% and only 8% above 4.25%, placing the implied upper bound firmly in the 4.0-4.25% range."
  - "EconoTimes reports markets priced a 90% hold probability; the Kalshi ladder's sharp cutoff above 4.25% is consistent with that read."
  - "September CPI at 3.7% year-over-year, driven largely by gasoline, keeps the Fed's hiking bias intact even as it pauses today."
  - "The Kalshi contract on a cut greater than 25bp this year (CM-EVT-RWRZ1R3SD6) at 3% reinforces there is no pricing for near-term easing despite the inflation backdrop."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Annual CPI accelerated to 3.7% ahead of the October Fed meeting, with markets seen at 90% probability of a hold."
    publisher: "Miriam Hart"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://econotimes.com/Fed-Meets-as-Annual-Inflation-Accelerates-to-3-7-Before-U-S-Election-1764363"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/Fed-Meets-as-Annual-Inflation-Accelerates-to-3-7-Before-U-S-Election-1764363"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing at 4.0-4.25% is consistent with the 90% hold consensus cited in the EconoTimes report and the 3.7% CPI reading."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: Fed Meets as Annual Inflation Accelerates to 3.7% Before U.S. Election"
    url: "https://econotimes.com/Fed-Meets-as-Annual-Inflation-Accelerates-to-3-7-Before-U-S-Election-1764363"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
