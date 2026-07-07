---
signal_id: "CMSIG2026070602"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-07-06"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Near-term Fed funds above 3.5 percent consensus anchors firm"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-06T19:35:27.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound following next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 15843.69
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder implies Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50%, collapsing to only 15% above 3.75%."
  - "Waller's July hike signal aligns with the ladder's strong pricing above 3.50%, but the 15% reading at 3.75% shows markets are not convinced a full hike to 4% materializes."
  - "The 83-percentage-point cliff between the 3.50% and 3.75% strikes is the sharpest inflection in the distribution, pinpointing where market conviction breaks down."
  - "Cross-reference with the Kalshi contract on a cut greater than 25 basis points at 10% confirms the market sees virtually no easing scenario in 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Christopher Waller flagged a potential July rate hike as inflation risks mounted, citing rising inflation dots."
    publisher: "Iwona Majkowska"
    published_at: "2026-07-06T19:35:27.000Z"
    source_url: "https://ts2.tech/en/feds-waller-flags-july-hike-as-inflation-dots-rise/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Iwona Majkowska"
        source_url: "https://ts2.tech/en/feds-waller-flags-july-hike-as-inflation-dots-rise/"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve policy announcement; the 3.75% strike is the swing point where Waller's hawkishness has not yet converted into full market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Iwona Majkowska: Fed’s Waller flags July hike as inflation dots rise"
    url: "https://ts2.tech/en/feds-waller-flags-july-hike-as-inflation-dots-rise/"
    published_at: "2026-07-06T19:35:27.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
