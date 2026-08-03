---
signal_id: "CMSIG2026080302"
signal_slug: "fed-funds-upper-bound-seen-3-75-kalshi-ladder-2026-08-03"
headline: "Fed funds upper bound seen 3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound holds near 3.75 percent after July pause"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound post-July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 9.76
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 98% above 3.50% and 58% above 3.75%, pinning the implied upper bound squarely at 3.75%."
  - "The 9-3 hold at 3.50-3.75% is fully consistent with the ladder's distribution; the three hawkish dissents keep a small tail alive above 3.75%."
  - "The sharp drop to 2% above 4.00% shows the market is not pricing a near-term hike despite the dissent noise."
  - "Polymarket (CM-EVT-87QV1G78C4) at 68% for any 2026 hike introduces a longer-horizon tension: ladder says ceiling now, but majority expects a move before year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The FOMC voted 9-3 to hold the federal-funds target at 3.50-3.75% on July 29, with three hawkish dissents."
    publisher: "111things.com"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://111things.com/national/three-fed-dissents-make-near-term-rate-relief-less-certain/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "111things.com"
        source_url: "https://111things.com/national/three-fed-dissents-make-near-term-rate-relief-less-certain/"
        retrieved_at: "2026-08-03T11:18:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the FOMC's announced target range; the distribution tightly brackets 3.75% with minimal mass above 4.00%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "111things.com: Three Fed dissents make near-term rate relief less certain | Interacti"
    url: "https://111things.com/national/three-fed-dissents-make-near-term-rate-relief-less-certain/"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-03T11:18:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
