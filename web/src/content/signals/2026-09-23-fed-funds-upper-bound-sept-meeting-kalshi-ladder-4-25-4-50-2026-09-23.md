---
signal_id: "CMSIG2026092301"
signal_slug: "fed-funds-upper-bound-sept-meeting-kalshi-ladder-4-25-4-50-2026-09-23"
headline: "Fed funds upper bound Sept meeting: Kalshi ladder ~4.25-4.50%"
semantic_title: "Fed funds upper bound seen near 4.25% after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound post-Sept 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.06
  volume_24h_usd: 3.82
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-September 2026 Fed funds upper bound at 4.25-4.50%, with 90% above 4.0% but only 6% above 4.50%, implying a single hike is nearly fully priced."
  - "Richmond Fed President Tom Barkin's speech questioning the rationale for hiking is at odds with the market's near-consensus view of a hike arriving at this meeting."
  - "Volume on this ladder surged 7,989% day over day, signaling a sharp pickup in fresh positioning around the September decision."
  - "The companion December ladder (CM-EVT-6BS28TS762) implies a slightly lower modal range of 4.0-4.25%, suggesting markets see the September hike as a possible one-and-done rather than the start of a cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Richmond Fed President Tom Barkin publicly asked 'why hike,' signaling internal Fed debate as markets price a second consecutive tightening."
    publisher: "insurancenewsnet.com"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://insurancenewsnet.com/oarticle/why-hike"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "insurancenewsnet.com"
        source_url: "https://insurancenewsnet.com/oarticle/why-hike"
        retrieved_at: "2026-09-25T07:47:46+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder with 80.9x volume surge; market-implied range 4.25-4.50% upper bound after September 2026 FOMC meeting."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "insurancenewsnet.com: WHY HIKE? - Insurance News | InsuranceNewsNet"
    url: "https://insurancenewsnet.com/oarticle/why-hike"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-25T07:47:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
