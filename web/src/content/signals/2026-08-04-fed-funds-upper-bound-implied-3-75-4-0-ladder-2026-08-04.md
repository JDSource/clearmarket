---
signal_id: "CMSIG2026080403"
signal_slug: "fed-funds-upper-bound-implied-3-75-4-0-ladder-2026-08-04"
headline: "Fed funds upper bound implied 3.75%-4.0%: ladder"
semantic_title: "Fed funds upper bound seen near 3.75%-4.0%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound after next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 49.2
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Prediction market ladder prices the Fed funds upper bound near 3.75%-4.0%, with 52% above 3.75% but only 2% above 4.0%."
  - "Manufacturing revival and construction momentum described in the news suggest the economy is absorbing current rates, consistent with the ladder's pricing of modest further easing rather than aggressive cuts."
  - "Kansas City Fed President Jeff Schmid's call for tighter policy stands in tension with the ladder implying the upper bound sits well below 4.0%."
  - "A Kalshi contract (CM-EVT-RWRZ1R3SD6) puts only 5% odds on a cut greater than 25 basis points this year, reinforcing the ladder's read of a cautious, incremental Fed path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Rate-sensitive sectors including manufacturing and construction are gaining momentum as the economy adjusts to the Fed's prior tightening campaign."
    publisher: "Courtenay Brown"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.axios.com/2026/08/04/manufacturing-construction-labor-rates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Courtenay Brown"
        source_url: "https://www.axios.com/2026/08/04/manufacturing-construction-labor-rates"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Ladder pricing from prediction market strikes; Kalshi contract on outsized cuts resolves via Federal Reserve announcement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Courtenay Brown: More manufacturers are increasing employment, ISM survey finds"
    url: "https://www.axios.com/2026/08/04/manufacturing-construction-labor-rates"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
