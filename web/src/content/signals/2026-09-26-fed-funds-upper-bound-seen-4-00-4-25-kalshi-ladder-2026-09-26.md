---
signal_id: "CMSIG2026092602"
signal_slug: "fed-funds-upper-bound-seen-4-00-4-25-kalshi-ladder-2026-09-26"
headline: "Fed funds upper bound seen 4.00-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen holding in the 4.00-4.25 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T07:46:09.422Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.48
  volume_24h_usd: 41.63
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 4.00-4.25% range: 89% above 4.00% but only 48% above 4.25%, with a sharp falloff to 9% above 4.50%."
  - "Strong PMI and hawkish Fed signals align with the market holding the upper bound in this range rather than pricing imminent cuts."
  - "The steep drop in probability above 4.25% suggests the market sees a ceiling there, even with yields climbing."
  - "Fed officials' updated 2027 rate forecast of 4.1%, up from 3.6% in June, is broadly consistent with the current ladder distribution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Hawkish Fed officials and a surge in PMI to a five-year high have markets pricing a higher-for-longer rate path."
    publisher: "Nasdaq"
    published_at: "2026-09-26T07:46:09.422Z"
    source_url: "https://www.nasdaq.com/economic-institute/chartstopper-092526"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nasdaq"
        source_url: "https://www.nasdaq.com/economic-institute/chartstopper-092526"
        retrieved_at: "2026-09-27T07:47:06+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via Federal Reserve policy announcement; the 4.00-4.25% implied range is the modal outcome per current strike probabilities."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nasdaq: Chartstopper: September 25, 2026"
    url: "https://www.nasdaq.com/economic-institute/chartstopper-092526"
    published_at: "2026-09-26T07:46:09.422Z"
    retrieved_at: "2026-09-27T07:47:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
