---
signal_id: "CMSIG2026092101"
signal_slug: "fed-funds-upper-bound-implied-4-0-4-25-kalshi-ladder-2026-09-21"
headline: "Fed funds upper bound implied 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen in 4.0-4.25% range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (post-September)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.42
  volume_24h_usd: 2423.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 4.0-4.25% range: 86% above 4.0%, but only 42% above 4.25%, with a sharp dropoff above 4.5% at 10%."
  - "St. Louis Fed President Alberto Musalem's call for more hikes is broadly consistent with market pricing, which already embeds a meaningful probability of at least one further move above 4.0%."
  - "Trading volume on this ladder surged 517x day over day, signaling a sharp jump in market attention following Musalem's comments."
  - "The fat tail collapses quickly above 4.5%: only 2% probability above 4.75%, suggesting markets credit Musalem's hawkish posture but do not price an aggressive multi-hike path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "St. Louis Fed President Alberto Musalem said more rate hikes are likely needed to quell inflation, signaling continued tightening beyond the September meeting."
    publisher: "Howard Schneider"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Howard Schneider"
        source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
        retrieved_at: "2026-09-23T13:17:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; volume spike of 517x day over day confirms fresh positioning around post-September rate path following Musalem remarks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Howard Schneider: EXCLUSIVE: Fed's Musalem says more rate hikes likely needed to quell i"
    url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-23T13:17:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
