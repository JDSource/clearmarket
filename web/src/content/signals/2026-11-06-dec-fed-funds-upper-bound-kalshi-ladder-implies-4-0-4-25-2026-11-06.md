---
signal_id: "CMSIG2026110601"
signal_slug: "dec-fed-funds-upper-bound-kalshi-ladder-implies-4-0-4-25-2026-11-06"
headline: "Dec Fed funds upper bound: Kalshi ladder implies 4.0-4.25%"
semantic_title: "Fed funds upper bound seen near 4.0 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound post-December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 45.02
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the Fed funds upper bound in the 4.0-4.25% range: 77% above 4.0% but only 1% above 4.25%."
  - "October payrolls surged 165,000 versus a 65,000 consensus, and San Francisco Fed President Mary Daly said higher rates are likely needed, the ladder pricing is broadly consistent with one more hike."
  - "The sharp cliff from 77% at 4.0% to 1% at 4.25% signals markets see the terminal rate near 4.0-4.25%, not a prolonged tightening cycle."
  - "The Polymarket contract on a 2026 Fed emergency cut sits at 2%, corroborating the Kalshi ladder: markets price deliberate hiking, not a panic pivot."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A stronger-than-expected October jobs report bolstered the case for a December Fed rate hike, with multiple policymakers signaling readiness to act."
    publisher: "streetinsider.com"
    published_at: "2026-11-06T00:00:00.000Z"
    source_url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "streetinsider.com"
        source_url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
        retrieved_at: "2026-11-07T14:38:54+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution implies a narrow consensus around one more hike bringing the upper bound to 4.0-4.25%; the 99% readings at lower strikes confirm all prior hikes are fully priced."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "streetinsider.com: Fed seen sticking to December rate hike after jobs data"
    url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
    published_at: "2026-11-06T00:00:00.000Z"
    retrieved_at: "2026-11-07T14:38:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
