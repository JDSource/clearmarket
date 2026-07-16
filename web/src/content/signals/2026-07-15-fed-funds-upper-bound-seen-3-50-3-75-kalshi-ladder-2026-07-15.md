---
signal_id: "CMSIG2026071504"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-07-15"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound anchors in the 3.50 to 3.75 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-15T18:15:29.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 115.27
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices 91% above 3.50% but only 36% above 3.75%, pinning the implied upper bound in the 3.50-3.75% range."
  - "Beige Book showing mild inflation easing is consistent with a market that sees no near-term rate shock in either direction."
  - "The 4.0% strike prices at just 4%, and 4.25% and above price at 3% or less, markets are ruling out any aggressive hike path."
  - "A longer-dated Kalshi ladder for the current period prices 99% above 3.50% and only 3% above 3.75%, echoing the same implied range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed's Beige Book signaled improving economic activity and slightly easing inflation, with fuel costs and tariffs flagged as persistent risks."
    publisher: "Thomson Reuters"
    published_at: "2026-07-15T18:15:29.000Z"
    source_url: "https://wqxc.com/2026/07/15/economic-activity-on-the-rise-and-inflation-may-be-improving-fed-survey-shows/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://wqxc.com/2026/07/15/economic-activity-on-the-rise-and-inflation-may-be-improving-fed-survey-shows/"
        retrieved_at: "2026-07-16T17:20:43+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official policy announcement; each strike resolves independently at the relevant meeting date."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Economic activity rising and inflation easing slightly, Fed survey sho"
    url: "https://wqxc.com/2026/07/15/economic-activity-on-the-rise-and-inflation-may-be-improving-fed-survey-shows/"
    published_at: "2026-07-15T18:15:29.000Z"
    retrieved_at: "2026-07-16T17:20:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
