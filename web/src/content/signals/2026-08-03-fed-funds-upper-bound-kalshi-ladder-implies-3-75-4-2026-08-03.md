---
signal_id: "CMSIG2026080302"
signal_slug: "fed-funds-upper-bound-kalshi-ladder-implies-3-75-4-2026-08-03"
headline: "Fed funds upper bound: Kalshi ladder implies 3.75-4%"
semantic_title: "Fed funds upper bound seen near 3.75-4 percent late cycle"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds rate upper bound (late-cycle meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.33
  volume_24h_usd: 55.47
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.0% range: 70% above 3.75% but only 33% above 4.0%."
  - "Williams's conditional hike signal is consistent with the distribution, which keeps meaningful mass at 3.75% while fading a full move to 4.0%."
  - "A companion ladder (CM-EVT-4ZQLQPNH91) implies a sharper 3.75% ceiling, only 56% above 3.75% and just 2% above 4.0%, suggesting some term-structure divergence across meeting horizons."
  - "Resolution: Federal Reserve FOMC post-meeting statement provides the upper bound figure that settles each Kalshi strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams told Reuters he expects inflation to ease but warned the Fed will act if it does not."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/business/federal-reserve-bank-of-new-york-president-john-williams-expects-inflation-to-ease-says-fed-will-act-if-it-doesnt/articleshow/132827712.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/international/business/federal-reserve-bank-of-new-york-president-john-williams-expects-inflation-to-ease-says-fed-will-act-if-it-doesnt/articleshow/132827712.cms"
        retrieved_at: "2026-08-04T10:33:12+00:00"
  - type: "pm_response"
    notes: "Multiple Kalshi ladders across meeting dates cluster the implied upper bound in the 3.75-4.0% zone, consistent with a hold-with-hike-bias posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: Federal Reserve Bank of New York President John Williams expects infla"
    url: "https://economictimes.indiatimes.com/news/international/business/federal-reserve-bank-of-new-york-president-john-williams-expects-inflation-to-ease-says-fed-will-act-if-it-doesnt/articleshow/132827712.cms"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-04T10:33:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
