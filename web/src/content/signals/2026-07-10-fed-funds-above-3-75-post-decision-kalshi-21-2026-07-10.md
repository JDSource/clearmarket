---
signal_id: "CMSIG2026071006"
signal_slug: "fed-funds-above-3-75-post-decision-kalshi-21-2026-07-10"
headline: "Fed funds above 3.75% post-decision: Kalshi 21%"
semantic_title: "Rate above 3.75 percent nears full pricing as anchor below that level"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T10:55:15.594Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound post-decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.21
  volume_24h_usd: 2978.55
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder shows 99% above 3.50% but only 21% above 3.75%, anchoring the consensus rate view firmly in the 3.50-3.75% range."
  - "The Fed report's 'stepped-up inflation' language is hawkish, but the market is not moving the upper bound probability above 3.75% into base-case territory."
  - "The 56% Kalshi reading on CM-EVT-P1KKDFWZ42 for the Fed raising rates at all in the 2026-2028 series is consistent with a market that prices hikes as possible but not certain."
  - "Resolves via Federal Reserve official decision; 99% certainty at 3.50% reflects a floor well-established before this report's release."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve's July 2026 Monetary Policy Report to Congress cited stepped-up inflation from tariffs, the Iran war, and AI buildout."
    publisher: "federalreserve.gov"
    published_at: "2026-07-10T10:55:15.594Z"
    source_url: "https://www.federalreserve.gov/monetarypolicy/files/20260710_mprfullreport.pdf"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "federalreserve.gov"
        source_url: "https://www.federalreserve.gov/monetarypolicy/files/20260710_mprfullreport.pdf"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder is consistent with markets absorbing hawkish Fed language without repricing a breakout above 3.75%, keeping the consensus pinned at the 3.50-3.75% band."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "federalreserve.gov: Monetary Policy Report, July 2026"
    url: "https://www.federalreserve.gov/monetarypolicy/files/20260710_mprfullreport.pdf"
    published_at: "2026-07-10T10:55:15.594Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
