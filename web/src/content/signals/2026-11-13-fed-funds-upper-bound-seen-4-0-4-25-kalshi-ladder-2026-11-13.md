---
signal_id: "CMSIG2026111301"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-11-13"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound priced in the 4.0-4.25% range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T19:55:01.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 280.93
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 96% above 4.0%, but only 10% above 4.25%."
  - "Multiple Fed officials backed further hikes this week, consistent with the ladder pricing a hike to 4.0-4.25% but resisting the 4.5% scenario."
  - "The sharp drop from 96% to 10% between 4.0% and 4.25% strikes suggests the market sees one hike as near-certain but a second consecutive move as unlikely."
  - "Kalshi's rate-cut contract (CM-EVT-RWRZ1R3SD6) sits at just 2% for a cut greater than 25 bps this year, fully consistent with the hike-leaning ladder read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bloomberg reports Fed officials signaled December and possibly January rate hikes after hot October CPI and strong jobs data."
    publisher: "Enda Curran"
    published_at: "2026-11-13T19:55:01.000Z"
    source_url: "https://finance.yahoo.com/economy/policy/articles/fed-track-raise-interest-rates-195501318.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Enda Curran"
        source_url: "https://finance.yahoo.com/economy/policy/articles/fed-track-raise-interest-rates-195501318.html"
        retrieved_at: "2026-11-16T07:48:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve announcement; the 4.0-4.25% implied range aligns with consensus Fed rhetoric but rules out an aggressive double-step."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Enda Curran: Fed on Track to Raise Interest Rates Next Month And Maybe Again in Jan"
    url: "https://finance.yahoo.com/economy/policy/articles/fed-track-raise-interest-rates-195501318.html"
    published_at: "2026-11-13T19:55:01.000Z"
    retrieved_at: "2026-11-16T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
