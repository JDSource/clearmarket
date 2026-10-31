---
signal_id: "CMSIG2026102801"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-28"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate seen topping out near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T18:04:42.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 20.98
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 4.00-4.25% range, with 72% above 4.00% but only 3% above 4.25%."
  - "The Fed held rates steady as reported, but the ladder's sharp drop above 4.25% shows the market is consistent with one more hike, not a prolonged tightening cycle."
  - "NPR and multiple outlets report investors expect a December hike; the ladder's 72% at 4.00% and near-zero above 4.25% prices exactly one 25bp move."
  - "Resolution hinges on the named settlement source, the actual federal funds upper bound set by the FOMC at or before the December 2026 meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held interest rates steady at its October 2026 meeting, with investors widely expecting a December hike to combat stubborn inflation."
    publisher: "Scott Horsley"
    published_at: "2026-10-28T18:04:42.000Z"
    source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott Horsley"
        source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder on the post-December federal funds upper bound reflects near-consensus for a single additional hike, with the distribution essentially ruling out anything beyond 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott Horsley: Fed holds interest rates steady despite stubborn inflation : NPR"
    url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    published_at: "2026-10-28T18:04:42.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
