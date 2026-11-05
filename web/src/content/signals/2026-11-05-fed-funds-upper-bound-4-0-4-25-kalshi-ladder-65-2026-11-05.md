---
signal_id: "CMSIG2026110501"
signal_slug: "fed-funds-upper-bound-4-0-4-25-kalshi-ladder-65-2026-11-05"
headline: "Fed funds upper bound 4.0-4.25%: Kalshi ladder 65%"
semantic_title: "Fed funds above 4 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T15:48:02.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (current cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 208.12
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 65% on the upper bound above 4.0%, with only 2% pricing above 4.25%, implying the market sees 4.0-4.25% as the likely ceiling."
  - "Barkin's hawkish framing is broadly consistent with the ladder, but the sharp drop from 65% to 2% above 4.25% signals the market sees 4.0% as near-terminal, not the start of a longer hike path."
  - "Cleveland Fed President Beth Hammack separately echoed the gradual-hike stance, adding a second voice to the same narrative the ladder already reflects."
  - "The Kalshi contract resolves via Federal Reserve official policy announcement; a surprise skip or pause at any upcoming meeting could collapse the 65% above-4.0% read quickly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Richmond Fed President Thomas Barkin backed a gradual rate-hike path, calling inflation the top risk and describing policy as straightforward."
    publisher: "Christian Borjon Valencia"
    published_at: "2026-11-05T15:48:02.000Z"
    source_url: "https://www.fxstreet.com/news/feds-barkin-backs-gradual-rate-hikes-as-inflation-stays-too-high-202611051548"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Christian Borjon Valencia"
        source_url: "https://www.fxstreet.com/news/feds-barkin-backs-gradual-rate-hikes-as-inflation-stays-too-high-202611051548"
        retrieved_at: "2026-11-05T16:02:36+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data provided; market treats 4.0-4.25% as the consensus destination, with tails above and below both priced as long shots."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Christian Borjon Valencia: Fed’s Barkin backs gradual rate hikes as inflation stays too high"
    url: "https://www.fxstreet.com/news/feds-barkin-backs-gradual-rate-hikes-as-inflation-stays-too-high-202611051548"
    published_at: "2026-11-05T15:48:02.000Z"
    retrieved_at: "2026-11-05T16:02:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
