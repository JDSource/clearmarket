---
signal_id: "CMSIG2026102806"
signal_slug: "fed-funds-upper-bound-post-oct-kalshi-ladder-4-0-4-25-2026-10-28"
headline: "Fed funds upper bound post-Oct: Kalshi ladder ~4.0-4.25%"
semantic_title: "Fed funds upper bound seen firmly in the 4.0 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T18:04:42.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following October 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 40.85
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 4.0-4.25% range: 73% above 4.0% but only 3% above 4.25%, implying 4.0-4.25% as the consensus zone."
  - "The October hold at approximately 3.9% is consistent with the 73% probability above 4.0%, which reflects the widely reported December hike expectation."
  - "Trading volume on this ladder surged 75,618% day-over-day (757x), the largest attention signal in the macro cluster, reflecting post-decision repricing activity."
  - "Resolution is tied to the Federal Reserve's official policy announcement; the December meeting is the next scheduled opportunity to move the upper bound above 4.0%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed held rates steady at its October meeting, with Chairman Kevin Warsh signaling fewer rate-setting meetings in future years and investors anticipating a December hike."
    publisher: "Scott Horsley"
    published_at: "2026-10-28T18:04:42.000Z"
    source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott Horsley"
        source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
        retrieved_at: "2026-10-30T14:47:28+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder's volume surge at 757x day-over-day is the dominant macro signal in today's session, with the distribution firmly anchoring expectations between 4.0% and 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott Horsley: Fed holds interest rates steady despite stubborn inflation : NPR"
    url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    published_at: "2026-10-28T18:04:42.000Z"
    retrieved_at: "2026-10-30T14:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
