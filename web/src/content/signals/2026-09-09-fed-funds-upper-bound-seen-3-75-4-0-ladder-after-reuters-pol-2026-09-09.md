---
signal_id: "CMSIG2026090902"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-ladder-after-reuters-pol-2026-09-09"
headline: "Fed funds upper bound seen 3.75-4.0%: ladder after Reuters poll"
semantic_title: "Fed funds upper bound seen staying near 3.75-4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-09T13:38:41.003Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting, post-2026)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.37
  volume_24h_usd: 71.11
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The rate ladder prices the upper bound in the 3.75-4.0% range: 93% above 3.50%, 79% above 3.75%, but only 37% above 4.0%."
  - "The Reuters poll consensus for a hold is broadly consistent with the ladder's center of gravity near 3.75-4.0%, though the rising minority view for a hike aligns with the 37% probability priced above 4.0%."
  - "A separate Polymarket contract puts 76% on the Fed raising rates at some point in 2026-2028, implying the terminal question is one of timing rather than direction."
  - "Resolution ties to the actual Federal Open Market Committee statement; a hike above 4.0% would need to clear the 37% hurdle priced by the ladder today."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters poll of economists found the Fed is expected to hold rates steady through the rest of 2026, though a rising number of analysts now see at least one hike."
    publisher: "Indradip Ghosh"
    published_at: "2026-09-09T13:38:41.003Z"
    source_url: "https://www.reuters.com/business/fed-hold-rates-steady-rest-2026-rising-number-analysts-see-least-one-hike-2026-09-09/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Indradip Ghosh"
        source_url: "https://www.reuters.com/business/fed-hold-rates-steady-rest-2026-rising-number-analysts-see-least-one-hike-2026-09-09/"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "Ladder distribution spans 2.75% through 5.25% and resolves via the official FOMC rate decision; the 4.0% strike at 37% is the key inflection between hold and hike scenarios."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Indradip Ghosh: Fed to hold rates steady in rest of 2026; rising number of analysts se"
    url: "https://www.reuters.com/business/fed-hold-rates-steady-rest-2026-rising-number-analysts-see-least-one-hike-2026-09-09/"
    published_at: "2026-09-09T13:38:41.003Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
