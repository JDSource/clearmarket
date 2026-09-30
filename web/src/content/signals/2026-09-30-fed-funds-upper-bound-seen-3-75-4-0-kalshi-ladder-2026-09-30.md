---
signal_id: "CMSIG2026093001"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-09-30"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen landing at 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound (next hike cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 22175.38
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder pins the fed funds upper bound in the 3.75-4.0% range: 98% above 3.75% but only 34% above 4.0%, implying one more hike is the consensus."
  - "New York Fed President John Williams called for one more late-2026 hike; the distribution is consistent with that single-hike view, not a more aggressive path."
  - "Volume surged 53x day over day on this ladder, signaling sharply rising market attention following Williams' public remarks."
  - "Beyond 4.0%, the ladder collapses to just 2% probability, suggesting markets firmly reject a scenario of multiple additional hikes from here."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams signaled one more rate hike in late 2026, saying there is no urgency to act after the most recent increase."
    publisher: "straitstimes.com"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
        retrieved_at: "2026-09-30T14:32:59+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the official federal funds rate target; the sharp break above 4.0% makes the single-hike read the dominant pricing outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: US Federal Reserve’s Williams sees one more interest rate hike in late"
    url: "https://www.straitstimes.com/business/economy/us-federal-reserves-williams-sees-one-more-interest-rate-hike-in-late-2026"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T14:32:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
