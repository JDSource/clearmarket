---
signal_id: "CMSIG2026082401"
signal_slug: "next-fed-funds-upper-bound-seen-3-75-4-0-kalshi-2026-08-24"
headline: "Next Fed funds upper bound seen 3.75-4.0%: Kalshi"
semantic_title: "Markets lean toward a Fed hike by next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-24T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Next FOMC meeting Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the next Fed funds upper bound in the 3.75-4.0% range, with 54% above 3.75% but only 17% above 4.0%."
  - "Fed officials' hike signal is broadly consistent with this pricing: markets lean hawkish but stop well short of pricing a full hike as certain."
  - "A companion Kalshi ladder for the current bound (CM-EVT-4ZQLQPNH91) prices the rate firmly at 3.50-3.75%, implying the market sees the next move, not the current one, as the hike risk."
  - "Resolves via Federal Reserve official rate announcement; any July-hold confirmation would collapse the 3.75%+ tail sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve officials signaled at their July meeting that a rate hike may be needed if inflation fails to cool, reinforcing hawkish posture ahead of Jackson Hole."
    publisher: "Chris Martin"
    published_at: "2026-08-24T00:00:00.000Z"
    source_url: "https://eciks.org/23074-fed-rate-hike-inflation-signal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Chris Martin"
        source_url: "https://eciks.org/23074-fed-rate-hike-inflation-signal"
        retrieved_at: "2026-08-25T08:36:45+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both near-term and forward Fed funds ladders; the spread between them captures the hike-or-hold debate playing out at Jackson Hole this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Chris Martin: Fed officials signal rate hike may be needed if inflation doesn't cool"
    url: "https://eciks.org/23074-fed-rate-hike-inflation-signal"
    published_at: "2026-08-24T00:00:00.000Z"
    retrieved_at: "2026-08-25T08:36:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
