---
signal_id: "CMSIG2026093004"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-ladder-99-28-2026-09-30"
headline: "Fed funds upper bound seen 3.75-4.0%: ladder 99%/28%"
semantic_title: "Longer-horizon Fed funds upper bound holds well below 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound (later 2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.28
  volume_24h_usd: 2850.47
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Ladder prices 99% above 3.75% but only 28% above 4.0%, placing the modal range firmly at 3.75-4.0% for a later 2026 meeting."
  - "New York Fed President John Williams signaled one more hike, but the market is fading full pricing of a move above 4.0%, assigning only 28% odds."
  - "The steep cliff from 99% to 28% at the 4.0% strike is the clearest single read: the market hears Williams but does not fully believe the hike clears 4.0%."
  - "Resolves via the Federal Reserve's official rate decision; settlement source not further specified in the candidate data."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams said there is one more rate hike likely in late 2026 but no urgency to act immediately."
    publisher: "straitstimes.com"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
        retrieved_at: "2026-10-02T07:47:52+00:00"
  - type: "pm_response"
    notes: "Ladder data carried via ClearMarket marks; Williams's hawkish signal is being partially faded by the distribution's sharp drop at the 4.0% strike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: US Federal Reserve’s Williams sees one more interest rate hike in late"
    url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-02T07:47:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
