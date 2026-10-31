---
signal_id: "CMSIG2026102802"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-ladder-74-2-2026-10-28"
headline: "Fed funds upper bound seen at 4.0-4.25%: ladder 74%/2%"
semantic_title: "Fed funds upper bound stays near 4 percent after hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T18:04:42.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 13.99
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The prediction market ladder puts 74% odds on the upper bound above 4.0% but only 2% above 4.25%, implying the next move is one 25-basis-point hike."
  - "The Fed held rates steady October 28, consistent with the ladder's near-certain pricing above 3.75% (98%), but the sharp drop above 4.25% says the market does not yet price two hikes."
  - "Two dissenters at the meeting sought an immediate hike; the market's concentration between 4.0% and 4.25% reflects that dissent as a December signal, not an imminent action."
  - "The Kalshi contract on a rate cut greater than 25 basis points this year sits at 1%, consistent with the ladder's hawkish-but-measured read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held its benchmark interest rate unchanged at its October 28 meeting, but investors widely expect a hike at the December meeting to combat stubborn inflation."
    publisher: "Scott Horsley"
    published_at: "2026-10-28T18:04:42.000Z"
    source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott Horsley"
        source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
        retrieved_at: "2026-10-31T14:15:55+00:00"
  - type: "pm_response"
    notes: "Ladder contract tracks the federal funds upper bound; Kalshi contract CM-EVT-RWRZ1R3SD6 (1% on a jumbo cut) resolves via the Federal Reserve, cross-confirming the rate-hike-not-cut narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott Horsley: Fed holds interest rates steady despite stubborn inflation : NPR"
    url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    published_at: "2026-10-28T18:04:42.000Z"
    retrieved_at: "2026-10-31T14:15:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
