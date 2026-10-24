---
signal_id: "CMSIG2026102301"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-23"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound priced between 4.0 and 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-23T19:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.11
  volume_24h_usd: 11.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the federal funds upper bound in the 4.0-4.25% range: 96% above 3.75%, only 11% above 4.25%."
  - "The Fed's unanimous 25bp hike to 3.75-4.00% is fully consistent with the ladder's modal pricing at the 4.0% strike sitting at 76%."
  - "Trading volume on the Kalshi rate-cut contract (CM-EVT-RWRZ1R3SD6) surged 7,152% day-over-day, signaling sharp fresh attention on the tightening path following the hike."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) implies the upper bound near 3.75-4.0%, with 4.0% at only 7%, likely keyed to an earlier meeting, revealing market doubt about further hikes beyond today's move."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve voted unanimously to raise rates 25 basis points to 3.75-4.00%, with Chair Kevin Warsh defying White House pressure to launch a tightening cycle."
    publisher: "BigGo Finance"
    published_at: "2026-10-23T19:00:00.000Z"
    source_url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BigGo Finance"
        source_url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
        retrieved_at: "2026-10-24T07:48:16+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distributes probability tightly around 4.0-4.25%, while the companion rate-cut contract at 3% on Kalshi confirms markets see virtually no chance of reversal this year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BigGo Finance: Federal Reserve Votes Unanimously to Raise Rates 25 Basis Points to 3."
    url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
    published_at: "2026-10-23T19:00:00.000Z"
    retrieved_at: "2026-10-24T07:48:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
